# Generated by Django 3.2.5 on 2021-09-15 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NGO', '0002_alter_ngo_profile_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Requirements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nid', models.IntegerField()),
                ('ename', models.CharField(max_length=100)),
                ('edescription', models.TextField()),
                ('edate', models.DateField()),
                ('ereq', models.IntegerField()),
            ],
        ),
    ]