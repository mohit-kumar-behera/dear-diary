from django.shortcuts import render, redirect
from . models import Entry
from .forms import EntryForm

def index(request):
	#entries = Entry.objects.all()# order in the way they were created i.e. first created one is at top
	entries = Entry.objects.order_by("-date_posted") #order date wise and time wise
	content = {'entries':entries}
	return render(request,'diaryEntry/homepage.html',content)

def add(request):
	if request.POST:
		form = EntryForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("home")
	else:
		form = EntryForm()

	context = {'form':form}
	return render(request,'diaryEntry/addpage.html',context)
