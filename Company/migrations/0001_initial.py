# Generated by Django 4.1.5 on 2023-04-22 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('SignUp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='company_contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=50)),
                ('message', models.TextField(max_length=300)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='jobpost',
            fields=[
                ('job_id', models.AutoField(primary_key=True, serialize=False)),
                ('job_title', models.TextField(max_length=45)),
                ('salary', models.TextField(max_length=10)),
                ('experience_required', models.TextField(max_length=10)),
                ('jobtype', models.TextField(blank=True, max_length=45)),
                ('skill_required', models.CharField(blank=True, max_length=45, null=True)),
                ('education_level', models.CharField(max_length=255)),
                ('post_date', models.DateTimeField(auto_now=True)),
                ('last_date', models.CharField(blank=True, max_length=10, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media')),
                ('job_description', models.TextField(max_length=255)),
                ('companyname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SignUp.company')),
            ],
        ),
    ]