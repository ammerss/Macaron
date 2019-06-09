# Generated by Django 2.1.7 on 2019-06-09 21:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('reser_num', models.BigIntegerField(default=0, primary_key=True, serialize=False)),
                ('choice_macaron', models.CharField(default='', max_length=10)),
                ('quantity', models.IntegerField(default=0)),
                ('amount', models.PositiveIntegerField(default=0)),
                ('reser_request_time', models.DateTimeField(auto_now_add=True)),
                ('reser_time', models.DateTimeField()),
                ('approve', models.IntegerField(default=0)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('shop_name', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='store.Store')),
            ],
        ),
    ]
