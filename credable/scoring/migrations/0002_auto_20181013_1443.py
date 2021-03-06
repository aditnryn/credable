# Generated by Django 2.0.9 on 2018-10-13 14:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scoring', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanapplication',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loan_applications', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='vouchers',
            field=models.ManyToManyField(related_name='vouched_loan_applications', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='vouching',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vouches', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
