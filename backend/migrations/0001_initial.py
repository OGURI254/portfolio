# Generated by Django 4.2.7 on 2023-11-04 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('year', models.IntegerField()),
                ('client', models.CharField(max_length=100)),
                ('services', models.TextField()),
                ('project', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='works/')),
            ],
        ),
        migrations.CreateModel(
            name='WorkImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='work_images/')),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.work')),
            ],
        ),
    ]
