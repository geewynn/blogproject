# Generated by Django 2.2 on 2019-08-06 22:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='blog_article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('blog_content', models.CharField(max_length=1000)),
                ('author', models.ForeignKey(on_delete='Protect', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
