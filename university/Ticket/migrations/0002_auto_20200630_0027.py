# Generated by Django 3.0.7 on 2020-06-29 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ticket', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='closeDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
