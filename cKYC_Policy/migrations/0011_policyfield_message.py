# Generated by Django 2.2.1 on 2019-08-20 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cKYC_Policy', '0010_policyfield_pattern'),
    ]

    operations = [
        migrations.AddField(
            model_name='policyfield',
            name='message',
            field=models.CharField(default=2, max_length=256),
            preserve_default=False,
        ),
    ]
