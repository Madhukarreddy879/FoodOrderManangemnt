from django.db import models

from django.dispatch import receiver
from django.db.models import Sum
from products.models import Product
from django.conf import settings

CURRENCY = settings.CURRENCY

 
class Order(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    title = models.CharField(blank=True, null=True, max_length=50)
    value = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    
    # class Meta:
    #     ordering = ['-timestamp', ]

    # def save(self, *args, **kwargs):
    #     self.value = self.order_items.all().aggregate(Sum('total_value'))['total_value__sum'] if \
    #         self.order_items.all() else 0
    #     self.value = self.value if self.value else 0
    #     super(Order, self).save(*args, **kwargs)
    #     self.table.value = self.value if self.value and self.active else 0
    #     self.table.save()

    # def tag_value(self):
    #     return f'{self.value} {CURRENCY}'

    # def tag_active(self):
    #     return 'Closed' if not self.active else 'Active'

    # def tag_timestamp(self):
    #     return self.timestamp.date()
    



class OrderItem(models.Model):
    product_related = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_related = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    value = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    qty = models.PositiveIntegerField(default=1)
    total_value = models.DecimalField(decimal_places=2, max_digits=10, default=0)

    def __str__(self):
        return f'{self.product_related.title}'

    def save(self, *args, **kwargs):
        self.value = self.product_related.value
        self.total_value = self.value * self.qty
        super(OrderItem, self).save(*args, **kwargs)
        self.order_related.save()

    def tag_value(self):
        return f'{self.value} {CURRENCY}'

    def tag_total_value(self):
        return f'{self.total_value} {CURRENCY}'

    def tag_order_related(self):
        return f'{self.order_related.__str__}'

    def tag_product_related(self):
        return f'{self.product_related.title}'

