from django.shortcuts import render

# Create your views here.

# Home penganjur
def home(request):
	return render(request,'penganjur/home.html')