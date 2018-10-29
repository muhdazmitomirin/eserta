from django.shortcuts import render
from .models import Aktiviti
from .forms import AktivitiForm


# Create your views here.

# Home penganjur
def home(request):

	#aktivitiid = request.GET['aktivitiid']
	print(request.GET['aktivitid'])
	a = Aktiviti.objects.all()
	for ak in a:
		print(ak.tajuk,ak.tempat,ak.penceramah)

	return render(request,'penganjur/home.html')

# update aktiviti
def update_aktiviti(request,pk):

	aktiviti = get_object_or_404(Aktiviti,pk)
	aktiviti = Aktiviti(tajuk='Not Cheddar Update', 
		tempat='Anyplaces Update', 
		penceramah='Anybody Update',
		hadpeserta=20
		)
	akt.save()

	return render(request,'penganjur/home.html')

# Add penganjur
def add_penganjur(request):

	# tambah data setiap kali request
	akt = Aktiviti(tajuk='Not Cheddar', 
		tempat='Anyplaces', 
		penceramah='Anybody',
		hadpeserta=55
		)
	akt.save()

	return render(request,'penganjur/home.html')

# Delete penganjur
def delete_penganjur(request,pk):

	aktiviti = get_object_or_404(Aktiviti,pk)
	aktiviti.delete()

	return render(request,'penganjur/home.html')



# Tambah aktiviti
def addaktiviti(request):

	if request.method == "POST":
		pass
	else:
		form = AktivitiForm()
	return render(request,'penganjur/tambahaktiviti.html', {'form': form})