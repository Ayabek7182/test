from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from django_unchained import views
from django_unchained.views import api_root


from django.contrib import admin

from django_unchained.views import MusicSampleViewSet, SampleCategoryViewSet, OrderViewSet, SampleReviewViewSet, CartItemViewSet, VisitViewSet, UserViewSet

router = DefaultRouter()
router.register(r'music-samples', MusicSampleViewSet)
router.register(r'sample-categories', SampleCategoryViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'sample-reviews', SampleReviewViewSet)
router.register(r'cart-items', CartItemViewSet)
router.register(r'visits', VisitViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('catalog/', views.catalog, name='catalog'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('faq/', views.faq, name='faq'),
    path('terms/', views.terms, name='terms'),
    path('privacy/', views.privacy, name='privacy'),
    path('login/', views.custom_login, name='login'),
    path('track-visit/', views.track_visit, name='track_visit'),
    path('register/', views.register, name='register'),
    path('api/', include(router.urls)),  # Используем DefaultRouter для корневой точки API
    path('create_order/', views.create_order, name='create_order'),
    path('api/', api_root, name='api-root'),
]

# Добавляем обработчик медиафайлов
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
