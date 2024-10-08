# Generated by Django 5.1 on 2024-08-30 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Titre')),
                ('sumary', models.CharField(max_length=60, null=True, verbose_name='Sommaire')),
                ('content', models.TextField(max_length=100, verbose_name='Contenue')),
                ('image', models.ImageField(upload_to='images', verbose_name='Images')),
                ('date_pub', models.DateField(null=True, verbose_name='Date de publication')),
            ],
        ),
    ]
