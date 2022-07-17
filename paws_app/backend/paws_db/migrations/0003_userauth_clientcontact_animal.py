# Generated by Django 4.0.5 on 2022-06-26 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paws_db', '0002_rescuedetail_fosterdetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAuth',
            fields=[
                ('uname', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('pw', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'user_auth',
            },
        ),
        migrations.CreateModel(
            name='ClientContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_type', models.CharField(choices=[('E', 'Email'), ('T', 'Telephone')], max_length=1)),
                ('contact', models.CharField(max_length=40)),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paws_db.client')),
            ],
            options={
                'db_table': 'client_contact',
            },
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('adm_date', models.DateField()),
                ('fost_parc', models.CharField(max_length=80)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('breed', models.CharField(choices=[('Aspin', 'Dog'), ('Puspin', 'Cat')], max_length=30)),
                ('desc', models.CharField(max_length=1000)),
                ('hist', models.CharField(max_length=1000)),
                ('init_wt', models.DecimalField(decimal_places=2, max_digits=5)),
                ('foster_det', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='paws_db.fosterdetail')),
                ('rescue_det', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='paws_db.rescuedetail')),
            ],
            options={
                'db_table': 'animal',
            },
        ),
    ]