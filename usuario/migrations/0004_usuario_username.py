# Generated by Django 5.0.3 on 2024-04-01 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("usuario", "0003_usuario_tipo_usuario"),
    ]

    operations = [
        migrations.AddField(
            model_name="usuario",
            name="username",
            field=models.CharField(default="...", max_length=50, unique=True),
        ),
    ]
