from modeltranslation.translator import translator, TranslationOptions

from .models import Course, Chapter, VideoLesson


class CourseTranslationOptions(TranslationOptions):
    fields = ('title',)


translator.register(Course, CourseTranslationOptions)


class ChapterTranslationOptions(TranslationOptions):
    fields = ('title',)


translator.register(Chapter, ChapterTranslationOptions)


class VideoLessonTranslationOptions(TranslationOptions):
    fields = ('title', 'body_text')


translator.register(VideoLesson, VideoLessonTranslationOptions)


class CourseTranslationOptions(TranslationOptions):
    fields = ('title',)


translator.register(Course, CourseTranslationOptions)
