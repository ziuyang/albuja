"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

import accounts.views
import blog.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),

    path('',blog.views.home,name="home"),
    path('search/', blog.views.search, name='search'),

    path('qnaList',blog.views.qnaListView, name="qnaList"), #옮기면서 ''를 qnaList로 바꿨음
    path('questions/<int:questions_id>', blog.views.qnaDetailView, name="qnaDetail"),
    path('questions/new', blog.views.qnaNewView, name="qnaNew"),
    path('questions/create', blog.views.qnaCreateView, name="qnaCreateFn"),
    path('questions/<int:questions_id>/update', blog.views.qnaUpdateView, name="qnaUpdate"),
    path('questions/<int:questions_id>/delete', blog.views.qnaDeleteView, name="qnaDelete"),

    ## blog review url
    path('review/posts/', blog.views.reviewPosts, name='reviewPosts'),
    path('review/create/', blog.views.reviewCreate, name='reviewCreate'),
    path('review/detail/<int:post_id>/', blog.views.reviewDetail, name='reviewDetail'),
    path('review/update/<int:pk>/', blog.views.reviewUpdate, name='reviewUpdate'),
    path('review/delete/<int:pk>/', blog.views.reviewDelete, name='reviewDelete'),

    path('allauth/', include('allauth.urls')),
    path('mypage', blog.views.mypage, name="mypage"), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
