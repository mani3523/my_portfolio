from django.contrib import admin
from django.urls import path
from home import views



# django admin changes
admin.site.site_header = "Login to Burhan"
admin.site.site_title = "Welocom to DashBord"
admin.site.index_title = "Welocom to Portal"



urlpatterns = [
    path('', views.home, name='home'),
    path('chatbot', views.chatbot, name='chatbot'),
    path('instagram/', views.instagram, name='instagram'),
    path('snake/', views.snake, name='snake'),
    path('todo_list/', views.todo_list, name='todo_list'),
    path('number/', views.number, name='number'),
    path('whatsapp/', views.whatsapp, name='whatsapp'),
    path('turtle/', views.turtle, name='turtle'),
    path('game/', views.game, name='game'),
    path('restaurant/', views.restaurant, name='restaurant'),
    path('#contact', views.contact, name='contact'),
]