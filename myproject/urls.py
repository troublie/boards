"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from boards import views
from django.conf.urls import url
from django.contrib import admin
from accounts import \
    views as accounts_views  # o "as" define um alias/apelido, pois senão o views.nome ia colidir com o views. do BOARDS.
from django.contrib.auth import views as auth_views

urlpatterns = [
    # url(r'^$', views.home, name='home'), #ANTIGA, FBV
    url(r'^$', views.BoardListView.as_view(), name='home'), #NOVA, GCBV
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^accounts/login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^signup/$', accounts_views.signup, name='signup'),  # URL do inicio da parte 3 - autenticação e login
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    # URL de logout. Pq do ()? Essa é CBV (class based)
    url(r'^boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics'),
    url(r'^boards/(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),
    url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/$', views.topic_posts, name='topic_posts'),
    url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/reply/$', views.reply_topic, name='reply_topic'),
    url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/posts/(?P<post_pk>\d+)/edit/$',
        views.PostUpdateView.as_view(), name='edit_post'),
    path('admin/', admin.site.urls),
]
