# Generated by Django 4.2.3 on 2023-07-26 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('info', models.CharField(default='', max_length=100)),
                ('price', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
