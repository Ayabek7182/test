# models.py

from django.db import models
from django.contrib.auth.models import User


class MusicSample(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    audio_file = models.FileField(upload_to='audio/')
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    genre = models.CharField(max_length=100, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    users_wishlist = models.ManyToManyField(User, related_name='wishlist', blank=True)

    def __str__(self):
        return self.title


class SampleCategory(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category_images/', blank=True, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    shipping_address = models.TextField(blank=True)

    def __str__(self):
        return f"Order #{self.id} - {self.user.username}"


class SampleReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sample = models.ForeignKey(MusicSample, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"Review by {self.user.username} for {self.sample.title}"


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sample = models.ForeignKey(MusicSample, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"CartItem - {self.sample.title} ({self.quantity})"


class Visit(models.Model):
    ip_address = models.CharField(max_length=100)
    visit_time = models.DateTimeField(auto_now_add=True)
