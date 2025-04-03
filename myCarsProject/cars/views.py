from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponse
from .models import Car
from .models import Tag

def index(request):
    cars = Car.published.all()  # Получаем только опубликованные автомобили
    data = {
        'title': 'Главная страница',
        'cars': cars,
    }
    return render(request, 'cars/index.html', context=data)

def about(request):
    return render(request, 'cars/about.html')

def compare(request):
    return render(request, 'cars/compare.html')

def cars_list(request):
    # Пример данных, можно заменить на реальные или модели.
    all_cars = [
        {'id': 1, 'name': 'Toyota Camry', 'description': 'Надежный седан с высоким комфортом.'},
        {'id': 2, 'name': 'Mazda CX-5', 'description': 'Современный кроссовер с динамичным дизайном.'},
    ]
    return render(request, 'cars/cars_list.html', {'cars': all_cars})

def car_detail(request, car_slug):
    car = get_object_or_404(Car, slug=car_slug)
    data = {
        'title': car.title,
        'car': car,
    }
    return render(request, 'cars/car_detail.html', context=data)


def archive(request, year):
    if year > 2025:
        raise Http404("Нет данных за этот год")
    return HttpResponse(f"<h1>Архив за {year} год</h1>")

def redirect_example(request):
    return redirect('home')

def get_params_example(request):
    name = request.GET.get('name', 'Гость')
    return HttpResponse(f"<h1>Привет, {name}!</h1>")

def category(request, cat_id):
    return HttpResponse(f"<h1>Страница категории</h1><p>ID категории: {cat_id}</p>")
def tags_list(request):
    tags = Tag.objects.all()
    data = {
        'title': 'Теги',
        'tags': tags,
    }
    return render(request, 'cars/tags_list.html', context=data)