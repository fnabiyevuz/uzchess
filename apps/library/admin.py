from django.contrib import admin

from apps.library.models import (Author, Book, Cart, CartItem, Category,
                                 Coupon, FavouriteBook, Order)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name")
    list_display_links = ("id", "full_name")
    date_hierarchy = "created_at"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    list_display_links = ("id", "title")
    date_hierarchy = "created_at"


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "page", "published_year", "updated_at")
    list_display_links = ("id", "title")
    search_fields = ("title",)
    list_filter = ("author", "category", "language")
    date_hierarchy = "created_at"


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "status", "total")
    list_display_links = ("id", "user")
    list_filter = ("status",)
    date_hierarchy = "created_at"


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ("id", "cart", "book", "quantity", "total")
    list_display_links = ("id", "cart")
    date_hierarchy = "created_at"


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ("id", "code", "percent", "min_amount", "expired_date")
    list_display_links = ("id", "code")
    date_hierarchy = "created_at"


@admin.register(FavouriteBook)
class FavouriteBookAdmin(admin.ModelAdmin):
    list_display = ("id", "book", "user")
    date_hierarchy = "created_at"


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", "cart", "payment_amount", "phone", "email", "order_id")
    list_display_links = ("id", "full_name")
    list_filter = ("payment_status", "payment_type")
    search_fields = ("full_name", "phone", "email", "order_id")
    date_hierarchy = "created_at"
