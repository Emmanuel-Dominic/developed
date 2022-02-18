from rest_framework import generics
from .models import Company
from .serializers import CompanySerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class CreateCompanyAPIView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    # lookup_field = ('name')

    # def get_queryset(self):
    #     return Company.objects.all()

    # def perform_create(self, serializer):
    #     return serializer.data
        
    # def list(self, request):
    #     companies = self.get_queryset()
    #     serializer = CompanySerializer(companies, many=True)
    #     return Response(data=serializer.data, content_type="application/json", status=status.HTTP_200_OK)


    def create(self, request, *args, **kwargs):
        data = request.data
        posted = {"name": data['name'], "bio": data['bio'], "active": data['active']}
        serializer = CompanySerializer(data=posted)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"message": "successfully created!"}, content_type="application/json", status=status.HTTP_201_CREATED)
        return Response(data={"error": "Record not created!"}, content_type="application/json", status=status.HTTP_400_BAD_REQUEST)

        # if serializer.is_valid(): 
        #     serializer.save()
        #     return Response(data={"message": "successfully created!"}, content_type="application/json", status=status.HTTP_201_CREATED)
        # else:
        #     return Response(data={"error": "Record not created!"}, content_type="application/json", status=status.HTTP_400_BAD_REQUEST)
