from django.conf.urls import url
from django.urls import path,include
from . import views
from django.conf.urls import handler404, handler500,handler403
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path(r'index', views.index, name='index'),
    path(r'blog',views.BlogView.as_view(), name='blog'),
    path(r'essay', views.EssayView.as_view(), name='essay'),
    path(r'about', views.about, name='about'),
    path(r'post/<id>/', views.detail, name='detail'),
    path(r'essay/<id>/', views.essay_detail, name='essay_detail'),
    path(r'archives/<year>/<month>/', views.archives, name='archives'),
    path(r'essay_archives/<year>/<month>/', views.essay_archives, name='essay_archives'),
    path(r'tag/<tag_name>/', views.tag, name='tag'),
    path(r'search/',views.search,name='search'),
    url(r'mdeditor/', include('mdeditor.urls')),
    # 在非 DEBUG 模式下 通过url的方式进行静态资源的转发与定位
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    url(r'^uploads/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # static files (images, css, javascript, etc.)

