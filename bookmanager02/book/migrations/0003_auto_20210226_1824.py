# Generated by Django 2.2.5 on 2021-02-26 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_remove_bookinfo_is_delete'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookinfo',
            name='comment_count',
        ),
        migrations.RemoveField(
            model_name='bookinfo',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='bookinfo',
            name='read_count',
        ),
    ]
