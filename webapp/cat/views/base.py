from django.shortcuts import render
from cat.cat_db import CatDb
from django.shortcuts import redirect 


def index_view(request):
    cats = CatDb.stats
    if request.POST.get("name"):
        CatDb.edit(request.POST.get("name"))
        return redirect('/cat_stats/')
    return render(request, 'index.html', context=cats)