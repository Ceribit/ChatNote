# Generated by Django 2.0.7 on 2018-07-24 20:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20180721_2100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='notifications',
        ),
        migrations.AlterField(
            model_name='friend',
            name='target_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='notification',
            name='from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='FROM', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='notification',
            name='target_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='TO', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='friends',
            field=models.ManyToManyField(blank=True, null=True, to='accounts.Friend'),
        ),
    ]