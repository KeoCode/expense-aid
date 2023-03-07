from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from datetime import datetime, date
from django.core.validators import MaxValueValidator, MinValueValidator
from django.template.defaultfilters import slugify

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True, null=False, blank=False)
    slug = models.SlugField(max_length=200, unique=True)
    date = models.DateField(("Date"), default=date.today)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="expense_post")
    udated_on = models.DateTimeField(auto_now=True)
    expense_amount = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(100000)])
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
