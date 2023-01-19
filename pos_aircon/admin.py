from django.contrib import admin

from .models import tools_inventory
from .models import customer_details
from .models import technician_details
admin.site.register(tools_inventory)
admin.site.register(customer_details)
admin.site.register(technician_details)

# Register your models here.
