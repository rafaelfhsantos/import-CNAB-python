from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from cnab.models import Cnab
from cnab.serializers import CnabSerializer
from .forms import UploadFileForm

# Imaginary function to handle an uploaded file.
from .utils import handle_uploaded_file

from datetime import date

def home(request):
    return render(request, 'home.html')
        

def handle_file(request):    
        form = UploadFileForm(request.POST, request.FILES)

        for line in request.FILES['filename'].readlines():
            transaction_type = line[0:1].decode() 

            transaction_date = line[1:9].decode()
            date_year = int(transaction_date[0:4]) 
            date_month = int(transaction_date[4:6])
            date_day = int(transaction_date[6:8])
            transaction_date = date(date_year, date_month, date_day)

            transaction_value = float(line[9:19].decode())/100 
            transaction_cpf = line[19:30].decode() 
            transaction_card = line[30:42].decode() 
            transaction_hour = line[42:48].decode() 
            transaction_shop_owner = line[48:62].decode() 
            transaction_shop_name = line[62:81].decode()

            cnab_data ={
                'transaction_type': transaction_type,
                'transaction_date': transaction_date,
                'transaction_value': transaction_value,
                'transaction_cpf': transaction_cpf,
                'transaction_card': transaction_card,
                'transaction_hour': transaction_hour,
                'transaction_shop_owner': transaction_shop_owner,
                'transaction_shop_name': transaction_shop_name
            }   

            print(cnab_data)

            serializer = CnabSerializer(data=cnab_data)
            serializer.is_valid(raise_exception=True)
            serializer.save()    

        return HttpResponse("Dados importados com sucesso!")


  