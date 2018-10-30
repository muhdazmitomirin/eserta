from django.shortcuts import render, redirect, get_object_or_404
from .models import Aktiviti
from .forms import AktivitiForm
from django.urls import reverse_lazy


# Create your views here.

# Home penganjur
def home(request):

	#aktivitiid = request.GET['aktivitiid']
	#print(request.GET['aktivitid'])
	a = Aktiviti.objects.all()
	# for ak in a:
	# 	print(ak.tajuk,ak.tempat,ak.penceramah)

	return render(request,'penganjur/home.html',{'aktiviti' : a})

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

	# user dah submit form / POST
	if request.method == "POST":
		form = AktivitiForm(request.POST)

		if form.is_valid():
			#simpan dalam memori
			aktiviti = form.save(commit=False)
			#update database
			aktiviti.save()
			return redirect(reverse_lazy('home_penganjur'))
	else:
		form = AktivitiForm()
		print(form)

	return render(request,'penganjur/tambahaktiviti.html', {'form': form})

	# hapus aktiviti guna form
def delete_aktiviti(request,pk):

	aktiviti = get_object_or_404(Aktiviti,pk=pk)

	if request.method == "POST":

		if request.POST.get("submit_yes"):

			aktiviti.delete()
			return redirect(reverse_lazy('home_penganjur'))

	return render(request,
		'penganjur/confirm_delete_aktiviti.html',
		{'aktiviti' : aktiviti })

def editaktiviti(request,pk):

	aktiviti = get_object_or_404(Aktiviti,pk=pk)
	if request.method == "POST":
		form = AktivitiForm(request.POST,instance=aktiviti)

		if form.is_valid():
			aktiviti = form.save(commit=False)
			aktiviti.save()
			return redirect(reverse_lazy('home_penganjur'))
	else:
		form = AktivitiForm(instance=aktiviti)

	return render(request,'penganjur/editaktiviti.html', {'form': form})