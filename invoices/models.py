from django.conf import settings
from django.db import models
from products.models import Product

class Invoice(models.Model):
    customer = models.CharField(max_length=150)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name="invoices")
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    total = models.DecimalField(max_digits=14, decimal_places=2, editable=False)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.total = self.quantity * self.price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Invoice #{self.pk}"
