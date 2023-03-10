# Generated by Django 4.0.1 on 2022-07-31 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_delete_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order', to='accounts.customer'),
        ),
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order', to='accounts.product'),
        ),
    ]
