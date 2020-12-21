from django.http import JsonResponse, response
from .models import TestModel,ModelX
from rest_framework.views import APIView
from django.forms.models import model_to_dict
from .serializers import SimpleSerializer

# Basic
'''
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt 
def simple(request):
    method = request.method.lower()

    if method == 'get':
        return JsonResponse({"data":[1,3,4,4,5]})
    elif method == 'post':
        return JsonResponse({"data":"Added Data successfully"})
    elif method == 'put':
        return JsonResponse({"data":"Updated Data successfully"})        

    return JsonResponse({"error":"method not allowed"})
'''
# APIView Basic 

'''
class simple(APIView):

    def post(self,request):
        new_test_content = TestModel.objects.create(
            name = request.data["name"],
            description = request.data["description"],
            phone_number = request.data["phone_number"],
            is_alive = request.data["is_alive"],
            amount = request.data["amount"]
        )
        return JsonResponse({"data":model_to_dict(new_test_content)})

    def get(self,request):
        content = TestModel.objects.all().values()
        return JsonResponse({"data":list(content)})
'''

'''class Simple(APIView):

    def post(self,request):
        new_test_content = TestModel.objects.create(
            name = request.data["name"],
            description = request.data["description"],
            phone_number = request.data["phone_number"],
            is_alive = request.data["is_alive"],
            amount = request.data["amount"]
        )
        return JsonResponse({"data":model_to_dict(new_test_content)})

    def get(self,request):
        content = TestModel.objects.all().values()
        return JsonResponse({"data":list(content)})'''

'''class Simple(APIView):

    def post(self,request):
        serializer = SimpleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse({"data":serializer.data})

    def get(self,request):
        content = TestModel.objects.all().values()
        return JsonResponse({"data":SimpleSerializer(content,many=True).data})

    def put(self,request,*args,**kwargs):
        model_id = kwargs.get("id",None)
        if not model_id:
            return JsonResponse({"error":"method /PUT/ not allowed"})
        try:
            instance = TestModel.objects.get(id=model_id)
        except:
            return JsonResponse({"error":"Object does not exist"})

        serializer = SimpleSerializer(data=request.data,instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse({"data":serializer.data})'''
        
                 

