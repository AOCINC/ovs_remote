# Generated by Django 4.0.3 on 2022-04-21 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('overseasApp', '0004_alter_student_info_planning_apply_in_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Order_No', models.CharField(max_length=10)),
                ('Student_name', models.CharField(max_length=255)),
                ('Address', models.CharField(max_length=255)),
                ('Phone', models.CharField(max_length=12)),
                ('Email', models.CharField(max_length=255)),
                ('Date', models.CharField(max_length=35)),
                ('Description', models.CharField(max_length=255)),
                ('Total_Payment', models.CharField(max_length=45)),
                ('Advance_Payment', models.CharField(max_length=45)),
                ('Due_Payment', models.CharField(max_length=45)),
            ],
        ),
    ]
