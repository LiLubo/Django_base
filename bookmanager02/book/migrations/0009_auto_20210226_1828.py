# Generated by Django 2.2.5 on 2021-02-26 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0008_auto_20210226_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinfo',
            name='pub_date',
            field=models.DateField(null=True),
        ),
    ]