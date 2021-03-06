# Generated by Django 3.2.9 on 2022-03-05 14:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='date updated')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('url', models.URLField(unique=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sites', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'Site',
                'verbose_name_plural': 'Sites',
                'ordering': ('-date_created',),
            },
        ),
        migrations.CreateModel(
            name='Proxy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='date updated')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('ip', models.GenericIPAddressField(verbose_name='ip')),
                ('http_port', models.PositiveIntegerField(verbose_name='http port')),
                ('https_port', models.PositiveIntegerField(blank=True, null=True, verbose_name='https port')),
                ('socks_port', models.PositiveIntegerField(blank=True, null=True, verbose_name='socks port')),
                ('username', models.CharField(blank=True, max_length=255, verbose_name='username')),
                ('password', models.CharField(blank=True, max_length=255, verbose_name='password')),
                ('status', models.CharField(blank=True, max_length=255, verbose_name='status')),
                ('speed', models.FloatField(blank=True, null=True, verbose_name='speed')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='location.country', verbose_name='country')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='proxies', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'Proxy',
                'verbose_name_plural': 'Proxies',
                'ordering': ('-date_created',),
                'unique_together': {('ip', 'http_port')},
            },
        ),
    ]
