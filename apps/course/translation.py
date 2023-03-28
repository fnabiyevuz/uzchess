from modeltranslation.translator import TranslationOptions, translator

from .models import Chapter, Course, VideoLesson


class CourseTranslationOptions(TranslationOptions):
    fields = ("title",)


translator.register(Course, CourseTranslationOptions)


class ChapterTranslationOptions(TranslationOptions):
    fields = ("title",)


translator.register(Chapter, ChapterTranslationOptions)


class VideoLessonTranslationOptions(TranslationOptions):
    fields = ("title", "body_text")


translator.register(VideoLesson, VideoLessonTranslationOptions)


class CourseTranslationOptions(TranslationOptions):
    fields = ("title",)


translator.register(Course, CourseTranslationOptions)
