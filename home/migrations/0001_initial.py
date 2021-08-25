# Generated by Django 3.2.6 on 2021-08-24 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Informations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('information_name', models.CharField(max_length=100)),
                ('json_text_field', models.TextField(default='{}')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updatet_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('information', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.informations')),
            ],
        ),
    ]