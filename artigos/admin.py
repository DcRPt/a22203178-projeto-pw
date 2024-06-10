from django.contrib import admin
from django.utils.html import format_html
from .models import Author, Article, Comment, Rating

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author_name', 'created_at', 'content_preview')
    list_filter = ('created_at', 'author')
    search_fields = ('title', 'content', 'author__name')

    def author_name(self, obj):
        return obj.author.name
    author_name.short_description = 'Author'

    def content_preview(self, obj):
        return obj.content[:75] + "..." if len(obj.content) > 75 else obj.content
    content_preview.short_description = 'Content Preview'

class CommentAdmin(admin.ModelAdmin):
    list_display = ('comenter_name', 'article_title', 'created_at', 'content_preview')
    list_filter = ('created_at', 'comenter_name', 'article__title')
    search_fields = ('comenter_name', 'content', 'article__title')

    def article_title(self, obj):
        return obj.article.title
    article_title.short_description = 'Article'

    def content_preview(self, obj):
        return obj.content[:50] + "..." if len(obj.content) > 50 else obj.content
    content_preview.short_description = 'Content Preview'

class RatingAdmin(admin.ModelAdmin):
    list_display = ('article_title', 'rating_value', 'created_at')
    list_filter = ('rating_value', 'created_at', 'article__title')
    search_fields = ('rating_value', 'article__title')

    def article_title(self, obj):
        return obj.article.title
    article_title.short_description = 'Article'

admin.site.register(Author, AuthorAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Rating, RatingAdmin)
