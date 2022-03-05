# Generated by Django 3.2.9 on 2022-03-05 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
        ('ddos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteCheckResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(verbose_name='status')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='location.country', verbose_name='country')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ddos.site', verbose_name='site')),
            ],
            options={
                'verbose_name': 'Site check result',
                'verbose_name_plural': 'Site check results',
                'ordering': ('-date_created',),
            },
        ),
    ]