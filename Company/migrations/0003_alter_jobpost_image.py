# Generated by Django 4.1.5 on 2023-04-23 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0002_alter_jobpost_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]