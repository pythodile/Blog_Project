from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Category(BaseModel):
    category_id = models.AutoField(primary_key=True)
    category_title = models.CharField(max_length=100)
    category_slug = models.SlugField(max_length = 250, null = True, blank = True)

    def __str__(self):
        return self.category_slug

class Tag(BaseModel):
    tag_id = models.AutoField(primary_key=True)
    tag_title = models.CharField(max_length=100)
    tag_content = models.CharField(max_length=200)
    
    def __str__(self):
        return self.tag_title

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
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    status = models.CharField(max_length = 10, choices = STATUS_CHOICES,default ='draft')
 
    def __str__(self):
        return self.title



