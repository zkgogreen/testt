# Generated by Django 5.0 on 2023-12-25 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=224)),
                ('nama', models.CharField(max_length=224)),
                ('ket', models.CharField(max_length=224)),
            ],
        ),
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=224, unique=True)),
                ('keterangan', models.CharField(max_length=224)),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=224, unique=True)),
                ('keterangan', models.CharField(max_length=224)),
            ],
        ),
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=224, unique=True)),
                ('keterangan', models.CharField(max_length=224)),
            ],
        ),
        migrations.CreateModel(
            name='QnA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quest', models.CharField(max_length=224)),
                ('answer', models.CharField(max_length=224)),
                ('klik', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=224)),
                ('sub', models.TextField()),
                ('icon', models.FileField(blank=True, upload_to='landing')),
                ('logo', models.FileField(blank=True, upload_to='landing')),
                ('foto', models.FileField(blank=True, upload_to='landing')),
                ('fotoadv', models.FileField(blank=True, upload_to='landing')),
                ('alamat', models.CharField(blank=True, max_length=224)),
                ('telp', models.CharField(blank=True, max_length=13)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('ig', models.CharField(blank=True, max_length=224)),
                ('fb', models.CharField(blank=True, max_length=224)),
                ('tiktok', models.CharField(blank=True, max_length=224)),
                ('youtube', models.CharField(blank=True, max_length=224)),
                ('komisi_teacher', models.IntegerField(default=70)),
                ('komisi_developer', models.IntegerField(default=7)),
                ('komisi_owner', models.IntegerField(default=23)),
            ],
        ),
    ]
