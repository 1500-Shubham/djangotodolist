from django.shortcuts import render, redirect

from .models import list
from .forms import listforms

#django messaging system
from django.contrib import messages

#for delete redirectign thing
from django.http import HttpResponseRedirect


def home(request): #objects lake database se

	if request.method == 'POST':
		form= listforms(request.POST or None)

		if form.is_valid():
			form.save()
			all_items=list.objects.all #querying database
			messages.success(request, ('Item added'))
			return render(request,'home.html',{'all_items':all_items}) #dictionart pass valjue to html page

	else:

		all_items=list.objects.all #querying database
		return render(request,'home.html',{'all_items':all_items}) #dictionart pass valjue to html page



    

def about(request):
	my_name="Shubham" #view se html pass karoge
	number="Keshari"

	context={'name':my_name,'number':number}
	return render(request,'about.html',context)

def delete(request, list_id):
	item= list.objects.get(pk=list_id)
	item.delete() #with uniques id leke
	messages.success(request, ('Item deleted'))
	return redirect('home')

def cross_off(request, list_id):
	item= list.objects.get(pk=list_id)
	item.completed= True #with uniques id leke
	#item.item="Whatever"
	item.save()
	return redirect('home')

def uncross(request, list_id):
	item= list.objects.get(pk=list_id)
	item.completed= False #with uniques id leke
	item.save()
	return redirect('home')