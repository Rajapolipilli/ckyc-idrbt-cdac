# Generated by Django 2.2.1 on 2019-08-07 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cKYC_Policy', '0007_auto_20190731_0958'),
    ]

    operations = [
        migrations.AddField(
            model_name='policy',
            name='policy_conditions',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]