from django.contrib import admin

from apps.library.models import (Author, Book, Cart, CartItem, Category,
                                 Coupon, FavouriteBook)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name")
    list_display_links = ("id", "full_name")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    list_display_links = ("id", "title")


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "page", "published_year", "updated_at")
    list_display_links = ("id", "title")
    search_fields = ("title",)
    list_filter = ("author", "category", "language")


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "phone", "payment_status", "payment_type", "total")
    list_display_links = ("id", "user")
    list_filter = ("payment_status", "payment_type")


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ("id", "cart", "book", "quantity", "total")
    list_display_links = ("id", "cart")


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ("id", "code", "percent", "min_amount", "expired_date")
    list_display_links = ("id", "code")


@admin.register(FavouriteBook)
class FavouriteBookAdmin(admin.ModelAdmin):
    list_display = ("id", "book", "user")
