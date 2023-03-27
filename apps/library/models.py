import datetime

from django.db import models
from django.utils.crypto import get_random_string
from django.utils.translation import gettext as _
from phonenumber_field.modelfields import PhoneNumberField

from apps.common.models import TimeStampedModel
from apps.library.choices import (LanguageType, LevelType, PaymentStatus,
                                  PaymentType)
from apps.users.models import CustomUser


class Author(TimeStampedModel):
    full_name = models.CharField(verbose_name=_("Full name"), max_length=255)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"


class Category(TimeStampedModel):
    title = models.CharField(verbose_name=_("Title"), max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


class Book(TimeStampedModel):
    author = models.ForeignKey(Author, verbose_name=_("Author"), on_delete=models.CASCADE)
    title = models.CharField(verbose_name=_("Title"), max_length=255)
    page = models.PositiveIntegerField(verbose_name=_("Page"), default=0)
    published_year = models.PositiveIntegerField(verbose_name=_("Published year"), default=2022)
    description = models.TextField(verbose_name=_("Description"))
    image = models.ImageField(verbose_name=_("Book image"), upload_to="image/%Y/%m/%d/")
    price = models.DecimalField(verbose_name=_("Price"), max_digits=10, decimal_places=2)
    discount = models.DecimalField(
        verbose_name=_("Discount price"), max_digits=10, decimal_places=2, null=True, blank=True, default=0
    )
    rate = models.DecimalField(verbose_name=_("Rate"), max_digits=2, decimal_places=1, default=0)
    category = models.ForeignKey(Category, verbose_name="Category", on_delete=models.CASCADE)
    language = models.CharField(
        verbose_name=_("Language"), max_length=25, choices=LanguageType.choices, default=LanguageType.UZ
    )
    level = models.CharField(
        verbose_name=_("Level"), max_length=25, choices=LevelType.choices, default=LevelType.ELEMENTARY
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Book")
        verbose_name_plural = _("Books")


def date_plus_30():
    today = datetime.datetime.now()
    exp_date = today + datetime.timedelta(days=30)
    return exp_date


class Coupon(TimeStampedModel):
    code = models.CharField(verbose_name=_("Code"), max_length=9, null=True, blank=True)
    percent = models.PositiveIntegerField(verbose_name=_("Percent"), default=0)
    min_amount = models.DecimalField(verbose_name=_("Minimal amount"), max_digits=10, decimal_places=2)
    expired_date = models.DateTimeField(verbose_name=_("Expired date"), null=True, blank=True)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = _("Coupon")
        verbose_name_plural = _("Coupons")

    def save(self, *args, **kwargs):
        if self.code is None:
            self.code = get_random_string(length=9, allowed_chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
        if self.expired_date is None:
            self.expired_date = date_plus_30()
        super(Coupon, self).save(*args, **kwargs)


class Cart(TimeStampedModel):
    user = models.ForeignKey(CustomUser, verbose_name=_("user"), on_delete=models.CASCADE)
    full_name = models.CharField(verbose_name=_("Full name"), max_length=255, null=True, blank=True)
    phone = PhoneNumberField(region="UZ", verbose_name=_("Phone number"), null=True, blank=True)
    email = models.EmailField(verbose_name=_("Email address"), null=True, blank=True)
    payment_status = models.CharField(
        verbose_name=_("Payment status"), max_length=25, choices=PaymentStatus.choices, default=PaymentStatus.PENDING
    )
    payment_type = models.CharField(
        verbose_name=_("Payment Type"), max_length=25, choices=PaymentType.choices, default=PaymentType.CLICK
    )
    coupon = models.ForeignKey(Coupon, on_delete=models.SET_NULL, verbose_name=_("Coupon"), null=True, blank=True)
    order_id = models.CharField(verbose_name=_("Order id"), max_length=11, null=True, blank=True)

    @property
    def total(self):
        return sum([cart_item.total for cart_item in self.cartitem_set.all()])

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = _("Cart")
        verbose_name_plural = _("Carts")


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, verbose_name="Cart", on_delete=models.CASCADE)
    book = models.ForeignKey(Book, verbose_name="Book", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name=_("Quantity"), default=1)
    total = models.DecimalField(verbose_name=_("Total"), default=0, max_digits=12, decimal_places=2)

    def save(self, *args, **kwargs):
        if self.book.discount > 0:
            self.total = self.book.discount * self.quantity
        self.total = self.book.price * self.quantity

        super(CartItem, self).save(*args, **kwargs)

    def __str__(self):
        return self.book.title

    class Meta:
        verbose_name = _("Cart Item")
        verbose_name_plural = _("Cart Items")


class Favourite(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name=_("User"), on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = _("Favourite")
        verbose_name_plural = _("Favourites")


class FavouriteItem(models.Model):
    favourite = models.ForeignKey(Favourite, verbose_name="Favourite", on_delete=models.CASCADE)
    book = models.ForeignKey(Book, verbose_name="Book", on_delete=models.CASCADE)

    def __str__(self):
        return self.book.title

    class Meta:
        verbose_name = _("Favourite Item")
        verbose_name_plural = _("Favourite Items")
