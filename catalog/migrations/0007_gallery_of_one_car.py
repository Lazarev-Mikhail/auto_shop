# Generated by Django 4.1 on 2022-09-12 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_alter_auto_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery_of_one_car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(default=None, upload_to='gallery_auto')),
                ('auto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='catalog.auto')),
            ],
        ),
    ]
