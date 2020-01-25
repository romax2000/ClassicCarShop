from django.contrib import admin
from ecomapp.models import Car
from ecomapp.models import User
from ecomapp.models import Cars
from ecomapp.models import Supplier
from ecomapp.models import Customer
from ecomapp.models import Deliveries
from ecomapp.models import Mycar
from ecomapp.models import Request
from ecomapp.models import Order
# Register your models here.
admin.site.register(Car)
admin.site.register(User)
admin.site.register(Cars)
admin.site.register(Supplier)
admin.site.register(Customer)
admin.site.register(Deliveries)
admin.site.register(Mycar)
admin.site.register(Request)
admin.site.register(Order)
