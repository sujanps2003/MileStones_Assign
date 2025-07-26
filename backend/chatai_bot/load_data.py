import pandas as pd
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chatai.settings")
django.setup()

from core.models import (
    DistributionCenter, Product, InventoryItem, OrderItem, Order, User
)

# Load and insert Distribution Centers
df = pd.read_csv('distribution_centers.csv')
for _, row in df.iterrows():
    DistributionCenter.objects.get_or_create(
        id=row['id'],
        defaults={
            'name': row['name'],
            'latitude': row['latitude'],
            'longitude': row['longitude']
        }
    )

# Load Users
df = pd.read_csv('users.csv')
for _, row in df.iterrows():
    User.objects.get_or_create(
        id=row['id'],
        defaults=dict(
            first_name=row['first_name'],
            last_name=row['last_name'],
            email=row['email'],
            age=row['age'],
            gender=row['gender'],
            state=row['state'],
            street_address=row['street_address'],
            postal_code=row['postal_code'],
            city=row['city'],
            country=row['country'],
            latitude=row['latitude'],
            longitude=row['longitude'],
            traffic_source=row['traffic_source'],
            created_at=row['created_at']
        )
    )

# Load Products
df = pd.read_csv('products.csv')
for _, row in df.iterrows():
    dc = DistributionCenter.objects.get(id=row['distribution_center_id'])
    Product.objects.get_or_create(
        id=row['id'],
        defaults=dict(
            cost=row['cost'],
            category=row['category'],
            name=row['name'],
            brand=row['brand'],
            retail_price=row['retail_price'],
            department=row['department'],
            sku=row['sku'],
            distribution_center=dc
        )
    )

# Load Inventory Items
df = pd.read_csv('inventory_items.csv')
for _, row in df.iterrows():
    dc = DistributionCenter.objects.get(id=row['product_distribution_center_id'])
    product = Product.objects.get(id=row['product_id'])
    InventoryItem.objects.get_or_create(
        id=row['id'],
        defaults=dict(
            product=product,
            created_at=row['created_at'],
            sold_at=row['sold_at'] if pd.notnull(row['sold_at']) else None,
            cost=row['cost'],
            product_category=row['product_category'],
            product_name=row['product_name'],
            product_brand=row['product_brand'],
            product_retail_price=row['product_retail_price'],
            product_department=row['product_department'],
            product_sku=row['product_sku'],
            product_distribution_center=dc
        )
    )

# Load Orders
df = pd.read_csv('orders.csv')
for _, row in df.iterrows():
    user = User.objects.get(id=row['user_id'])
    Order.objects.get_or_create(
        order_id=row['order_id'],
        defaults=dict(
            user=user,
            status=row['status'],
            gender=row['gender'],
            created_at=row['created_at'],
            returned_at=row['returned_at'] if pd.notnull(row['returned_at']) else None,
            shipped_at=row['shipped_at'] if pd.notnull(row['shipped_at']) else None,
            delivered_at=row['delivered_at'] if pd.notnull(row['delivered_at']) else None,
            num_of_item=row['num_of_item']
        )
    )

# Load Order Items
df = pd.read_csv('order_items.csv')
for _, row in df.iterrows():
    order = Order.objects.get(order_id=row['order_id'])
    user = User.objects.get(id=row['user_id'])
    product = Product.objects.get(id=row['product_id'])
    inventory = InventoryItem.objects.get(id=row['inventory_item_id'])

    OrderItem.objects.get_or_create(
        id=row['id'],
        defaults=dict(
            order=order,
            user=user,
            product=product,
            inventory_item=inventory,
            status=row['status'],
            created_at=row['created_at'],
            shipped_at=row['shipped_at'] if pd.notnull(row['shipped_at']) else None,
            delivered_at=row['delivered_at'] if pd.notnull(row['delivered_at']) else None,
            returned_at=row['returned_at'] if pd.notnull(row['returned_at']) else None,
        )
    )
