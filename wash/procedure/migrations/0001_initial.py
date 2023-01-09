# Generated by Django 4.1.4 on 2023-01-09 12:24

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BID', models.CharField(max_length=20, verbose_name='洗衣袋編號')),
                ('MEMID', models.CharField(default=0, max_length=20, verbose_name='使用者編號')),
                ('GDATE', models.DateTimeField(default=django.utils.timezone.now, verbose_name='租借時間')),
                ('RDATE', models.DateTimeField(default=django.utils.timezone.now, verbose_name='歸還時間')),
            ],
        ),
        migrations.CreateModel(
            name='delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ORDID', models.CharField(max_length=20, verbose_name='訂單編號')),
                ('SHOPID', models.CharField(max_length=20, verbose_name='店鋪編號')),
                ('PHONE', models.CharField(max_length=10, verbose_name='使用者電話')),
                ('ADDRESS', models.CharField(max_length=40, verbose_name='使用者地址')),
                ('GDATE', models.DateTimeField(default=django.utils.timezone.now, verbose_name='取件時間')),
                ('S_CODE', models.CharField(max_length=20, verbose_name='取件條碼')),
                ('G_CODE', models.CharField(max_length=20, verbose_name='送件條碼')),
            ],
        ),
        migrations.CreateModel(
            name='FMODE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FMODE', models.CharField(max_length=20, verbose_name='模式名稱')),
                ('MONEY', models.IntegerField(verbose_name='價格')),
                ('POINTS', models.IntegerField(verbose_name='碳權點數')),
                ('MEMISSIONS', models.IntegerField(verbose_name='碳排(公斤)')),
                ('TIME', models.IntegerField(verbose_name='所需時間(分鐘)')),
            ],
        ),
        migrations.CreateModel(
            name='LMODE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LMODE', models.CharField(max_length=20, verbose_name='模式名稱')),
                ('MONEY', models.IntegerField(verbose_name='價格')),
                ('POINTS', models.IntegerField(verbose_name='碳權點數')),
                ('MEMISSIONS', models.IntegerField(verbose_name='碳排(公斤)')),
                ('TIME', models.IntegerField(verbose_name='所需時間(分鐘)')),
            ],
        ),
        migrations.CreateModel(
            name='lock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LOCKID', models.CharField(max_length=20, verbose_name='鎖櫃編號')),
                ('ORDID', models.CharField(max_length=20, verbose_name='訂單編號')),
                ('INDATE', models.DateTimeField(default=django.utils.timezone.now, verbose_name='放入時間')),
                ('OUTDATE', models.DateTimeField(default=django.utils.timezone.now, verbose_name='取出時間')),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ORDID', models.CharField(max_length=20, verbose_name='訂單編號')),
                ('MEMID', models.CharField(max_length=20, verbose_name='使用者編號')),
                ('APPID', models.IntegerField(verbose_name='app編號')),
                ('C_AMOUNT', models.IntegerField(verbose_name='花費的碳稅')),
                ('GPOINT', models.IntegerField(verbose_name='獲得的點數')),
                ('AMOUNT', models.IntegerField(verbose_name='消費總金額')),
                ('CDATE', models.DateTimeField(default=django.utils.timezone.now, verbose_name='成立時間')),
            ],
        ),
        migrations.CreateModel(
            name='shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SHOPID', models.CharField(max_length=20, verbose_name='店鋪編號')),
                ('SHOPNAME', models.CharField(max_length=10, verbose_name='店鋪名稱')),
                ('ADDRESS', models.CharField(max_length=40, verbose_name='使用者地址')),
            ],
        ),
        migrations.CreateModel(
            name='WMODE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('WMODE', models.CharField(max_length=20, verbose_name='模式名稱')),
                ('MONEY', models.IntegerField(verbose_name='價格')),
                ('POINTS', models.IntegerField(verbose_name='碳權點數')),
                ('MEMISSIONS', models.IntegerField(verbose_name='碳排(公斤)')),
                ('TIME', models.IntegerField(verbose_name='所需時間(分鐘)')),
            ],
        ),
        migrations.CreateModel(
            name='CLIST',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ORDID', models.CharField(max_length=20, verbose_name='訂單編號')),
                ('BAGNUM', models.IntegerField(default=1, verbose_name='袋數')),
                ('PRICE', models.IntegerField(default=0, verbose_name='總金額')),
                ('TIME', models.IntegerField(default=0, verbose_name='總時長')),
                ('FMODE', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='procedure.fmode')),
                ('LMODE', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='procedure.lmode')),
                ('WMODE', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='procedure.wmode')),
            ],
        ),
    ]
