# Generated by Django 4.2.2 on 2023-06-29 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0002_alter_adoptantes_mensaje'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adoptantes',
            name='mensaje',
            field=models.CharField(max_length=300),
        ),
    ]
