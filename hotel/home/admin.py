from django.contrib import admin
from home.models import Amenities , Hotel ,HotelImages ,HotelBooking , Coupon


# Register your models here.

admin.site.register(Amenities)
admin.site.register(Hotel)
admin.site.register(HotelImages)
admin.site.register(HotelBooking)
admin.site.register(Coupon)
