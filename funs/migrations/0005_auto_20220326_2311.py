# Generated by Django 3.0.6 on 2022-03-26 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funs', '0004_auto_20220326_2107'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='offerID',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='offer',
            name='maxOrder',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='minOrder',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='offerDescription',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='offer',
            name='offerImage',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='offerLink',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='offerPercentage',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='offerPrice',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='offerSource',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='offer',
            name='offerValidUpto',
            field=models.DateField(blank=True, null=True),
        ),
    ]
