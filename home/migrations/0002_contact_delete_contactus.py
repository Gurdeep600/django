# Generated by Django 4.0.3 on 2022-03-18 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=110)),
                ('phone', models.CharField(max_length=111)),
            ],
        ),
        migrations.DeleteModel(
            name='contactus',
        ),
    ]
