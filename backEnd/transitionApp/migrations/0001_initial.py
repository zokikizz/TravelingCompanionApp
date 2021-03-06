# Generated by Django 3.2.4 on 2021-06-13 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('travelApp', '0001_initial'),
        ('destinationApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('transit_type', models.CharField(choices=[('train', 'TRAIN'), ('bus', 'BUS'), ('plane', 'PLANE'), ('ship', 'SHIP')], default='train', max_length=10)),
                ('start', models.DateTimeField(null=True)),
                ('end', models.DateTimeField(null=True)),
                ('end_destination', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='end_location', to='destinationApp.destination')),
                ('start_destination', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='start_location', to='destinationApp.destination')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='belongs_to', to='travelApp.trip')),
            ],
        ),
    ]
