# Generated by Django 3.1.4 on 2020-12-19 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0002_modelx'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelY',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mileage', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('test_content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_content_Y', to='test_app.testmodel')),
            ],
            options={
                'verbose_name_plural': 'ModelY',
                'ordering': ('-created_at',),
            },
        ),
    ]
