from django.db import models

# Create your models here.
class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class AuthorModel(TimeStampModel):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    profession = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CategoryModel(TimeStampModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class TagModel(TimeStampModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(TimeStampModel):
    title = models.CharField(max_length=100)
    body = models.TextField()
    categories = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    tags = models.ManyToManyField(TagModel)
    image = models.ImageField(upload_to='images/')
    authors = models.ForeignKey(AuthorModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Comment(TimeStampModel):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    image = models.ImageField(upload_to='images/')
    website = models.URLField()
    message = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ExtraInfo(TimeStampModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.name


class HappyClients(TimeStampModel):
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()

    def __str__(self):
        return self.name


class About(TimeStampModel):
    title = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    video = models.URLField()
    extra_info = models.ManyToManyField(ExtraInfo)
    happy_clients = models.ManyToManyField(HappyClients)

    def __str__(self):
        return self.title




