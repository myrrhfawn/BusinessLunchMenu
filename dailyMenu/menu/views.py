import datetime
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .models import Menu, Order
from .serializer import MenuSerializer, RegisterSerializer, UserSerializer, ChoiceSerializer, DailyRequestSerializer


# Create your views here.

class MenuAPIView(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = (IsAuthenticated, )

class MenuV2APIView(generics.ListAPIView):
    queryset = Menu.objects.all().values()
    serializer_class = MenuSerializer
    permission_classes = (IsAuthenticated, )

class DailyAPIView(generics.ListAPIView):
    now = datetime.datetime.now()
    day = now.strftime("%a")
    queryset = Menu.objects.filter(days__contains=day).values()
    serializer_class = MenuSerializer
    #permission_classes = (IsAuthenticated, )
    if day == "Sun":
        orders = Order.objects.all()
        for order in orders:
            order.day = None
            order.save()

        print(orders[0].day)


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })

class ChoiceAPI(generics.GenericAPIView):
    serializer_class = ChoiceSerializer
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        serializer = ChoiceSerializer(data=request.data, context={"user_id": request.user.id})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "user_id": request.user.id,
            "dish_id": request.data["dish_id"]
        })

    def put(self, request, *args, **kwargs):

        try:
            instance = Order.objects.get(user_id=request.user.id)
        except:
            return Response({"error": "Object does not exists"})

        serializer = ChoiceSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})


class DailyRequestAPIView(generics.ListAPIView):
    now = datetime.datetime.now()
    day = now.strftime("%a")
    queryset = Order.objects.filter(day__contains=day)
    serializer_class = DailyRequestSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)
