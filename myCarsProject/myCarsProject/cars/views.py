from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse

def index(request):
    # Если есть динамические данные, передавайте их через контекст.
    return render(request, 'cars/index.html')

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

def car_detail(request, car_id):
    # Предположим, что ID больше 10 – ошибка.
    if car_id > 10:
        raise Http404("Машина с таким ID не найдена")
    return HttpResponse(f"<h1>Информация о машине</h1><p>ID: {car_id}</p>")

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
