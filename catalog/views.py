from django.shortcuts import render, get_object_or_404
from .models import Auto, Brend, Gallery_of_one_car
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from .forms import AutoCostFilterForm
from django.core.paginator import Paginator


# Create your views here.

class IndexTemplate(TemplateView):
    template_name = 'catalog/index.html'


# Отображение с фильтром и паггинацией
def show_all_cars(request):
    autos = Auto.objects.all()
    form = AutoCostFilterForm(request.GET)
    if form.is_valid():
        if form.cleaned_data['min_price']:
            autos = autos.filter(price__gte=form.cleaned_data['min_price'])
    if form.is_valid():
        if form.cleaned_data['max_price']:
            autos = autos.filter(price__lte=form.cleaned_data['max_price'])
    paginator = Paginator(autos, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'catalog/all_cars.html', context={'autos': page_obj, 'form': form})


def show_one_auto(request, slug_auto: str):
    auto = get_object_or_404(Auto, slug_auto=slug_auto)
    gallery = Gallery_of_one_car.objects.all()
    return render(request, 'catalog/show_one_car.html', context={
        'auto': auto,
        'gallery': gallery,
    })


class ListBrend(ListView):
    template_name = 'catalog/brends.html'
    model = Brend
    context_object_name = 'brends'


def show_brend_car(request, brend_auto: str):
    brend = Brend.objects.get(name=brend_auto.capitalize())
    autos = brend.autos.all()
    form = AutoCostFilterForm(request.GET)
    if form.is_valid():
        if form.cleaned_data['min_price']:
            autos = autos.filter(price__gte=form.cleaned_data['min_price'])
    if form.is_valid():
        if form.cleaned_data['max_price']:
            autos = autos.filter(price__lte=form.cleaned_data['max_price'])
    return render(request, 'catalog/show_brend_car.html', context={
        'autos': autos,
        'brend': brend,
        'form': form,
    })


def contact(request):
    return render(request, 'catalog/contact.html')
