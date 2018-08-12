from django.shortcuts import render
from . models import Tabooksite
# Create your views here.

def index_view(request):
    tabook_list=Tabooksite.objects.all()
    context={
        'tabook_list':tabook_list
    }
    if request.method == "POST":
        posted_title=request.POST.get('title','')
        posted_description=request.POST.get('description','')

        tabook_new=Tabooksite.objects.create(
            title=posted_title,
            description=posted_description
        )
        tabook_new.save() #to save to database, because create not saving to database
        return render(request, 'tabook_app/index.html',context)
    return render(request, 'tabook_app/index.html',context)

def artlst_view(request):
     tabook_list=Tabooksite.objects.all()
    context={
        'tabook_list':tabook_list
    }
    return render(request, 'tabook_app/lst.html',context)