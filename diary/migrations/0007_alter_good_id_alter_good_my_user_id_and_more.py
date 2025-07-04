# Generated by Django 5.2.3 on 2025-06-22 10:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0006_good_my_user_id_good_page_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='good',
            name='my_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='diary.myuser'),
        ),
        migrations.AlterField(
            model_name='good',
            name='page_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='diary.page'),
        ),
    ]
