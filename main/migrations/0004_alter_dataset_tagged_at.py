# Generated by Django 4.2 on 2023-05-18 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_dataset_verifier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='tagged_at',
            field=models.DateTimeField(verbose_name='Tagged At'),
        ),
    ]