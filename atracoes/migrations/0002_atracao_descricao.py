# Generated by Django 2.2.5 on 2019-09-09 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atracoes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='atracao',
            name='descricao',
            field=models.TextField(default='testing'),
            preserve_default=False,
        ),
    ]