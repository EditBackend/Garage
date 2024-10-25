from django.contrib import admin


from blog.models import Email,Cars,Category,Tag
# Register your models here.

admin.site.register(Email)
admin.site.register(Cars)
admin.site.register(Category)
admin.site.register(Tag)
