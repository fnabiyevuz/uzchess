from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

<<<<<<< HEAD
from apps.library.api_endpoints.book.BookList.serializers import \
=======
from apps.course.api_endpoints.course.CourseList.serializers import \
    CourseListSerializer
from apps.course.models import Course
from apps.library.api_endpoints.BookList.serializers import \
>>>>>>> eda245dc7df37f23f1318282038e4889cb81b6bb
    BookSerializer as BookListSerializer
from apps.library.models import Book


class GetFavouriteBooksAPIView(ListAPIView):
    serializer_class = BookListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Get Books queryset liked by request user
        """
        favourite_books = Book.objects.filter(favourite_books__user=self.request.user)

        return favourite_books


<<<<<<< HEAD
__all__ = ["GetFavouriteBooksAPIView"]
=======
class GetFavouriteCoursesAPIView(ListAPIView):
    serializer_class = CourseListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Get Books queryset liked by request user
        """
        favourite_courses = Course.objects.filter(favourite_courses__user=self.request.user)

        return favourite_courses


__all__ = ["GetFavouriteBooksAPIView", "GetFavouriteCoursesAPIView"]
>>>>>>> eda245dc7df37f23f1318282038e4889cb81b6bb
