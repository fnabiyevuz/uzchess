from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from sorl.thumbnail import ImageField

from apps.common.models import TimeStampedModel
from apps.course.utils import randomize_certificate_number
from apps.users.models import CustomUser

from .choices import (COMPLAINT_TYPE_CHOICES, COURSE_COMMENT_STATUS_CHOICES,
                      LANGUAGE_CODE_CHOICES, PAYMENT_STATUS_CHOICES,
                      PAYMENT_TYPE_CHOICES)


# Create your models here.
class CourseType(models.TextChoices):
    COURSE_SALE = "course_sale", _("Course sale")


class CourseCategory(TimeStampedModel):
    title_uz = models.CharField(max_length=255, verbose_name=_("Title_uz"))
    title_ru = models.CharField(max_length=255, verbose_name=_("Title_ru"))
    title_en = models.CharField(max_length=255, verbose_name=_("Title_en"))
    icon = ImageField(upload_to="categories", null=True, blank=True, verbose_name=_("Icon"))

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.title_uz


class CourseLevel(TimeStampedModel):
    title_uz = models.CharField(max_length=255, verbose_name=_("Title_uz"))
    title_ru = models.CharField(max_length=255, verbose_name=_("Title_ru"))
    title_en = models.CharField(max_length=255, verbose_name=_("Title_en"))
    icon = ImageField(upload_to="levels", null=True, blank=True, verbose_name=_("Icon"))

    class Meta:
        verbose_name = _("Level")
        verbose_name_plural = _("Levels")

    def __str__(self):
        return self.title_uz


class Course(TimeStampedModel):
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    author = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="course_author", verbose_name=_("Author")
    )
    lang_code = models.CharField(max_length=3, verbose_name=_("Language code"), choices=LANGUAGE_CODE_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Price"), blank=True, null=True)
    discounted_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name=_("Discounted price"), blank=True, null=True
    )
    discounted_expire_date = models.DateTimeField(verbose_name=_("Discounted expire date"))
    category = models.ForeignKey(
        CourseCategory, on_delete=models.CASCADE, related_name="category", verbose_name=_("Category")
    )
    level = models.ForeignKey(CourseLevel, on_delete=models.CASCADE, related_name="level", verbose_name=_("Level"))

    is_free = models.BooleanField(default=False, verbose_name=_("Is Free"))

    class Meta:
        verbose_name = _("Course")
        verbose_name_plural = _("Courses")

    def __str__(self):
        return self.title


class Chapter(TimeStampedModel):
    title = models.CharField(max_length=255, verbose_name=_("Title"))

    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="course", verbose_name=_("Course"))

    class Meta:
        verbose_name = _("Chapter")
        verbose_name_plural = _("Chapters")

    def __str__(self):
        return self.title


class VideoLesson(TimeStampedModel):
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    body_text = models.TextField(verbose_name=_("Body text"))
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name="chapter", verbose_name=_("Chapter"))
    video_path = models.FileField(upload_to="videos", verbose_name=_("Video path"))
    video_duration = models.DurationField(verbose_name=_("Video duration"), null=True, blank=True)
    video_thumbnail = models.ImageField(upload_to="thumbnails", verbose_name=_("Video thumbnail"))

    class Meta:
        verbose_name = _("Video")
        verbose_name_plural = _("Videos")

    def __str__(self):
        return self.title


class VideoUserViews(TimeStampedModel):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="user_video_views", verbose_name=_("User")
    )
    video = models.ForeignKey(
        VideoLesson, on_delete=models.CASCADE, related_name="user_video_views", verbose_name=_("Video")
    )
    last_watched_time = models.DurationField(verbose_name=_("Last Watched Time"), blank=True, null=True)
    is_finished = models.BooleanField(default=False, verbose_name=_("Is Finished"))
    progress = models.IntegerField(verbose_name=_("Progress"), blank=True, null=True)  # 0-100 foizlarda

    class Meta:
        verbose_name = _("Video user view")
        verbose_name_plural = _("Video user views")

    def __str__(self):
        return f"{self.user} - {self.video}"


