# Generated by Django 2.2.1 on 2019-08-26 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cKYC_Policy', '0012_auto_20190821_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='policyfield',
            name='pattern',
            field=models.CharField(choices=[('^[A-Za-z ]+$', 'only alpha'), ('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$', 'email contraint'), ('^\\d{10}$', 'phone number (10 digits)'), ('^\\d$', 'number'), ('None', 'None')], help_text='select data validations', max_length=100),
        ),
    ]