# Generated by Django 3.1.1 on 2021-03-02 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sgfi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='email',
            field=models.CharField(default='sgfi.correos@gmail.com', max_length=254),
            preserve_default=False,
        ),
    ]
