# Generated by Django 2.2.1 on 2019-08-26 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cKYC_Policy', '0013_auto_20190826_1118'),
    ]

    operations = [
        migrations.RenameField(
            model_name='policyfield',
            old_name='field_datatype',
            new_name='datatype',
        ),
        migrations.RenameField(
            model_name='policyfield',
            old_name='field_type',
            new_name='meta',
        ),
        migrations.RenameField(
            model_name='policyfield',
            old_name='field_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='policyfield',
            old_name='proof_doc',
            new_name='proof',
        ),
    ]
