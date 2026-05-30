from django.shortcuts import render

def dashboard(request):
    return render(request, 'dashboard_second/dashboard_second.html')
