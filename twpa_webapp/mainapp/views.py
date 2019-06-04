from django.shortcuts import render


def main(request):
    context = {'title': 'Главная'}
    return render(request, 'mainapp/base.html', context)