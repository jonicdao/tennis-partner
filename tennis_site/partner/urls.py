from django.urls import path

from . import views

app_name='partner'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('detail/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('result/', views.ResultsView, name='result'),
    path('signup/', views.signup, name='signup'),

    # path('', views.index, name = 'index'),
]

# To be implemented:

    # path('', views.IndexView.as_view(), name='index'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),