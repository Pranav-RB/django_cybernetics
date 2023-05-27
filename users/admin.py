from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from .models import User
from .forms import UserRegisterForm, UserUpdateForm

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserAdmin(BaseUserAdmin):
    form = UserUpdateForm
    add_form = UserRegisterForm
    model = User
    add_fieldsets = (
        (None, {'fields': ('email', 'first_name', 'last_name','password1','password2','events_list','college','phone_number')}),
    )
    fieldsets = (
        (None, {
            "fields": (
                ('email', 'first_name', 'last_name','password','events_list','college','phone_number')
                
            ),
        }),
    )
    ordering = ('email',)
admin.site.register(User, UserAdmin)
