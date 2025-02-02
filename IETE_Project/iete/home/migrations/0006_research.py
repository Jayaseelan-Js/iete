# Generated by Django 4.0.5 on 2023-08-31 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_education'),
    ]

    operations = [
        migrations.CreateModel(
            name='Research',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('genere', models.TextField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='research_images/')),
            ],
        ),
    ]
