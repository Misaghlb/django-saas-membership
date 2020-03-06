# Generated by Django 2.2.10 on 2020-03-05 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0006_add_slugs'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriptiontransaction',
            name='reference',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='subscriptiontransaction',
            name='reservation',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
