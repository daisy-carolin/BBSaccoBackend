# Generated by Django 4.2.7 on 2023-11-10 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('borrowers', '0001_initial'),
        ('useraccount', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrowers1',
            name='loan_officers_access',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='useraccount.user'),
        ),
        migrations.AddField(
            model_name='adduserinbranch',
            name='branch_id',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='borrowers.branch'),
        ),
        migrations.AddField(
            model_name='adduserinbranch',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='useraccount.user', unique=True),
        ),
    ]
