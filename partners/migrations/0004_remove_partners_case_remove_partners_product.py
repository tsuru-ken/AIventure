# Generated by Django 4.2.7 on 2024-06-11 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0003_rename_enginner_partners_engineer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partners',
            name='case',
        ),
        migrations.RemoveField(
            model_name='partners',
            name='product',
        ),
    ]
