# Generated by Django 3.0.6 on 2022-03-26 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.CharField(max_length=20)),
                ('card_name', models.CharField(max_length=20)),
                ('card_expiry', models.CharField(max_length=20)),
                ('card_cvv', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CardType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank', models.CharField(max_length=20)),
                ('card_type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='OfferCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='OfferDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minOrder', models.IntegerField(null=True)),
                ('maxOrder', models.IntegerField(null=True)),
                ('offerPercentage', models.IntegerField(null=True)),
                ('offerValidUpto', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offerTitle', models.CharField(max_length=20)),
                ('offerSource', models.CharField(max_length=20)),
                ('offerDescription', models.CharField(max_length=20)),
                ('offerImage', models.CharField(max_length=20)),
                ('offerLink', models.CharField(max_length=100)),
                ('offerPrice', models.FloatField()),
                ('offerCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='funs.OfferCategory')),
                ('offerDetails', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='funs.OfferDetails')),
                ('onCard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='funs.Card')),
            ],
        ),
        migrations.AddField(
            model_name='card',
            name='card_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='funs.CardType'),
        ),
        migrations.AddField(
            model_name='card',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='funs.Users'),
        ),
    ]
