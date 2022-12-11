# Generated by Django 4.1.4 on 2022-12-11 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("watchlist_app", "0002_streamplatform_watchlist_delete_movie"),
    ]

    operations = [
        migrations.AddField(
            model_name="watchlist",
            name="platform",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="watchlist",
                to="watchlist_app.streamplatform",
            ),
            preserve_default=False,
        ),
    ]
