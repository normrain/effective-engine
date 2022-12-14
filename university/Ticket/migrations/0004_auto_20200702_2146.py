# Generated by Django 3.0.7 on 2020-07-02 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ticket', '0003_auto_20200630_2356'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='activityID',
            new_name='activity_id',
        ),
        migrations.RenameField(
            model_name='ticket',
            old_name='TicketID',
            new_name='ticket_id',
        ),
        migrations.AddField(
            model_name='activity',
            name='message',
            field=models.TextField(default='Enter text here'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='content',
            field=models.TextField(default='Enter text here'),
        ),
    ]
