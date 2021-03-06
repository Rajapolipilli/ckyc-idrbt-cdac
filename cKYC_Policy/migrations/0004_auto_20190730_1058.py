# Generated by Django 2.2.1 on 2019-07-30 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cKYC_Policy', '0003_auto_20190730_0628'),
    ]

    operations = [
        migrations.CreateModel(
            name='PolicyField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_name', models.CharField(max_length=100)),
                ('field_type', models.CharField(choices=[('primary', 'primary'), ('mandetory', 'mandetory'), ('optional', 'optional')], max_length=60)),
                ('field_datatype', models.CharField(choices=[('BigIntegerField', 'BigIntegerField'), ('BinaryField', 'BinaryField'), ('BooleanField', 'BooleanField'), ('CharField', 'CharField'), ('DateField', 'DateField'), ('DateTimeField', 'DateTimeField'), ('DecimalField', 'DecimalField'), ('DurationField', 'DurationField'), ('ImageField', 'ImageField'), ('EmailField', 'EmailField'), ('FileField', 'FileField'), ('FloatField', 'FloatField'), ('IntegerField', 'IntegerField'), ('PositiveIntegerField', 'PositiveIntegerField'), ('SlugField', 'SlugField'), ('TextField', 'TextField'), ('TimeField', 'TimeField'), ('URLField', 'URLField'), ('UUIDField', 'UUIDField')], max_length=60)),
                ('proof_doc', models.CharField(choices=[('Drving liecense', 'Drving liecense'), ('Aadhar', 'Aadhar'), ('SSC Certificate', 'SSC Certificate'), ('Passport', 'Passport'), ('PAN card', 'PAN card'), ('Any Govt. Issued Proof', 'Any Govt. Issued Proof')], max_length=60)),
            ],
        ),
        migrations.DeleteModel(
            name='PolicyFields',
        ),
        migrations.AddField(
            model_name='policy',
            name='policyfield',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='cKYC_Policy.PolicyField'),
            preserve_default=False,
        ),
    ]
