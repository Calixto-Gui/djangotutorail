# Generated by Django 4.2.2 on 2023-06-16 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_name',
            field=models.CharField(default='Bob', max_length=50),
            preserve_default=False,
        ),
    ]
