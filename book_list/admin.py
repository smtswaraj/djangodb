from django.contrib import admin
from .models import Book,Author
class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ('slug',)
    prepopulated_fields = {'slug':('title',)}
    # pass

# Register your models here.
admin.site.register(Book,BookAdmin)
admin.site.register(Author)
