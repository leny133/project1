from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def search(request, title):
    return render(request, "wiki/index.html",{
        "content" : util.get_entry(title),
        "title" : title
    })