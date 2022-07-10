# Generated by Django 4.0.5 on 2022-07-10 21:09

from django.db import migrations, models
import django.db.models.deletion
import home.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('url', models.URLField(verbose_name='URL')),
                ('icon', models.FileField(help_text='Only SVG files. The image will be used to show links on home page', upload_to='images/links/', validators=[home.models.validate_svg_file])),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('image', models.ImageField(upload_to='images/posts/')),
                ('comment', models.TextField(max_length=256)),
                ('creation_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='LinkOnPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('url', models.URLField(verbose_name='URL')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.post')),
            ],
        ),
    ]
