# Generated by Django 5.0.3 on 2024-03-27 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("usuario", "0002_usuario_foto"),
    ]

    operations = [
        migrations.AddField(
            model_name="usuario",
            name="tipo_usuario",
            field=models.IntegerField(
                choices=[(1, "Cliente"), (2, "Vendedor"), (3, "Gerente")], default=1, verbose_name="User Type"
            ),
        ),
    ]
