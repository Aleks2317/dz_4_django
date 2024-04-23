from django.contrib import admin
from .models import Coin, Cube, Number


@admin.action(description='Изменить результат игры на Решка')
def reset_result_egle(modeladmin, request, queryset):
    queryset.update(result='Решка')


@admin.action(description='Изменить результат игры на Орел')
def reset_result_tails(modeladmin, request, queryset):
    queryset.update(result='Орел')


class CoinAdmin(admin.ModelAdmin):
    list_display = ['date_ordered', 'name', 'result']
    list_filter = ['date_ordered']
    search_fields = ['date_ordered']
    search_help_text = 'Поиск по полю date_ordered (пример: 2024-05-12)'
    actions = [reset_result_egle, reset_result_tails]


class CubeAdmin(admin.ModelAdmin):
    list_display = ['date_ordered', 'name', 'result']
    list_filter = ['date_ordered']
    search_fields = ['date_ordered']
    search_help_text = 'Поиск по полю date_ordered (пример: 2024-05-12)'
    actions = [reset_result_egle, reset_result_tails]


class NumberAdmin(admin.ModelAdmin):
    list_display = ['date_ordered', 'name', 'result']
    list_filter = ['date_ordered']
    search_fields = ['date_ordered']
    search_help_text = 'Поиск по полю date_ordered (пример: 2024-05-12)'
    actions = [reset_result_egle, reset_result_tails]


admin.site.register(Coin, CoinAdmin)
admin.site.register(Cube, CubeAdmin)
admin.site.register(Number, NumberAdmin)
