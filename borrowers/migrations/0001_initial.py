# Generated by Django 4.2.7 on 2023-11-10 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddBorrowersGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('notes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='AddUserInBranch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Borrowers1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=15)),
                ('country', models.CharField(default='IN', max_length=50)),
                ('title', models.CharField(max_length=15)),
                ('mobile', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('unique_number', models.CharField(max_length=30)),
                ('dob', models.DateField()),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=50)),
                ('zip_code', models.CharField(max_length=50)),
                ('bussiness_name', models.CharField(max_length=100)),
                ('working_status', models.CharField(choices=[('Owner', 'Owner'), ('Employee', 'Employee'), ('Student', 'Student'), ('Overseas Worker', 'Overseas Worker'), ('Pensioner', 'Pensioner'), ('Unemployed', 'Unemployed')], max_length=100)),
                ('photo', models.ImageField(upload_to='images/')),
                ('note', models.TextField()),
                ('files', models.FileField(upload_to='files/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(auto_now=True)),
                ('is_decline', models.BooleanField(default=False)),
                ('is_approve', models.BooleanField(default=False)),
                ('is_blacklist', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
