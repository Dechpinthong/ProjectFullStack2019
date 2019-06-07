from django.contrib import admin
from .models import Book, Transaction, Publisher, Binding

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # list_display = ['id','name']
    list_display = [f.name for f in Book._meta.fields]

# admin.register(Category, CategoryAdmin)

# @admin.register(Borrow)
# class BorrowAdmin(admin.ModelAdmin):
#     list_display = [f.name for f in Borrow._meta.fields]

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Publisher._meta.fields]

@admin.register(Binding)
class BindingAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Binding._meta.fields]

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Transaction._meta.fields]
     # readonly_fields = [f.name for f in Transaction._meta.fields]