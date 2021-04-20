from django.contrib import admin
from .models import post, Purchaseinq, Token
# Register your models here.

admin.site.register(post)
admin.site.register(Purchaseinq)
admin.site.register(Token)