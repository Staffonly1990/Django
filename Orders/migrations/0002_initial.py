# Generated by Django 3.2.2 on 2021-05-10 17:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderstaff',
            name='users',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователи'),
        ),
        migrations.AddField(
            model_name='orders',
            name='categories',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Orders.categories', verbose_name='Категории'),
        ),
    ]
