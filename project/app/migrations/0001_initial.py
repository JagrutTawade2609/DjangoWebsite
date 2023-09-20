# Generated by Django 4.2.5 on 2023-09-18 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=101)),
                ('useraddress', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='fooditem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foodname', models.CharField(max_length=300)),
                ('picture', models.ImageField(upload_to='')),
                ('foodprice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('foodtype', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.DecimalField(decimal_places=2, max_digits=3)),
                ('foodid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.fooditem')),
                ('reviewername', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.customer')),
            ],
        ),
    ]
