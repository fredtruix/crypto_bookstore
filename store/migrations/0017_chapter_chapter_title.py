# Generated by Django 4.0.2 on 2022-04-04 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_book_overview_alter_user_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='Chapter_title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
