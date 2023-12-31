# Generated by Django 4.2.3 on 2023-08-09 22:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_version', models.IntegerField(verbose_name='номер версии')),
                ('name_version', models.CharField(max_length=150, verbose_name='название версии')),
                ('is_active_version', models.BooleanField(blank=True, default=False, null=True, verbose_name='признак версии')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='version', to='catalog.product', verbose_name='продукт')),
            ],
            options={
                'verbose_name': 'Версия',
                'verbose_name_plural': 'Версии',
                'ordering': ('number_version',),
            },
        ),
    ]
