# Generated by Django 2.2.5 on 2019-09-14 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('atracoes', '0004_auto_20190912_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atracao',
            name='ponto_turistico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='atracoes', to='core.PontoTuristico'),
        ),
    ]
