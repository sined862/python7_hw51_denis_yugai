from django.shortcuts import render
from cat.cat_db import CatDb


def stats_view(request):
    context = CatDb.stats
    if request.POST.get("action"):
        CatDb.actions(request.POST.get("action"))
        CatDb.get_img(CatDb.stats.get('happiness'))
    return render(request, 'cat_stats.html', context=context)