from django.shortcuts import render

# Представление главной страницы
def index(request):
    return render(request, 'infomax/index.html')
