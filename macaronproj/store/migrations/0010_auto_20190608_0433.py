# Generated by Django 2.2.2 on 2019-06-08 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_store_store_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='macarons',
            name='pic_content',
            field=models.CharField(max_length=200),
        ),
    ]