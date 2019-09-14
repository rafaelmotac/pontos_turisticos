# Generated by Django 2.2.5 on 2019-09-12 01:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('atracoes', '0003_atracao_ponto_turistico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atracao',
            name='ponto_turistico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pontos_turisticos', to='core.PontoTuristico'),
        ),
    ]