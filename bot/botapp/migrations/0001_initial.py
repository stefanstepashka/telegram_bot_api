# Generated by Django 4.0.6 on 2022-09-18 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Words',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=100, verbose_name='Word')),
                ('gender', models.CharField(choices=[('мужской', 'Мужской'), ('женский', 'Женский'), ('Средний', 'Средний')], max_length=7, verbose_name='Gender')),
            ],
        ),
    ]
