# Generated by Django 5.1.4 on 2024-12-20 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JSONData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('data', models.JSONField()),
            ],
        ),
        migrations.DeleteModel(
            name='ChatLog',
        ),
    ]