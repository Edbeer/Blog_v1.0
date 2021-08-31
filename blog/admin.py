from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe

from .models import *


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'slug', 'category', 'created_at', 'views', 'get_photo', 'is_published')
    list_display_links = ('id', 'title', 'slug')
    list_filter = ('category', 'tags', 'is_published')
    list_editable = ('is_published',)
    fields = ('title', 'slug', 'content', 'category', 'tags', 'photo', 'get_photo', 'created_at', 'views', 'is_published')
    search_fields = ('title', 'content')
    readonly_fields = ('get_photo', 'created_at', 'views')
    save_on_top = True
    save_as = True

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')

    get_photo.short_description = 'IMG'


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)

