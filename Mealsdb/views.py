from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from API_Meals.Get_meals import Request_meals
from django.core.paginator import Paginator
from django.urls import reverse
from django.shortcuts import redirect
# Create your views here.
meals = Request_meals()
qtde_pag = 10
def index(request):
    search_key = request.GET.get('searchfield')
    page_number = request.GET.get('page')
    if search_key:
        meals.search(search_key)
        base_url = reverse('search_view')
        url = '{}?{}'.format(base_url, 'searchfield={}'.format(search_key))
        return redirect(url)
    else:
        paginator = Paginator(meals.request, qtde_pag)
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)
        return render(request, 'index.html', {'page_obj': page_obj})


def search(request):
    search_key = request.GET.get('newsearch')
    search_key2 = request.GET.get('searchfield')

    if search_key:
        meals.search(search_key)
        base_url = reverse('search_view')
        paginator = Paginator(meals.search_list, qtde_pag)
        page_number = request.GET.get('page', 1)
        try:
            page_obj = paginator.get_page(page_number)
            url = '{}?{}'.format(base_url, 'searchfield={}'.format(search_key))
            return redirect(url)
        except TypeError:
            return render(request, 'error.html', {'mealsearch': search_key})
    else:
        if request.GET.get('page') != 1:
            paginator = Paginator(meals.search_list, qtde_pag)
            page_number = request.GET.get('page', 1)
            page_obj = paginator.get_page(page_number)
            return render(request, 'list.html', {'page_obj': page_obj,'mealsearch': request.GET.get('searchfield')})
        else:
            meals.search(search_key2)
            paginator = Paginator(meals.search_list, qtde_pag)
            page_number = request.GET.get('page', 1)
            page_obj = paginator.get_page(page_number)
            return render(request, 'list.html', {'page_obj': page_obj,'mealsearch': request.GET.get('searchfield')})