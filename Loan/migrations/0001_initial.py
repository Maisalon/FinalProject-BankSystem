# Generated by Django 5.1.2 on 2024-10-27 14:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('BankAccount', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('granted_at', models.DateTimeField(auto_now_add=True)),
                ('repaid', models.BooleanField(default=False)),
                ('amount_paid', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('bank_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BankAccount.bankaccount')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
