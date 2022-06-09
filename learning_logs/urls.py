"""Define URL schemes for learning_logs"""

from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Outputting all topics
    path('topics/', views.topics, name='topics'),
    # Page with info about each topic
    path('topics/<topic_id>/', views.topic, name='topic'),
    # Page for adding new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for adding new entry
    path('new entry/<topic_id>/', views.new_entry, name='new_entry'),
    # Page for editing entry
    path('edit_entry/<entry_id>/', views.edit_entry, name='edit_entry'),
]
