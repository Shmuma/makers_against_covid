# Generated by Django 3.0.5 on 2020-04-08 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20200408_1953'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticketupdate',
            name='target_ticket',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='updates', to='orders.Ticket'),
            preserve_default=False,
        ),
    ]