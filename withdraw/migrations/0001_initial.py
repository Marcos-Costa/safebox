# Generated by Django 2.0.2 on 2018-03-14 16:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('varys', '0016_auto_20180314_1611'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventSubscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Valor')),
                ('justification', models.CharField(default='', max_length=257, verbose_name='Justificativa')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data de criação')),
                ('receipt', models.FileField(blank=True, null=True, upload_to='comprovantes', verbose_name='Comprovante(s)')),
                ('name', models.CharField(max_length=64, verbose_name='Nome Do Evento')),
                ('date', models.CharField(max_length=32, verbose_name='Data do Evento')),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Inscrições em eventos',
                'verbose_name': 'Inscrição em evento',
            },
        ),
        migrations.CreateModel(
            name='Withdraw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Valor')),
                ('justification', models.CharField(default='', max_length=257, verbose_name='Justificativa')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data de criação')),
                ('receipt', models.FileField(blank=True, null=True, upload_to='comprovantes', verbose_name='Comprovante(s)')),
                ('origin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='varys.Box')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Saques',
                'verbose_name': 'Saque',
            },
        ),
    ]
