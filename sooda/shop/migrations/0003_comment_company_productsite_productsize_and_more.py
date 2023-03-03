# Generated by Django 4.1.5 on 2023-01-16 15:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("shop", "0002_rename_subcategory_product_category"),
    ]

    operations = [
        migrations.CreateModel(
            name="Comment",
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
                ("title", models.CharField(max_length=255, null=True, unique=True)),
                ("content", models.TextField(max_length=255, null=True, unique=True)),
                (
                    "created",
                    models.DateField(auto_now_add=True, null=True, unique=True),
                ),
                ("updated", models.DateField(auto_now=True, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Company",
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
                ("name", models.CharField(max_length=255, null=True, unique=True)),
                ("url", models.TextField(max_length=255, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="ProductSite",
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
                ("name", models.CharField(max_length=255, null=True, unique=True)),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=9, null=True, unique=True
                    ),
                ),
                ("url", models.TextField(max_length=255, null=True, unique=True)),
                (
                    "created",
                    models.DateField(auto_now_add=True, null=True, unique=True),
                ),
                ("updated", models.DateField(auto_now=True, null=True, unique=True)),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sites",
                        related_query_name="site",
                        to="shop.company",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductSize",
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
                ("name", models.CharField(max_length=255, null=True, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name="SubCategory",
        ),
        migrations.AlterModelOptions(
            name="category",
            options={},
        ),
        migrations.AlterModelOptions(
            name="product",
            options={"ordering": ["-created"]},
        ),
        migrations.AlterIndexTogether(
            name="product",
            index_together=set(),
        ),
        migrations.RemoveField(
            model_name="category",
            name="slug",
        ),
        migrations.AddField(
            model_name="product",
            name="content",
            field=models.TextField(max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="created",
            field=models.DateField(auto_now_add=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="name",
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="updated",
            field=models.DateField(auto_now=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name="productsite",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="sites",
                related_query_name="site",
                to="shop.product",
            ),
        ),
        migrations.AddField(
            model_name="productsite",
            name="productsize",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="sites",
                related_query_name="site",
                to="shop.productsize",
            ),
        ),
        migrations.AddField(
            model_name="comment",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                related_query_name="comment",
                to="shop.product",
            ),
        ),
        migrations.AddField(
            model_name="comment",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                related_query_name="comment",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.RemoveField(
            model_name="product",
            name="available",
        ),
        migrations.RemoveField(
            model_name="product",
            name="description",
        ),
        migrations.RemoveField(
            model_name="product",
            name="price",
        ),
        migrations.RemoveField(
            model_name="product",
            name="slug",
        ),
        migrations.RemoveField(
            model_name="product",
            name="stock",
        ),
        migrations.RemoveField(
            model_name="product",
            name="category",
        ),
        migrations.AddField(
            model_name="product",
            name="category",
            field=models.ManyToManyField(
                null=True, related_name="products", to="shop.category"
            ),
        ),
    ]
