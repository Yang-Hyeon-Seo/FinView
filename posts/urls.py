from django.urls import path
from . import views
app_name='posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    # path('detail/<int:num>/', views.detail, name='detail'),
    # path('update/<int:num>/', views.update, name='update'),
    path('delete/<int:num>', views.delete, name='delete'),
]
