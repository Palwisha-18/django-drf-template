from django.urls import include, path
from api.app1.views import home_view

urlpatterns = [
    path('home', home_view)
]
