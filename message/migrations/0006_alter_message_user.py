# Generated by Django 4.2.7 on 2024-04-18 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_rename_birth_date_profile_birthdate'),
        ('message', '0005_badword'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.profile'),
        ),
    ]
