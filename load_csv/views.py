from django.db.utils import IntegrityError
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from account.models import Account
import csv

# Create your views here.
def index(request, *args, **kwargs):
    return render(request, 'load_csv/index.html')

# Parse CSV file into models
def load_csv(request):
    try:
        if request.method == 'POST' and request.FILES['file']:
            csv_file = request.FILES['file']
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)
            
            for row in reader:
                Account.objects.create(
                    client_id = row['client reference no'],
                    balance = float(row['balance']),
                    status = row['status'].upper(),
                    consumer_name = row['consumer name'].lower(),
                    address = row['consumer address'],
                    ssn = row['ssn'],
                )
            
            return HttpResponse('<h1>CSV upload succeed!</h1>')
    except:
            return HttpResponse('<h1>No file uploaded or invalid request method</h1>')

# NOTE: Create a column for agency id if modeling many agency and many clients