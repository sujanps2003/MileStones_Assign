from django.db import models

class DistributionCenter(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()

class Product(models.Model):
    cost = models.FloatField()
    category = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=100)
    retail_price = models.FloatField()
    department = models.CharField(max_length=100)
    sku = models.CharField(max_length=100)
    distribution_center = models.ForeignKey(DistributionCenter, on_delete=models.CASCADE)

class InventoryItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    sold_at = models.DateTimeField(null=True, blank=True)
    cost = models.FloatField()
    product_category = models.CharField(max_length=100)
    product_name = models.CharField(max_length=255)
    product_brand = models.CharField(max_length=100)
    product_retail_price = models.FloatField()
    product_department = models.CharField(max_length=100)
    product_sku = models.CharField(max_length=100)
    product_distribution_center = models.ForeignKey(DistributionCenter, on_delete=models.CASCADE)

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    state = models.CharField(max_length=100)
    street_address = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    traffic_source = models.CharField(max_length=100)
    created_at = models.DateTimeField()

class Order(models.Model):
    order_id = models.IntegerField(unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    created_at = models.DateTimeField()
    returned_at = models.DateTimeField(null=True, blank=True)
    shipped_at = models.DateTimeField(null=True, blank=True)
    delivered_at = models.DateTimeField(null=True, blank=True)
    num_of_item = models.IntegerField()

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    inventory_item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    shipped_at = models.DateTimeField(null=True, blank=True)
    delivered_at = models.DateTimeField(null=True, blank=True)
    returned_at = models.DateTimeField(null=True, blank=True)


class ChatUser(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)

class Conversation(models.Model):
    user = models.ForeignKey(ChatUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    sender = models.CharField(max_length=10)  # 'user' or 'ai'
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']  # chronological order
