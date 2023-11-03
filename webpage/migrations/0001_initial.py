# Generated by Django 4.2.1 on 2023-11-02 04:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('ingredient_id', models.IntegerField(primary_key=True, serialize=False)),
                ('food', models.CharField(max_length=100)),
                ('measure', models.CharField(max_length=100)),
                ('grams', models.IntegerField()),
                ('calories', models.IntegerField()),
                ('fat', models.IntegerField()),
                ('sat_fat', models.IntegerField()),
                ('fiber', models.IntegerField()),
                ('carbs', models.IntegerField()),
                ('category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MeasurementQty',
            fields=[
                ('qty_id', models.IntegerField(primary_key=True, serialize=False)),
                ('qty_desc', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MeasurementUnits',
            fields=[
                ('unit_id', models.IntegerField(primary_key=True, serialize=False)),
                ('measurement_desc', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('role_id', models.IntegerField(primary_key=True, serialize=False)),
                ('role_name', models.CharField(max_length=30)),
                ('role_desc', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=50)),
                ('user_email', models.EmailField(max_length=254)),
                ('user_pass', models.CharField(max_length=50)),
                ('role_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webpage.roles')),
            ],
        ),
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('recipe_id', models.IntegerField(primary_key=True, serialize=False)),
                ('recipe_name', models.CharField(max_length=200)),
                ('recipe_desc', models.CharField(max_length=10000)),
                ('recipe_ingredients', models.CharField(max_length=10000)),
                ('recipe_preptime', models.IntegerField()),
                ('recipe_cooktime', models.IntegerField()),
                ('recipe_peanut', models.BooleanField(default=False)),
                ('recipe_Dairy', models.BooleanField(default=False)),
                ('recipe_vegetarian', models.BooleanField(default=False)),
                ('recipe_vegan', models.BooleanField(default=False)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webpage.users')),
            ],
        ),
        migrations.CreateModel(
            name='RecipeIngredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webpage.ingredients')),
                ('qty_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webpage.measurementqty')),
                ('recipe_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webpage.recipes')),
                ('unit_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webpage.measurementunits')),
            ],
        ),
        migrations.CreateModel(
            name='PantryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=255)),
                ('item_amount', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webpage.users')),
            ],
        ),
    ]
