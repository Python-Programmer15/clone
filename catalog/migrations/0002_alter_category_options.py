# Generated by Django 3.2.6 on 2021-09-09 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-created_at'], 'verbose_name_plural': 'categories'},
        ),
    ]
