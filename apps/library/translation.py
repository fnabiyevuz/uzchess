from modeltranslation.translator import translator, TranslationOptions
from .models import Author, Category, Book


class AuthorTranslationOptions(TranslationOptions):
    fields = ('full_name',)


translator.register(Author, AuthorTranslationOptions)


class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


translator.register(Category, CategoryTranslationOptions)


class BookTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


translator.register(Book, BookTranslationOptions)
