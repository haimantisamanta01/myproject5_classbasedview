from django.shortcuts import render
from django.views import View
# Create your views here.
class GetInput(View):
    def get(self, request):
        return render(request, 'getinput.html')
class PostInput(View):
    def get(self, request):
        return render(request, 'postinput.html')
class Add(View):
    def get(self, request):
        x = request.GET["t1"]
        y = request.GET["t2"]
        z = int(x)+int(y)
        con_dic = {"data": z}
        return render(request, 'display.html', con_dic)
    def post(self,request):
        x = request.POST["t1"]
        y = request.POST["t2"]
        z = int(x)+int(y)
        con_dic = {"data": z}
        return render(request, 'display.html', con_dic)