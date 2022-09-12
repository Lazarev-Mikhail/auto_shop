from django.contrib import admin

# Register your models here.

from .models import Auto, Brend, Gallery_of_one_car
from django.db.models import QuerySet


# Register your models here.
class PriceFilter(admin.SimpleListFilter):
    title = 'Фильтр по цене'
    parameter_name = 'price'

    def lookups(self, request, model_admin):
        return [
            ('<500000', 'Дешевые'),
            ('от 500000 до 1500000', 'Средние'),
            ('от 1500000 до 4000000', 'Дорогие'),
            ('>=4000000', 'Люксовые'),
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == '<500000':
            return queryset.filter(price__lt=500000)
        elif self.value() == 'от 500000 до 1500000':
            return queryset.filter(price__gte=500000).filter(price__lt=1500000)
        elif self.value() == 'от 1500000 до 4000000':
            return queryset.filter(price__gte=1500000).filter(price__lt=4000000)
        elif self.value() == '>=4000000':
            return queryset.filter(price__gte=4000000)


class Gallery_of_one_car_Inline(admin.TabularInline):
    fk_name = 'auto'
    model = Gallery_of_one_car


@admin.register(Auto)  # привязка при помощи декоратора
class AutoAdmin(admin.ModelAdmin):
    list_display = ['name', 'year', 'brend', 'price']
    list_editable = ['year', 'brend', 'price']
    ordering = ['-price']
    list_per_page = 10
    search_fields = ['name__startwith']
    list_filter = [PriceFilter]
    prepopulated_fields = {'slug_auto': ('name',)}
    inlines = [Gallery_of_one_car_Inline, ]


@admin.register(Brend)
class BrendAdmin(admin.ModelAdmin):
    list_display = ['name']
