from modeltranslation.translator import translator, TranslationOptions
from .models import Info, RulesOfUsing


class InfoTranslationOptions(TranslationOptions):
    fields = ('metro',)


translator.register(Info, InfoTranslationOptions)


class RulesOfUsingTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


translator.register(RulesOfUsing, RulesOfUsingTranslationOptions)

