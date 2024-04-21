from django.shortcuts import render

# Create view for frontend
def index(request, *args, **kwargs):
    return render(request, 'frontend/index.html')