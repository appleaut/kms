from django.db import models
from django_currentuser.db.models import CurrentUserField

class Category(models.Model):
    name = models.CharField('ชื่อหมวดหมู่', max_length=100)
    description = models.TextField('รายละเอียด', null=True, blank=True)
    created_by = CurrentUserField(related_name='category_created_by')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    last_updated_by = CurrentUserField(on_update=True, related_name='category_updated_by')
    last_updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    class Meta:
        verbose_name_plural = '     หมวดหมู่'
        verbose_name = 'หมวดหมู่'
        ordering = ('name',)

    def __str__(self):
        return self.name
    

class Article(models.Model):
    title = models.CharField('หัวเรื่อง', max_length=250)
    content = models.TextField('เนื้อหา')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_by = CurrentUserField(related_name='article_created_by')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    last_updated_by = CurrentUserField(on_update=True, related_name='article_updated_by')
    last_updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    class Meta:
        verbose_name_plural = '    บทความ'
        verbose_name = 'บทความ'
        ordering = ('-id',)

    def __str__(self):
        return self.title
    
    
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField('เนื้อหา')
    created_by = CurrentUserField(related_name='comment_created_by')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    last_updated_by = CurrentUserField(on_update=True, related_name='comment_updated_by')
    last_updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    class Meta:
        verbose_name_plural = '   ความคิดเห็น'
        verbose_name = 'ความคิดเห็น'
        ordering = ('id',)

    def __str__(self):
        return '%s-%s' % (self.article.id, self.id)