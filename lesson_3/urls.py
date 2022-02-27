from django.urls import path
from .views import *
from lesson_3.post_view import MyTemplateView, post_page

urlpatterns = [
    path('main/', main),
    path('main/text/', text, name="text"),
    path('main/file/', file, name="file"),
    path('main/redirect/', redirect, name="redirect"),
    path('main/not-allowed/', not_allowed, name="not_allowed"),
    path('main/json/', json, name="json"),

    path('class-view/', MyTemplateView.as_view(), name='class_view'),
    path('post/<int:number>/', post_page, name='detael_post'),

]
