# Generated by Django 3.2.3 on 2021-07-06 15:17

import django.db.models.deletion
import django.utils.timezone
import versatileimagefield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0004_auto_20210706_1138"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="image",
            options={
                "ordering": ["is_feature"],
                "verbose_name": "Versatile Image",
                "verbose_name_plural": "Versatile Images",
            },
        ),
        migrations.RemoveField(
            model_name="product",
            name="image_vers",
        ),
        migrations.AddField(
            model_name="image",
            name="alt_text",
            field=models.CharField(
                blank=True,
                help_text="Please add alternative text",
                max_length=255,
                null=True,
                verbose_name="Alternative text",
            ),
        ),
        migrations.AddField(
            model_name="image",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now, verbose_name="Created at"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="image",
            name="is_feature",
            field=models.BooleanField(
                default=False, help_text="Assign this as the feature image", verbose_name="Feature Image"
            ),
        ),
        migrations.AddField(
            model_name="image",
            name="product",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="product_images",
                to="store.product",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="image",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="Updated at"),
        ),
        migrations.AlterField(
            model_name="image",
            name="image",
            field=versatileimagefield.fields.VersatileImageField(
                blank=True,
                default="images/default.png",
                help_text="Upload a versatile product image",
                null=True,
                upload_to="images/",
                verbose_name="Image",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="image",
            field=versatileimagefield.fields.VersatileImageField(
                blank=True,
                default="images/default.png",
                help_text="Upload a product image",
                null=True,
                upload_to="images/",
                verbose_name="Main Image",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="thumbnail",
            field=versatileimagefield.fields.VersatileImageField(
                blank=True,
                help_text="Upload a thumbnail image",
                null=True,
                upload_to="images/",
                verbose_name="Thumbnail image",
            ),
        ),
    ]