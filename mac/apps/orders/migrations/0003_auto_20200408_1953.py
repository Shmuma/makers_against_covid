# Generated by Django 3.0.5 on 2020-04-08 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20200408_1646'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticketupdate',
            name='target_ticket',
        ),
        migrations.AlterField(
            model_name='ticketupdate',
            name='type',
            field=models.TextField(choices=[('comment', 'Комментарий'), ('is_produced', 'Партия произведена'), ('is_delivered', 'Партия доставлена')], default=('comment', 'Комментарий'), verbose_name='Тип обновления'),
        ),
    ]