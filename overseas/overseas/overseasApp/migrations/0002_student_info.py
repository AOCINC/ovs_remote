# Generated by Django 4.0.3 on 2022-04-20 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('overseasApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='student_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('Email', models.CharField(max_length=255)),
                ('Phone', models.CharField(max_length=12)),
                ('Location', models.CharField(max_length=255)),
                ('Country_Looking_For', models.CharField(max_length=255)),
                ('Ielts_score', models.CharField(max_length=255)),
                ('Which_Degree_Pursue', models.CharField(max_length=255)),
                ('Planning_Apply_In', models.DateField(default='')),
                ('Whats_highest_Education', models.CharField(max_length=255)),
                ('Expected_Or_Gained_Percentage', models.CharField(max_length=20)),
                ('Year_Of_Gruduation', models.CharField(max_length=12)),
                ('Status_Of_IELTS_TOEFL_Exam', models.CharField(max_length=25)),
            ],
        ),
    ]