# Generated by Django 3.0.7 on 2020-07-15 15:58

from django.db import migrations
import yamlfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('scanEngine', '0006_auto_20200707_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='enginetype',
            name='yaml_configuration',
            field=yamlfield.fields.YAMLField(default=''),
        ),
    ]