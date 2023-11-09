# Generated by Django 4.2.5 on 2023-11-09 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loanmanagement', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LoanApplicatin',
            new_name='LoanApplication',
        ),
        migrations.AlterField(
            model_name='borrowers',
            name='files',
            field=models.FileField(blank=True, null=True, upload_to='files/'),
        ),
        migrations.AlterField(
            model_name='borrowers',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
