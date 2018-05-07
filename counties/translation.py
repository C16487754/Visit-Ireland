from modeltranslation.translator import translator, TranslationOptions
from .models import County
from .models import Attraction

class CountyTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'paragraph')

translator.register(County, CountyTranslationOptions)

class AttractionTranslationOptions(TranslationOptions):
    fields = ('subject', 'paragraph1', 'paragraph2', 'title')

translator.register(Attraction, AttractionTranslationOptions)

