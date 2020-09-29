from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

"""
register custom 'user' model with admin
"""

admin.site.register(User, UserAdmin)
