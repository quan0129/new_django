from django.shortcuts import render
from django.http import HttpResponse
from .utils import autolike
from .models import FacebookUser
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import AccountSerializer
from rest_framework.response import Response
# Create your views here.


def index_view(request):
    """
        đây là chỗ để
        tính tổng

        """
    if request.method == 'GET':
        # hiển thị giao diện
        users = FacebookUser.objects.all()
        context = {
            'users': users
        }
        return render(request, 'index.html', context)

    if request.method == 'POST':
        # chạy vào đây tính tổng
        so1 = request.POST['so1']
        so2 = request.POST['so2']

        so3 = int(so1) + int(so2)

        context = {
            'ketqua': so3
        }
        return render(request, 'index.html', context)


def auto_like(request):
    autolike()
    return HttpResponse("da like")


def tinhtong(request):
    # day la cho de tinh tong
    """
    đây là chỗ để
    tính tổng

    """
    if request.method == 'GET':
        # hiển thị giao diện

        return render(request, 'index.html')

    if request.method == 'POST':
        # chạy vào đây tính tổng
        so1 = request.POST['so1']
        so2 = request.POST['so2']

        so3 = int(so1) + int(so2)

        context = {
            'ketqua': so3
        }
        return render(request, 'index.html', context)


class FacebookAccountView(APIView):
    permission_class = [AllowAny]
    
    def get(self,request,facebook_id):
        fuser = FacebookUser.objects.get(facebook_id=facebook_id)
        serial = AccountSerializer(fuser)
        print(serial)
        return Response(data=serial.data)
    
    def post(self,request,facebook_id):
        return Response('post thanh cong')

        
    