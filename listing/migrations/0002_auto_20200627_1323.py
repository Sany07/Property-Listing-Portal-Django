# Generated by Django 3.0.7 on 2020-06-27 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='property',
            options={'verbose_name': 'Property', 'verbose_name_plural': 'Properties'},
        ),
        migrations.RemoveField(
            model_name='realtor',
            name='is_mvp',
        ),
        migrations.CreateModel(
            name='Mvp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('realtor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listing.Realtor')),
            ],
            options={
                'verbose_name': 'MVP',
                'verbose_name_plural': 'MVP',
            },
        ),
    ]
