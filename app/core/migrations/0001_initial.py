# Generated by Django 3.1.7 on 2021-04-02 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('tax_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='core.person')),
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            bases=('core.person',),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.person')),
                ('passport_num', models.CharField(max_length=10)),
            ],
            bases=('core.person',),
        ),
    ]