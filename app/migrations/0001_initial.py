# Generated by Django 4.2.7 on 2023-12-01 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='This is the title bitch', max_length=250)),
                ('body', models.TextField()),
                ('category', models.TextField(blank=True, null=True)),
                ('picture', models.ImageField(upload_to='blog')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
