# Generated by Django 2.0.6 on 2018-07-09 10:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavoriteItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('source_id', models.IntegerField(blank=True, null=True)),
                ('type', models.CharField(blank=True, choices=[('kennel', 'kennel'), ('animal', 'animal'), ('litter', 'litter')], max_length=100, null=True)),
                ('follower', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Favorite Items',
                'verbose_name_plural': 'Favorite Item',
                'db_table': 'favorite_item',
            },
        ),
    ]
