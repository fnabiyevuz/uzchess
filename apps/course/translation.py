from modeltranslation.translator import TranslationOptions, translator

from .models import Chapter, Course, VideoLesson, CourseCategory, CourseLevel


class CourseCategoryTranslationOptions(TranslationOptions):
    fields = ("title",)


translator.register(CourseCategory, CourseCategoryTranslationOptions)


class CourseLevelTranslationOptions(TranslationOptions):
    fields = ("title",)


translator.register(CourseLevel, CourseLevelTranslationOptions)


class CourseTranslationOptions(TranslationOptions):
    fields = ("title",)


translator.register(Course, CourseTranslationOptions)


class ChapterTranslationOptions(TranslationOptions):
    fields = ("title",)


translator.register(Chapter, ChapterTranslationOptions)


class VideoLessonTranslationOptions(TranslationOptions):
    fields = ("title", "body_text")


translator.register(VideoLesson, VideoLessonTranslationOptions)
