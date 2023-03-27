from django.urls import path

from apps.library.api_endpoints.BookDetail.views import BookDetailApiView
from apps.library.api_endpoints.BookList.views import BookListApiView
from apps.library.api_endpoints.CartCreate.views import CartCreateApiView
from apps.library.api_endpoints.CartDetail.views import CartDetailApiView
from apps.library.api_endpoints.CartItemCreate.views import \
    CartItemCreateApiView
from apps.library.api_endpoints.CartItemUpdate.views import \
    CartItemUpdateApiView
from apps.library.api_endpoints.CartUpdate.views import CartUpdateView
from apps.library.api_endpoints.CouponRegistration.views import \
    CouponRegistrationView
from apps.library.api_endpoints.OrderCreate.views import OrderCreateApiView

urlpatterns = [
    path("books/", BookListApiView.as_view(), name="book-lists"),
    path("books/detail/<int:pk>", BookDetailApiView.as_view(), name="book-detail"),
    path("cart/create/", CartCreateApiView.as_view(), name="cart-create"),
    path("cartitem/create/", CartItemCreateApiView.as_view(), name="cartitem-create"),
    path("cartitem/update/<int:pk>", CartItemUpdateApiView.as_view(), name="cartitem-update"),
    path("cart/detail/<int:pk>", CartDetailApiView.as_view(), name="cart-detail"),
    path("cart/update/<int:pk>", CartUpdateView.as_view(), name="cart-update"),
    path("coupon/registration/", CouponRegistrationView.as_view(), name="coupon-registration"),
    path("order/create/", OrderCreateApiView.as_view(), name="oreder-create"),
]
