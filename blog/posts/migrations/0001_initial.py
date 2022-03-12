# Generated by Django 4.0.3 on 2022-03-12 11:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='posts.basemodel')),
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_title', models.CharField(max_length=100)),
                ('category_slug', models.SlugField(blank=True, max_length=250, null=True)),
            ],
            bases=('posts.basemodel',),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='posts.basemodel')),
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('meta_title', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, max_length=250, null=True)),
                ('text', models.TextField()),
                ('published_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-published_at',),
            },
            bases=('posts.basemodel',),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='posts.basemodel')),
                ('tag_id', models.AutoField(primary_key=True, serialize=False)),
                ('tag_title', models.CharField(max_length=100)),
                ('tag_content', models.CharField(max_length=200)),
            ],
            bases=('posts.basemodel',),
        ),
        migrations.CreateModel(
            name='PostTag',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='posts.basemodel')),
                ('post', models.ManyToManyField(to='posts.post')),
                ('tags', models.ManyToManyField(to='posts.tag')),
            ],
            bases=('posts.basemodel',),
        ),
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='posts.basemodel')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.category')),
                ('post', models.ManyToManyField(to='posts.post')),
            ],
            bases=('posts.basemodel',),
        ),
    ]