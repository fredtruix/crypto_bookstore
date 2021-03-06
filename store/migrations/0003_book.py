# Generated by Django 3.2.5 on 2022-02-21 08:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20220221_0011'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Book_image', models.URLField()),
                ('book_name', models.CharField(max_length=400)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('strike_price', models.IntegerField()),
                ('book_file', models.URLField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
