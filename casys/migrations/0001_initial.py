# Generated by Django 4.0.4 on 2022-07-07 01:36

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('contact_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_picture', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('courier', models.CharField(choices=[('jt', 'J&T Express'), ('lm', 'lala move'), ('lbc', 'LBC Hari ng Padala')], max_length=300)),
                ('gcash_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('gcash_name', models.CharField(max_length=300)),
                ('proof_of_payment', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=24, unique=True)),
                ('art_medium', models.CharField(max_length=300)),
                ('size', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=24)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_to_ship', models.DateField()),
                ('time_to_ship', models.TimeField()),
                ('order_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='casys.order')),
            ],
        ),
        migrations.CreateModel(
            name='Product_Receive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proof_received', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('feedback', models.TextField()),
                ('order_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='casys.order')),
                ('recipient_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='casys.client')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='product_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='casys.product'),
        ),
        migrations.AddField(
            model_name='order',
            name='user_information',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='casys.client'),
        ),
    ]
