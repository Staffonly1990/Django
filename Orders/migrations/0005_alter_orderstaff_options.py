# Generated by Django 3.2.2 on 2021-05-10 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0004_alter_orders_publication_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderstaff',
            options={'ordering': ['id'], 'verbose_name': 'Заказ/Пользователь', 'verbose_name_plural': 'Заказы/Пользователи'},
        ),
    ]