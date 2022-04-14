from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import View
from .serializers import ProductSerializer
from .models import Product
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .permissions import IsAdimOrReadOnly
# Create your views here.

from django.http import HttpResponse
class HomeView(View):
    def get(self,request):
        return render(request,'home.html')
class InsertInput(View):
    def get(self,request):
        return render(request,'productinput.html')
class InserView(View):
    def get(self,request):
        p_id=int(request.GET["t1"])
        p_name=request.GET["t2"]
        p_cost=float(request.GET["t3"])
        p_mfdt=request.GET["t4"]
        p_expdt=request.GET["t5"]
        p1=Product(pid=p_id,pname=p_name,pcost=p_cost,pmfdt=p_mfdt,pexpdt=p_expdt)
        p1.save()
        resp=HttpResponse("product inserted successfully")
        return resp

class DisplayView(View):
    def get(self,request):
        qs=Product.objects.all()
        con_dic={"records":qs}
        return render(request,"display.html",con_dic)
class DeleteInputView(View):
    def get(self,request):
        return render(request,"deleteinput.html")
class DeleteView(View):
    def get(self,request):
        P_id=int(request.GET["t1"])
        prod=Product.objects.filter(pid=P_id)
        prod.delete()
        resp = HttpResponse("product deleted successfully")
        return resp
class UpdateInputView(View):
    def get(self,request):
        return render(request,"updateinput.html")
class UpdateView(View):
    def post(self,request):
        P_id=int(request.POST["t1"])
        p_name = request.POST["t2"]
        p_cost = float(request.POST["t3"])
        p_mfdt = request.POST["t4"]
        p_expdt = request.POST["t5"]
        prod=Product.objects.get(pid=P_id)
        prod.pname=p_name
        prod.pcost=p_cost
        prod.pmfdt=p_mfdt
        prod.pexpdt=p_expdt
        prod.save()
        resp = HttpResponse("product updated successfully")
        return resp
class InputView(View):
    def get(self,request):
        return render(request,'input.html')

class ProductList(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdimOrReadOnly,)
class ProductList1(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdimOrReadOnly,)