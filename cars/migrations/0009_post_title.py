# Generated by Django 5.0.4 on 2024-04-14 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0008_alter_post_year_of_issue'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]