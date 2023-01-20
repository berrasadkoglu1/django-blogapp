# Generated by Django 4.1.2 on 2023-01-09 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_blog_category_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='category_id',
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.category'),
        ),
    ]
