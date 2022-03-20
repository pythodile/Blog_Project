from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Post(BaseModel):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    post_id = models.AutoField(primary_key=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    meta_title = models.CharField(max_length=50)
    slug = models.SlugField(max_length = 250, null = True, blank = True)
    text = models.TextField()
    published_at = models.DateTimeField(auto_now_add = True)
    status = models.CharField(max_length = 10, choices = STATUS_CHOICES,default ='draft')

    class Meta:
       ordering = ('-published_at', )
 
    def __str__(self):
        return self.title

class Category(BaseModel):
    category_id = models.AutoField(primary_key=True)
    category_title = models.CharField(max_length=100)
    category_slug = models.SlugField(max_length = 250, null = True, blank = True)

class Tag(BaseModel):
    tag_id = models.AutoField(primary_key=True)
    tag_title = models.CharField(max_length=100)
    tag_content = models.CharField(max_length=200)

class PostTag(BaseModel):
    post = models.ManyToManyField(Post)
    tags = models.ManyToManyField(Tag)

class PostCategory(BaseModel):
    post = models.ManyToManyField(Post)
    cat = models.ForeignKey(Category,on_delete=models.CASCADE)






