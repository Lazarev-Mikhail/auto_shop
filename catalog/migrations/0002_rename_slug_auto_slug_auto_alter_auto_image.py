# Generated by Django 4.1 on 2022-08-27 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auto',
            old_name='slug',
            new_name='slug_auto',
        ),
        migrations.AlterField(
            model_name='auto',
            name='image',
            field=models.FileField(upload_to='gallery_auto'),
        ),
    ]