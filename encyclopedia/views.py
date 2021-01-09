from django.shortcuts import render
from django.utils import html
from . import util
from markdown2 import Markdown
from django.http import HttpResponse
from django import forms
import re

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
markdowner = Markdown()


class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Search")

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, title):
    if util.get_entry(title) == None:
        content=None
    else:
        content=markdowner.convert(util.get_entry(title))
    return render(request, "wiki/index.html",{
        "content" : content,
        "title" : title
    })

def search(request):
    title = request.POST['q']
    entries=[]
    if request.method == "POST":
        if util.get_entry(title) == None:
            slist=util.list_entries()
            for title in slist:
                entries.append(title)
            return render(request, "encyclopedia/index.html", {
        "entries": list(entries)
    })
            
        else:
            content=markdowner.convert(util.get_entry(title))
    return render(request, "wiki/index.html",{
        "content" : content,
        "title" : title
    })   
        