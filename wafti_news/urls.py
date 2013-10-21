from django.conf.urls import patterns, include, url
from news_rhino import views
from rest_framework import routers


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
router = routers.DefaultRouter()
router.register(r'news', views.ArticleViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wafti_news.views.home', name='home'),
    # url(r'^wafti_news/', include('wafti_news.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include(
            'rest_framework.urls', namespace='rest_framework'))
)
