# Generated by Django 3.2.18 on 2023-04-19 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='table',
            field=models.CharField(choices=[('Table1', 'Table1'), ('Table2', 'Table2'), ('Table3', 'Table3'), ('Table4', 'Table4'), ('Table5', 'Table5')], default=None, max_length=6),
        ),
    ]
