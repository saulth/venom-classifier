# Generated by Django 4.0.4 on 2022-05-03 08:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sequences',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence', models.TextField(max_length=600)),
                ('prediction', models.CharField(max_length=1)),
                ('probnotvenom', models.FloatField(default=0.0)),
                ('probvenom', models.FloatField(default=0.0)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('consultant', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]