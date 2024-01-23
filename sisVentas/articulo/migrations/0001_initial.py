# Generated by Django 4.2.9 on 2024-01-23 23:10

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Categoria",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                (
                    "nombre",
                    models.CharField(
                        max_length=25, verbose_name="Nombre de la categoria"
                    ),
                ),
                (
                    "descripcion",
                    models.CharField(
                        max_length=50, verbose_name="Descripcion de la categoria"
                    ),
                ),
                ("condicion", models.BooleanField(default=False)),
            ],
            options={
                "verbose_name": "Categoria",
                "verbose_name_plural": "Categorias",
            },
        ),
        migrations.CreateModel(
            name="Articulo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                ("codigo", models.CharField(max_length=50, verbose_name="Codigo")),
                ("nombre", models.CharField(max_length=150, verbose_name="Nombre")),
                ("stock", models.IntegerField(verbose_name="Stock")),
                (
                    "descripcion",
                    models.TextField(
                        blank=True,
                        max_length=500,
                        null=True,
                        verbose_name="Descripcion",
                    ),
                ),
                (
                    "imagen",
                    models.ImageField(
                        blank=True, null=True, upload_to="media/articulos"
                    ),
                ),
                (
                    "estado",
                    models.PositiveSmallIntegerField(
                        choices=[
                            (1, "Error en la factura"),
                            (2, "Factura radicada"),
                            (3, "Factura sin radicar"),
                        ],
                        default=3,
                        verbose_name="Estado del articulo",
                    ),
                ),
                (
                    "categoria",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="articulo.categoria",
                        verbose_name="Categoria",
                    ),
                ),
            ],
            options={
                "verbose_name": "Articulo",
                "verbose_name_plural": "Articulos",
            },
        ),
    ]