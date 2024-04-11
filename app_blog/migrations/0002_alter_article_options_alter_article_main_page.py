# Generated by Django 5.0.4 on 2024-04-11 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="article",
            options={
                "ordering": ["-pub_date"],
                "verbose_name": "Статя",
                "verbose_name_plural": "Cтатті",
            },
        ),
        migrations.AlterField(
            model_name="article",
            name="main_page",
            field=models.BooleanField(
                default=True,
                help_text="Показувати на головній сторінці",
                verbose_name="Головна",
            ),
        ),
    ]
