from django.contrib import admin
from .models import *

admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Orders)
admin.site.register(OrderItem)
