# Generated by Django 4.1.4 on 2023-01-12 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_alter_reproblems_pid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reproblems',
            name='MEMID',
            field=models.CharField(default='', max_length=43, verbose_name='會員序號'),
        ),
    ]
