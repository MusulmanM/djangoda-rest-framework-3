from rest_framework.viewsets import ModelViewSet
from .serializer import Salom1serializer, Salom2serializer, Salom3serializer, Salom4serializer, Salom5serializer
from .models import Salom1, Salom2, Salom3, Salom4, Salom5
# Create your views here.


class Salom1vset(ModelViewSet):
    serializer_class = Salom1serializer
    queryset = Salom1.objects.all()





class Salom2vset(ModelViewSet):
    serializer_class = Salom2serializer
    queryset = Salom2.objects.all()






class Salom3vset(ModelViewSet):
    serializer_class = Salom3serializer
    queryset = Salom3.objects.all()





class Salom4vset(ModelViewSet):
    serializer_class = Salom4serializer
    queryset = Salom4.objects.all()





class Salom5vset(ModelViewSet):
    serializer_class = Salom5serializer
    queryset = Salom5.objects.all()

