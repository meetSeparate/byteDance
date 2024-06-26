# Generated by Django 4.2 on 2024-05-04 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_delivery_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResumeFile',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField(verbose_name='用户id')),
                ('file', models.FileField(upload_to='resume/', verbose_name='简历文件')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='上传时间')),
            ],
            options={
                'verbose_name_plural': '简历文件',
            },
        ),
    ]
