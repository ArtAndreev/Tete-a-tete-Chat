# Generated by Django 2.0.6 on 2018-07-01 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_attachment_content_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='text',
            field=models.TextField(null=True, verbose_name='Message text'),
        ),
    ]
