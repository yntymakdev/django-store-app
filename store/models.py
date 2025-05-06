from django.forms import models


class Category(models.Model):
    category_name = models.CharField(max_length=16,unique=True)
    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_name = models.CharField(max_length=16,unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=2, desimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    have = models.BooleanField(default=False)
    video = models.FileField(blank=True)
    def __str__(self):
        return self.product_name

