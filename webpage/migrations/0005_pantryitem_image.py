# Generated by Django 4.2.1 on 2023-11-17 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0004_rename_item_amount_pantryitem_quantity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pantryitem',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='pantry_images/'),
        ),
    ]
