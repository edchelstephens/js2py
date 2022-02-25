from django.urls import path

from conversions.views.conversion import ConversionAPIView

urlpatterns = [
    path("js-to-python/", ConversionAPIView.as_view()),
]
