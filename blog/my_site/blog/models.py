from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class author(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email = models.EmailField(verbose_name="Email", max_length=254)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Tag(models.Model):
    caption=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.caption}"

class post(models.Model):
    title=models.CharField(max_length=50)
    excerpt=models.CharField(max_length=200)
    image_name=models.ImageField(upload_to="posts",null=True)
    date=models.DateField(auto_now=True)
    slug=models.SlugField(unique=True,db_index=True,allow_unicode=True)
    content=models.TextField(validators=[MinLengthValidator(10)])
    author=models.ForeignKey(author,on_delete=models.SET_NULL,null=True)
    tag=models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.title}"
    
class comment(models.Model):
    user_name=models.CharField(max_length=120)
    user_email=models.EmailField()
    text=models.TextField(max_length=400)
    post=models.ForeignKey(post,on_delete=models.CASCADE, related_name="comments")