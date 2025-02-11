from django.db import models

# 1. Media model
class Media(models.Model):
    url = models.URLField()
    type = models.CharField(max_length=50)
    uploaded_at = models.DateTimeField(auto_now_add=True)

# 2. Region model
class Region(models.Model):
    name = models.CharField(max_length=255)
    media = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True, blank=True)

# 3. District model
class District(models.Model):
    name = models.CharField(max_length=255)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    media = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True, blank=True)

# 4. Category model
class Category(models.Model):
    name = models.CharField(max_length=255)
    media = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True, blank=True)

# 5. Feature model
class Feature(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    media = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True, blank=True)

# 6. Level model
class Level(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    media = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True, blank=True)

# 7. Role model
class Role(models.Model):
    name = models.CharField(max_length=255)
    staff = models.BooleanField(default=False)

# 8. Service model
class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    media = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True, blank=True)

# 9. User model
class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# 10. Contact model
class Contact(models.Model):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    website = models.URLField(null=True, blank=True)
    social_links_1 = models.URLField(null=True, blank=True)
    social_links_2 = models.URLField(null=True, blank=True)
    social_links_3 = models.URLField(null=True, blank=True)

# 11. Partner model
class Partner(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    coin = models.IntegerField(default=0)
    star = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

# 12. Badge model
class Badge(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    media = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True, blank=True)

# 13. Business Hour model
class BusinessHour(models.Model):
    day_of_week = models.IntegerField()
    open_time = models.TimeField()
    close_time = models.TimeField()
    effective_from = models.DateField()
    effective_to = models.DateField(null=True, blank=True)
    active = models.BooleanField(default=True)
    sort = models.IntegerField()

# 14. Product model
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

# 15. Coin Transaction Type model
class CoinTransactionType(models.Model):
    rules_direction = models.CharField(max_length=255)

# 16. Partner-Badge relationship
class PartnerBadge(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)
    effective_from = models.DateField()
    effective_to = models.DateField(null=True, blank=True)

# 17. Partner-BusinessHour relationship
class PartnerBusinessHour(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    business_hour = models.ForeignKey(BusinessHour, on_delete=models.CASCADE)

# 18. Partner-Feature relationship
class PartnerFeature(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    updated_on = models.DateTimeField(auto_now=True)

# 19. Partner-Media relationship
class PartnerMedia(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    uploaded_on = models.DateTimeField(auto_now_add=True)

# 20. Partner-Service relationship
class PartnerService(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

# 21. Partner-Product relationship
class PartnerProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    effective_from = models.DateField()
    effective_to = models.DateField(null=True, blank=True)
    active = models.BooleanField(default=True)

# 22. Review model
class Review(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    content = models.TextField()
    coins_earned = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

# 23. Coin Transaction model
class CoinTransaction(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    coin_transaction_type = models.ForeignKey(CoinTransactionType, on_delete=models.CASCADE)
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
