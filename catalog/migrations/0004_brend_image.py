# Generated by Django 4.1 on 2022-08-28 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_brend_remove_auto_mark_alter_auto_color_auto_brend'),
    ]

    operations = [
        migrations.AddField(
            model_name='brend',
            name='image',
            field=models.FileField(default=None, upload_to='gallery_auto'),
        ),
    ]
