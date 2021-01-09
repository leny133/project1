from django.shortcuts import render
from django.utils import html
from . import util
from markdown2 import Markdown
from django.http import HttpResponse

markdowner = Markdown()

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def search(request, title):
    if util.get_entry(title) == None:
        content=None
    else:
        content=markdowner.convert(util.get_entry(title))
    return render(request, "wiki/index.html",{
        "content" : content,
        "title" : title
    })