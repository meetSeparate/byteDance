# Generated by Django 4.2.7 on 2024-05-03 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_rename_compony_workinfo_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(verbose_name='用户id')),
                ('job_id', models.IntegerField(verbose_name='岗位id')),
                ('status', models.CharField(choices=[('待审核', '待审核'), ('待检阅', '待检阅'), ('面试中', '面试中'), ('待签约', '待签约'), ('已结束', '已结束')], default='待审核', max_length=256, verbose_name='投递状态')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='投递时间')),
            ],
            options={
                'verbose_name_plural': '投递记录',
            },
        ),
    ]
