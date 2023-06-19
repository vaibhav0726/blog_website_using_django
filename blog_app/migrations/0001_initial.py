# Generated by Django 4.2.2 on 2023-06-18 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CreateBlog',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('metaTitle', models.CharField(max_length=1000)),
                ('slug', models.CharField(max_length=255)),
                ('metaDescription', models.CharField(max_length=1000)),
                ('body', models.TextField()),
                ('image', models.TextField()),
            ],
        ),
    ]
