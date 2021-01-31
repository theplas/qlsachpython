from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static
from.views import HomeDetailView

urlpatterns = [
    # path("detail", views.post, name="detail"),
    path("", views.home, name="home"),
    path('detail/<int:pk>', HomeDetailView.as_view(), name="detail"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
