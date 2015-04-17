from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'minblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/login/$', 'login.views.login_user', name='login'),
    url(r'^user/logout/$', 'login.views.logout_user', name='logout'),
    url(r'^user/register/$', 'login.views.register_user', name='register'),
    url(r'^articles/all/$', 'articles.views.articles_show', name='articles'),
    url(r'^articles/create/', 'articles.views.article_create', name='article_create'),
    url(r'^articles/save/$', 'articles.views.article_save', name='article_save'),
    url(r'^articles/(\d+)/$', 'articles.views.article_show', name='article'),
    url(r'^articles/(\d+)/change/$', 'articles.views.article_change', name='article_change'),
    url(r'^articles/delete/$', 'articles.views.article_delete', name='article_delete'),
    url(r'^articles/user/(\w+)/$', 'articles.views.articles_user', name='articles_user'),
    url(r'^comments/(\d+)/$', 'comments.views.comments_show', name='comments_show'),
    url(r'^comments/save/$', 'comments.views.comment_save', name='comment_save'),
    url(r'^comments/delete/(\d+)/$', 'comments.views.comment_delete', name='comment_delete'),
    url(r'^comments/update/$', 'comments.views.comments_update', name='comments_update'),
    url(r'^$', 'articles.views.root', name='articles_root')
)

urlpatterns += staticfiles_urlpatterns()