# Generated by Django 3.1.1 on 2021-01-31 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='urls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='top_words',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=100)),
                ('frequency', models.PositiveIntegerField()),
                ('url', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.urls')),
            ],
        ),
    ]
