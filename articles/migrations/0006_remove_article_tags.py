# Generated by Django 4.2.1 on 2023-07-04 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_alter_scope_options_alter_scope_is_main'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='tags',
        ),
    ]
