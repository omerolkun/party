# Generated by Django 3.2.4 on 2021-08-12 23:00

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Columnist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField(default=30, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(18)])),
                ('membership', models.CharField(choices=[('member', 'member'), ('party friend', 'p friend')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('issue', models.CharField(choices=[('economy', 'eco'), ('woman', 'female'), ('culture', 'cultur'), ('union', 'unionx')], max_length=30)),
                ('article_writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dip.columnist')),
            ],
        ),
    ]
