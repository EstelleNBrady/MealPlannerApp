# Generated by Django 4.2.1 on 2023-12-01 04:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0007_pantryitem_carbohydrate_pantryitem_cholesterol_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pantryitem',
            name='sodium',
        ),
    ]
