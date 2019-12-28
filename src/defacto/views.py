from django.shortcuts import render
from .lang import lang


def home(request):
    """ Home page handler """

    return render(request, 'core/index.html', {
        'lang' : lang['mon']
    })


def about(request):
    """ About page handler """
    return render(request, 'core/pages/about.html')


def contact(request):
    """ Contact page handler """
    return render(request, 'core/pages/contact.html')
