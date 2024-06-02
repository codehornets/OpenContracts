# Generated by Django 3.2.9 on 2024-06-02 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('corpuses', '0002_initial'),
        ('extracts', '0003_auto_20240602_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extract',
            name='corpus',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='extracts', to='corpuses.corpus'),
        ),
    ]
