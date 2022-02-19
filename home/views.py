# 'reverse' s/cut allows lookup of a url by name given in urls.py
from django.shortcuts import render
# get_object_or_404


# to display home page


def welcome(request):
    name = "Marty"

    return render(request,
                  'index.html', {
                                "name": name,
                                })
