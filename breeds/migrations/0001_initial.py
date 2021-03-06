# Generated by Django 2.0.6 on 2018-06-13 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('type', models.CharField(blank=True, choices=[('dogs', 'dogs'), ('cats', 'cats')], max_length=255, null=True)),
                ('history', models.CharField(blank=True, max_length=65535, null=True)),
                ('character', models.CharField(blank=True, max_length=65535, null=True)),
                ('standard', models.CharField(blank=True, max_length=65535, null=True)),
                ('club', models.CharField(blank=True, max_length=255, null=True)),
                ('slug', models.CharField(blank=True, max_length=65535, null=True)),
            ],
            options={
                'verbose_name': 'Breed',
                'verbose_name_plural': 'Breeds',
                'db_table': 'animal_breeds',
            },
        ),
    ]
