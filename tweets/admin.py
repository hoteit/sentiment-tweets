from django.contrib import admin

# Register your models here.
from .models import SearchKeywords, TwitterText

admin.site.register(SearchKeywords)

admin.site.register(TwitterText)
