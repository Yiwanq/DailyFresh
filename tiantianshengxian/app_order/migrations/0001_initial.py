# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_goods', '0001_initial'),
        ('app_user', '0003_user_ushou'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count', models.IntegerField()),
                ('price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('goid', models.ForeignKey(to='app_goods.GoodsInfo')),
            ],
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('oid', models.IntegerField()),
                ('odate', models.DateTimeField()),
                ('opay_way', models.CharField(max_length=30)),
                ('is_paid', models.BooleanField(default=False)),
                ('oaddress', models.CharField(max_length=100)),
                ('ouser', models.ForeignKey(to='app_user.User')),
            ],
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='order',
            field=models.ForeignKey(to='app_order.OrderInfo'),
        ),
    ]
