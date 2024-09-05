from django.contrib import admin
from content_app.models import Article, Category, Comment

class CategoryAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ('name', 'description', 'created_by', 'created_at',)
    search_fields = ['name', 'description']
    ordering = ('name',)
    exclude = ()
    readonly_fields = ('created_by', 'last_updated_by', 'created_at', 'last_updated_at')
    
    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser or request.user.is_staff
    
    def has_add_permission(self, request):
        return request.user.is_superuser or request.user.is_staff
    
    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser or request.user.is_staff


class CommentInline(admin.TabularInline):
    model = Comment
    fields = ['content', 'created_by', 'created_at']
    readonly_fields = ['created_at',]
    extra = 0
    
class ArticleAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ('title', 'category', 'created_by', 'created_at',)
    search_fields = ['title', 'content']
    list_filter = ['category']
    date_hierarchy = 'created_at'
    ordering = ('-id',)
    inlines = [CommentInline]
    exclude = ()
    readonly_fields = ('created_by', 'last_updated_by', 'created_at', 'last_updated_at')
    
    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser or request.user.is_staff
    
    def has_add_permission(self, request):
        return request.user.is_superuser or request.user.is_staff
    
    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser or request.user.is_staff
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)