# Generated by Django 2.1.7 on 2019-03-28 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0025_merge_20190327_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bounty',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bounties', to='dashboard.HackathonEvent'),
        ),
    ]
