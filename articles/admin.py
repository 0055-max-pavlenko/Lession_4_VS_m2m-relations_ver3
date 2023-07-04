from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Tag

class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        checked = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main') is True:
                checked += 1
        if checked > 1:
            raise ValidationError('Основным может быть один раздел')
            
        elif checked == 0:
            raise ValidationError('Укажите основной раздел')
            

class ScopeInline(admin.TabularInline):
    model = Scope
    formset = RelationshipInlineFormset
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at', 'image']
    inlines = [ScopeInline,]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    