class CourseComment(TimeStampedModel):
    author = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="coursecomment_author", verbose_name=_("Author")
    )
    rating = models.PositiveSmallIntegerField(
        verbose_name=_("Rating"), validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    status = models.CharField(
        max_length=50, verbose_name=_("Status"), choices=COURSE_COMMENT_STATUS_CHOICES
    )  # static choice 1= moderating, 2=approved, 3=declined, 4=complained
    comment_text = models.TextField(verbose_name=_("Comment text"))
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="comments", verbose_name=_("Course"))

    class Meta:
        verbose_name = _("Course comment")
        verbose_name_plural = _("Course comments")

    def __str__(self):
        return f"{self.author} - {self.course} - {self.rating * '⭐'}"


class CourseCommentComplaint(TimeStampedModel):
    comment = models.ForeignKey(
        CourseComment, on_delete=models.CASCADE, related_name="comment", verbose_name=_("Comment")
    )
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="coursecommentcomplaint_user", verbose_name=_("User")
    )
    complaint_type = models.CharField(
        max_length=50, verbose_name=_("Complaint type"), choices=COMPLAINT_TYPE_CHOICES, blank=True, null=True
    )  # static choice 1= spam, 2=offensive, 3=other
    complaint_text = models.TextField(verbose_name=_("Complaint text"))

    class Meta:
        verbose_name = _("Course comment complaint")
        verbose_name_plural = _("Course comment complaints")

    def __str__(self):
        return self.user.full_name


class Payment(TimeStampedModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="user_payment", verbose_name=_("User"))
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="course_payment", verbose_name=_("Course")
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Amount"))
    payment_type = models.CharField(
        max_length=50, verbose_name=_("Payment type"), choices=PAYMENT_TYPE_CHOICES
    )  # static choice 1=card, 2=click, 3=uzcard
    payment_status = models.CharField(
        max_length=50, verbose_name=_("Payment status"), choices=PAYMENT_STATUS_CHOICES
    )  # static choice 1=success, 2=failed 3=moderating
    payment_date = models.DateTimeField(verbose_name=_("Payment date"), auto_now_add=True)

    class Meta:
        verbose_name = _("Payment")
        verbose_name_plural = _("Payments")

    def __str__(self):
        return str(self.id)


class UserCourse(TimeStampedModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="user_courses", verbose_name=_("User"))
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="user_courses", verbose_name=_("Course"))
    is_finished = models.BooleanField(default=False, verbose_name=_("Is Finished"))
    finished_at = models.DateTimeField(null=True, blank=True, verbose_name=_("Finished At"))

    # order = models.OneToOneField("payment.Order", on_delete=models.CASCADE, verbose_name=_("Order"))

    def __str__(self):
        return f"{self.user} - {self.course}"

    class Meta:
        verbose_name = _("User Course")
        verbose_name_plural = _("User Courses")


class Certificate(TimeStampedModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="certificates", verbose_name=_("User"))
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="certificates", verbose_name=_("Course"))
    full_name = models.CharField(max_length=255, verbose_name=_("Full Name"), null=True)
    cid = models.CharField(max_length=255, verbose_name=_("CID"), default=randomize_certificate_number)
    file = models.FileField(upload_to="certificates", verbose_name=_("File"), null=True)
    image = models.ImageField(upload_to="certificates", verbose_name=_("Image"), null=True)

    def __str__(self):
        return f"{self.user} - {self.course} - {self.cid}"

    class Meta:
        verbose_name = _("Certificate")
        verbose_name_plural = _("Certificates")
        unique_together = ["user", "course"]


class FavouriteCourse(TimeStampedModel):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="favourite_courses", verbose_name=_("User")
    )
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="favourite_courses", verbose_name=_("Favourite Course")
    )

    def __str__(self):
        return f"{self.user} - {self.course}"

    class Meta:
        verbose_name = _("Favourite Course")
        verbose_name_plural = _("Favourite Courses")
        unique_together = ["user", "course"]
