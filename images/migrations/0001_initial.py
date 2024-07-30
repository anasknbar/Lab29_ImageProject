# Generated by Django 5.0.7 on 2024-07-30 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_type', models.CharField(max_length=16)),
                ('tag', models.CharField(max_length=16)),
                ('webformatURL', models.URLField(max_length=256)),
                ('views', models.PositiveIntegerField(default=0)),
                ('downloads', models.PositiveIntegerField(default=0)),
                ('likes', models.PositiveIntegerField(default=0)),
                ('user', models.CharField(max_length=16)),
                ('userimageURL', models.URLField(max_length=256)),
            ],
            options={
                'ordering': ['-views'],
            },
        ),
    ]