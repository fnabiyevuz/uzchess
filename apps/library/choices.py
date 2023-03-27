from django.db import models


class LanguageType(models.TextChoices):
    UZ = "uz"
    RU = "ru"
    EN = "en"


class LevelType(models.TextChoices):
    ELEMENTARY = "Boshlang'ich"
    AMATEUR = "Havaskor"
    PROFESSIONAL = "Professional"


class PaymentStatus(models.TextChoices):
    PENDING = "Pending"
    FAILED = "Failed"
    PAID = "Paid"


class PaymentType(models.TextChoices):
    PAYLOV = "Paylov"
    PAYME = "Payme"
    CLICK = "Click"
    UZUMBANK = "Uzum Bank"

class CartStatus(models.TextChoices):
    PENDING = "Pending"
    CHECKOUT = "Checkout"