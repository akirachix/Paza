# Generated by Django 4.1.2 on 2022-10-23 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.TextField(max_length=50, null=True)),
                ('action', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=250, null=True)),
                ('sector', models.TextField(max_length=30, null=True)),
                ('time_date', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Leader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=240)),
                ('county', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=30, null=True)),
                ('neighbourhood_associattion', models.CharField(max_length=40, null=True)),
                ('username', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('neighbourhood', models.CharField(max_length=20, null=True)),
                ('date_of_meeting', models.DateTimeField(null=True)),
                ('tittle_of_meeting', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=20, null=True)),
                ('date_and_time', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.TextField(max_length=250, null=True)),
                ('description', models.TextField(max_length=250, null=True)),
                ('sector', models.TextField(max_length=30, null=True)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('video', models.FileField(null=True, upload_to='')),
                ('time_date', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Resident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=240, null=True)),
                ('username', models.CharField(max_length=30, null=True)),
                ('password', models.CharField(max_length=30, null=True)),
                ('county', models.CharField(choices=[('N', 'Nairobi'), ('M', 'Mombasa'), ('T', 'Turkana'), ('K', 'Kitale')], max_length=20, null=True)),
                ('neighbourhood_associattion', models.CharField(max_length=40, null=True)),
            ],
        ),
    ]
