from django.urls import path
from . import views
app_name='posts'
urlpatterns = [
    path('', views.index, name='index'),
<<<<<<< HEAD
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    # path('detail/<int:num>/', views.detail, name='detail'),
    # path('update/<int:num>/', views.update, name='update'),
    path('delete/<int:num>', views.delete, name='delete'),
=======
    path('<int:article_pk>/', views.detail, name='detail'),
    path('<int:article_pk>/update', views.update, name='update'),
>>>>>>> 3e87dcebe2deb1e1163e7e78db64c9d6f527caed
]
