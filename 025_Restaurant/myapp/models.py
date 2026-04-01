# restaurant/models.py

from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name      = models.CharField(max_length=100)
    slug      = models.SlugField(unique=True, blank=True)
    order     = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'name']
        verbose_name_plural = 'Categories'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    category       = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    name           = models.CharField(max_length=200)
    description    = models.TextField()
    price          = models.DecimalField(max_digits=8, decimal_places=2)
    original_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    image          = models.ImageField(upload_to='menu/', null=True, blank=True)
    ingredients    = models.TextField(blank=True)
    allergens      = models.TextField(blank=True)
    is_veg         = models.BooleanField(default=True)
    is_active      = models.BooleanField(default=True)
    is_featured    = models.BooleanField(default=False)
    is_popular     = models.BooleanField(default=False)
    is_special     = models.BooleanField(default=False)   # weekend special
    is_spicy       = models.BooleanField(default=False)
    is_gluten_free = models.BooleanField(default=False)
    serves         = models.CharField(max_length=20, blank=True)
    prep_time      = models.PositiveIntegerField(null=True, blank=True, help_text='Minutes')
    created_at     = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['category', 'name']

    @property
    def discount_percent(self):
        if self.original_price and self.original_price > self.price:
            return int((1 - self.price / self.original_price) * 100)
        return None

    def __str__(self):
        return self.name


class Order(models.Model):
    ORDER_TYPE_CHOICES = [
        ('delivery', 'Delivery'),
        ('pickup',   'Self Pickup'),
        ('dine',     'Dine In'),
    ]
    PAYMENT_CHOICES = [
        ('cod',  'Cash on Delivery'),
        ('upi',  'UPI / GPay / PhonePe'),
        ('card', 'Credit / Debit Card'),
    ]
    STATUS_CHOICES = [
        ('confirmed',         'Confirmed'),
        ('preparing',         'Preparing'),
        ('ready',             'Ready'),
        ('out_for_delivery',  'Out for Delivery'),
        ('delivered',         'Delivered'),
        ('cancelled',         'Cancelled'),
    ]

    first_name     = models.CharField(max_length=100)
    last_name      = models.CharField(max_length=100, blank=True)
    phone          = models.CharField(max_length=20)
    email          = models.EmailField(blank=True)
    order_type     = models.CharField(max_length=20, choices=ORDER_TYPE_CHOICES, default='delivery')
    address        = models.TextField(blank=True)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_CHOICES, default='cod')
    notes          = models.TextField(blank=True)
    items          = models.ManyToManyField(MenuItem, blank=True, related_name='orders')
    total_amount   = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status         = models.CharField(max_length=30, choices=STATUS_CHOICES, default='confirmed')
    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Order #{self.pk} — {self.first_name} {self.last_name}'


class ContactMessage(models.Model):
    SUBJECT_CHOICES = [
        ('reservation', 'Table Reservation'),
        ('catering',    'Catering Enquiry'),
        ('feedback',    'Feedback'),
        ('complaint',   'Complaint'),
        ('other',       'Other'),
    ]
    first_name       = models.CharField(max_length=100)
    last_name        = models.CharField(max_length=100, blank=True)
    email            = models.EmailField()
    phone            = models.CharField(max_length=20, blank=True)
    subject          = models.CharField(max_length=20, choices=SUBJECT_CHOICES, default='other')
    message          = models.TextField()
    reservation_date = models.DateField(null=True, blank=True)
    reservation_time = models.CharField(max_length=20, blank=True)
    guests           = models.CharField(max_length=20, blank=True)
    is_read          = models.BooleanField(default=False)
    created_at       = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.get_subject_display()} from {self.first_name} — {self.email}'


class Review(models.Model):
    name         = models.CharField(max_length=100)
    location     = models.CharField(max_length=100, blank=True)
    rating       = models.PositiveSmallIntegerField(default=5)
    text         = models.TextField()
    is_published = models.BooleanField(default=True)
    created_at   = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} — {self.rating}★'


class TeamMember(models.Model):
    name      = models.CharField(max_length=100)
    role      = models.CharField(max_length=100)
    bio       = models.TextField()
    photo     = models.ImageField(upload_to='team/', null=True, blank=True)
    order     = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.name
