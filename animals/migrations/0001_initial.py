# Generated by Django 2.0.6 on 2018-06-13 11:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('breeds', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kennels', '0002_auto_20180611_1023'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseAnimal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('type', models.CharField(blank=True, choices=[('dogs', 'dogs'), ('cats', 'cats')], max_length=100, null=True)),
                ('full_name', models.CharField(blank=True, max_length=256, null=True)),
                ('home_name', models.CharField(blank=True, max_length=100, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('deathday', models.DateField(blank=True, null=True)),
                ('color', models.CharField(blank=True, max_length=50, null=True)),
                ('height', models.CharField(blank=True, max_length=50, null=True)),
                ('registry', models.CharField(blank=True, max_length=50, null=True)),
                ('pedigree', models.URLField(blank=True, null=True)),
                ('entitlements', models.CharField(blank=True, max_length=2048, null=True)),
                ('gender', models.CharField(blank=True, choices=[('male', 'male'), ('female', 'female')], max_length=100, null=True)),
                ('achievements', models.CharField(blank=True, max_length=2048, null=True)),
                ('elbow_ed', models.CharField(blank=True, max_length=2048, null=True)),
                ('hip_hd', models.CharField(blank=True, max_length=2048, null=True)),
                ('tattoo', models.CharField(blank=True, max_length=50, null=True)),
                ('dna_data', models.CharField(blank=True, max_length=2048, null=True)),
                ('microchip', models.CharField(blank=True, max_length=50, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d')),
                ('about', models.CharField(blank=True, max_length=10000, null=True)),
                ('slug', models.CharField(blank=True, max_length=256, null=True)),
                ('is_owner', models.BooleanField(default=False)),
                ('breed', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='breeds.Breed')),
                ('father', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='father_dog', to='animals.BaseAnimal')),
                ('kennel_live', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='kennel_live', to='kennels.Kennel')),
                ('kennel_of_birth', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='kennel_birth', to='kennels.Kennel')),
                ('mother', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mother_dog', to='animals.BaseAnimal')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Animal',
                'verbose_name_plural': 'Animals',
                'db_table': 'kennel_animal',
            },
        ),
    ]
