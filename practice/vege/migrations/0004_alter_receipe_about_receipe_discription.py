# Generated by Django 4.2.1 on 2023-06-21 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0003_rename_password_receipe_about_receipe_discription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipe_about',
            name='receipe_discription',
            field=models.TextField(max_length=200),
        ),
    ]
