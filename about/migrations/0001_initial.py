# Generated by Django 3.2.25 on 2025-05-19 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label_1', models.CharField(max_length=255)),
                ('paragraph_1', models.TextField()),
                ('label_2', models.CharField(max_length=255)),
                ('paragraph_2', models.TextField()),
            ],
        ),
    ]
