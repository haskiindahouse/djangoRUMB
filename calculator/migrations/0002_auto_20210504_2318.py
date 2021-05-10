# Generated by Django 3.2 on 2021-05-04 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('x', models.FloatField(max_length=50)),
                ('y', models.FloatField(max_length=50)),
                ('z', models.FloatField(max_length=50)),
                ('longitude', models.FloatField(max_length=50)),
                ('lattitude', models.FloatField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
