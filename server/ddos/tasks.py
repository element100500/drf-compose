import requests
from celery import shared_task, group, chain

from location.models import Country
from .models import Site, SiteCheckResult, Proxy


@shared_task()
def check_proxies():
    pks = Proxy.objects.all() \
        .values_list('pk', flat=True)

    group(check_proxy.s(pk) for pk in pks)()

    return list(pks)


@shared_task()
def check_proxy(pk):
    proxy = Proxy.objects.get(pk=pk)

    try:
        r = requests.get('https://google.com/', proxies=proxy.as_dict(), timeout=30)

        proxy.status = 'ok'
        proxy.speed = r.elapsed.total_seconds()
    except requests.exceptions.ProxyError:
        proxy.status = 'auth error'
        proxy.speed = None
    except requests.exceptions.ConnectTimeout:
        proxy.status = 'down'
        proxy.speed = None

    proxy.update_country()
    proxy.save(update_fields=('speed', 'status', 'country'))


@shared_task()
def check_sites():
    pks = Site.objects.all() \
        .values_list('pk', flat=True)

    group(check_site.s(pk) for pk in pks)()

    return list(pks)


@shared_task()
def check_site(pk):
    countries = Country.objects.filter(proxies__isnull=False).all()

    group(check_site_from_country.s(pk, country.pk) for country in countries)()


@shared_task(
    autoretry_for=(requests.exceptions.ProxyError,)
)
def check_site_from_country(site_pk, country_pk):
    site = Site.objects.get(pk=site_pk)
    proxy = Proxy.objects.filter(country_id=country_pk, status='ok').order_by('?').first()

    if proxy is None:
        raise Proxy.DoesNotExist

    site_check_result = False

    try:
        requests.get(site.url, proxies=proxy.as_dict(), timeout=30)
        site_check_result = True
    except requests.exceptions.ConnectTimeout:
        pass

    SiteCheckResult.objects.update_or_create(site=site, country_id=country_pk, defaults={
        'status': site_check_result
    })


@shared_task()
def parse_uashield_proxies():
    r = requests.get('https://raw.githubusercontent.com/opengs/uashieldtargets/master/proxy.json', timeout=5)
    proxies = r.json()

    for proxy in proxies:
        ip, http_port = proxy.get('ip', '').split(':')
        username, password = proxy.get('auth', '').split(':')

        try:
            Proxy.objects.update_or_create(
                ip=ip,
                http_port=http_port,
                defaults={
                    'username': username,
                    'password': password,
                }
            )
        except ValueError:
            continue


@shared_task()
def parse_uashield_sites():
    r = requests.get('https://raw.githubusercontent.com/opengs/uashieldtargets/master/sites.json', timeout=5)
    sites = r.json()

    for site in sites:
        Site.objects.update_or_create(url=site.get('page'))


@shared_task()
def update_geoip_db():
    db_url = 'https://download.maxmind.com/app/geoip_download'
    r = requests.get(db_url, params={
        'edition_id': 'GeoLite2-Country',
        'suffix': 'tar.gz',
        'license_key': 'XA5G2z06R0urAQ3q',
    })
    print(r.content)
