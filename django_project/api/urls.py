from django.urls import path, include
from api.app1 import urls as app1_urls


urlpatterns = [
    path(r'app1/', include(app1_urls))
]
