from .models import MusicSample, SampleCategory, Order, SampleReview
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import CustomAuthenticationForm

def index(request):
    data = {"header": "Hello Django", "message": "Welcome to Python"}
    return render(request, "index.html", context=data)

def catalog(request):
    sample_categories = SampleCategory.objects.all()
    category_id = request.GET.get('category')

    music_samples = MusicSample.objects.all()
    if category_id:
        music_samples = music_samples.filter(samplecategory_id=category_id)
        category_filter = int(category_id)
    else:
        category_filter = None

    orders = Order.objects.all()
    sample_reviews = SampleReview.objects.all()
    context = {
        'music_samples': music_samples,
        'sample_categories': sample_categories,
        'orders': orders,
        'sample_reviews': sample_reviews,
        'category_filter': category_filter,  # Передаем переменную category_filter в контекст
    }
    return render(request, 'catalog.html', context)

def contact(request):
    return render(request, "contact.html", {"page_title": "Контакты"})

def about(request):
    return render(request, "about.html", {"page_title": "О нас"})

def faq(request):
    return render(request, 'faq.html')

def terms(request):
    return render(request, 'terms.html')

def privacy(request):
    return render(request, 'privacy.html')

def custom_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Перенаправление на главную страницу после успешного входа
            else:
                form.add_error(None, "Invalid username or password.")
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request.POST)  # Используем вашу форму аутентификации
        if form.is_valid():
            form.save()
            return redirect('login')  # Перенаправление на страницу входа после успешной регистрации
    else:
        form = CustomAuthenticationForm()  # Используем вашу форму аутентификации
    return render(request, 'register.html', {'form': form})
from django.http import JsonResponse
from .models import Visit

def track_visit(request):
    if request.method == 'POST' and request.POST.get('visit') == 'true':
        # Получаем IP-адрес пользователя
        ip_address = request.META.get('REMOTE_ADDR', None)

        # Сохраняем информацию о посещении в базе данных
        visit = Visit(ip_address=ip_address)
        visit.save()

        # Возвращаем ответ в формате JSON
        return JsonResponse({'message': 'Visit tracked successfully'})
    else:
        # Если запрос не POST или нет параметра "visit", возвращаем ошибку
        return JsonResponse({'error': 'Invalid request'}, status=400)


# views.py
from django.contrib.auth.models import User
from rest_framework import viewsets
from .models import MusicSample, SampleCategory, Order, SampleReview, CartItem, Visit
from .serializers import MusicSampleSerializer, SampleCategorySerializer, OrderSerializer, SampleReviewSerializer, CartItemSerializer, VisitSerializer, UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MusicSampleViewSet(viewsets.ModelViewSet):
    queryset = MusicSample.objects.all()
    serializer_class = MusicSampleSerializer


class SampleCategoryViewSet(viewsets.ModelViewSet):
    queryset = SampleCategory.objects.all()
    serializer_class = SampleCategorySerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class SampleReviewViewSet(viewsets.ModelViewSet):
    queryset = SampleReview.objects.all()
    serializer_class = SampleReviewSerializer


class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class VisitViewSet(viewsets.ModelViewSet):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer

def create_order(request):
        return render(request, 'create_order.html')

from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer

class OrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    """
    Корневая точка API, предоставляющая список доступных ресурсов.
    """

    # Определяем ссылки на доступные ресурсы
    links = {
        'music-samples': reverse('music-sample-list', request=request, format=format),
        'sample-categories': reverse('sample-category-list', request=request, format=format),
        'orders': reverse('order-list', request=request, format=format),
        'sample-reviews': reverse('sample-review-list', request=request, format=format),
        'cart-items': reverse('cart-item-list', request=request, format=format),
        'visits': reverse('visit-list', request=request, format=format),
        'users': reverse('user-list', request=request, format=format),
    }

    # Возвращаем список ресурсов в формате JSON
    return Response(links)






from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    """
    Корневая точка API, предоставляющая список доступных ресурсов.
    """

    # Определяем ссылки на доступные ресурсы
    links = {
        'music-samples': reverse('music-sample-list', request=request, format=format),
        'sample-categories': reverse('sample-category-list', request=request, format=format),
        'orders': reverse('order-list', request=request, format=format),
        'sample-reviews': reverse('sample-review-list', request=request, format=format),
        'cart-items': reverse('cart-item-list', request=request, format=format),
        'visits': reverse('visit-list', request=request, format=format),
        'users': reverse('user-list', request=request, format=format),
    }

    # Возвращаем список ресурсов в формате JSON
    return Response(links)
