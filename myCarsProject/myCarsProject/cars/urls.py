from django.urls import path
from . import views
from . import converters
from django.urls import register_converter

register_converter(converters.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('', views.index, name='home'),           # Главная страница
    path('about/', views.about, name='about'),      # О нас
    path('compare/', views.compare, name='compare'),
    path('cars/', views.cars_list, name='cars'),      # Список машин
    path('cars/<int:car_id>/', views.car_detail, name='car_detail'),  # Детальная страница машины
    path('archive/<year4:year>/', views.archive, name='archive'),
    path('go-home/', views.redirect_example, name='go_home'),
    path('hello/', views.get_params_example, name='hello'),
    path('category/<int:cat_id>/', views.category, name='category'),
]
