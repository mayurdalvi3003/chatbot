from django.urls import path
from . import views

urlpatterns = [
    path('chatbot/', views.chatbot_view, name='chatbot'),  # Your original chatbot API
    path('chatbot-page/', views.chatbot_page, name='chatbot_page'),  # New route for chatbot page
]
