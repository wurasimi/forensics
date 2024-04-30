from django.contrib import admin
from .models import item,Post,Contact

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
     
     
     
@admin.register(item)
class itemAdmin(admin.ModelAdmin):
    pass

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass