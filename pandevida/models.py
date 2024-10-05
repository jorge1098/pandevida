from django.db import models
from django.utils.text import slugify
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=250, unique=True, blank=True) 
    description = models.TextField(blank=True, null=True) 
    def save(self, *args, **kwargs):
            if not self.slug:
                base_slug = slugify(self.name)
                slug = base_slug
                num = 1
                while Category.objects.filter(slug=slug).exists():
                    slug = f"{base_slug}-{num}"
                    num += 1
                self.slug = slug
            super().save(*args, **kwargs)

    def _str_(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, 
                                related_name='products',
                                on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,
                            unique=True) 
    image = models.ImageField(upload_to='products/%Y/%m/%d', 
                            blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, 
                                decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        
        
        ]

    def __str__(self):
        return self.name
    