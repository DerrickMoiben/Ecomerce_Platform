from django.contrib import admin
from owner.models import Product, Movie


class MoveAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Movie, MoveAdmin)
admin.site.register(Product)