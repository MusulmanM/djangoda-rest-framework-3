from django.urls import path
from .views import Salom1listCreateapiview, Salom2listCreateapiview, Salom3listCreateapiview, Salom4listCreateapiview, Salom5listCreateapiview


urlpatterns = [
    path('1/', Salom1listCreateapiview.as_view(), name='salom-1'),
    path('2/', Salom2listCreateapiview.as_view(), name='salom-2'),
    path('3/', Salom3listCreateapiview.as_view(), name='salom-3'),
    path('4/', Salom4listCreateapiview.as_view(), name='salom-4'),
    path('5/', Salom5listCreateapiview.as_view(), name='salom-5'),
]