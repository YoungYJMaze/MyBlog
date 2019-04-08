from ..models import Post,Category,Essay,Tag
from django import template
from comments.models import Comment,Essay_Comment
from django.db.models.aggregates import Count
import random

register = template.Library()

@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-views')[:num]

@register.simple_tag
def get_recent_essays(num=5):
    return Essay.objects.all().order_by('-views')[:num]

@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')

@register.simple_tag
def essay_archives():
    return Essay.objects.dates('created_time', 'month', order='DESC')

@register.simple_tag
def get_recent_comments(num=5):
    return Comment.objects.all().order_by('-created_time')[:num]

@register.simple_tag
def get_recent_essays_comments(num=5):
    return Essay_Comment.objects.all().order_by('-created_time')[:num]

@register.simple_tag
def get_categories():
    # 别忘了在顶部引入 Category 类
    return Category.objects.all()

@register.simple_tag
def get_categories():
    # 记得在顶部引入 count 函数
    # Count 计算分类下的文章数，其接受的参数为需要计数的模型的名称
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)

@register.simple_tag()
def get_time_essay_archive():
    pass

@register.simple_tag()
def get_tags():
    return Tag.objects.all()

# 统计每个tags下文章数目的函数标签
@register.simple_tag()
def get_tags_times(tag):
    return Post.objects.filter(tags__name=tag.name).distinct().count()+Essay.objects.filter(tags__name=tag.name).distinct().count()

@register.simple_tag()
def randomcolor():
    colorArr = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    color = ""
    for i in range(6):
        color += colorArr[random.randint(0,14)]
    return "#"+color

@register.simple_tag()
def randomsize():
    fontArr = ['0.9rem','1.2rem','3.0rem','1.4rem','1.8rem','2.0rem','2.2rem','1.6rem','3.2rem','1.3rem','1.9rem','2.8rem','2.6rem','2.1rem','2.4rem']
    return fontArr[random.randint(0,14)]

