from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from markdown2 import markdown_path
from django.contrib import messages
from django.urls import reverse

from . import util
import os 
import random

def create_random_entry():
    return random.choice(util.list_entries())


"""Home page"""
def index(request):
    random_entry = './wiki/' + create_random_entry()

    entries = []
    heading = "All pages"

    # User search
    if request.method == "POST":
        title = request.POST.get("title").lower()

        # Find entries has title as substring 
        for entry in util.list_entries():
            if entry.find(title) != -1:
                entries.append(entry)
        
        # No entry match 
        if len(entries) == 0: 
            messages.error(request, 'What you are searching for is not exist. Click on the side bar to create it if you want to.')
            return HttpResponseRedirect(reverse("encyclopedia:index"))

        # One entry match
        elif len(entries) == 1:
            return HttpResponseRedirect(reverse("encyclopedia:wiki", args=[entries[0]]))
        
        #Multiple entries match
        else:
            heading = "Matching Results"

    else: entries = util.list_entries()
            
    return render(request, "encyclopedia/index.html", {
        "entries": entries, "random_entry": random_entry, "heading": heading
    })


"""Entry a page"""
def wiki(request, title):
    random_entry = './' + create_random_entry()

    # Convert title to lowercase
    title = title.lower()

    # Title not exist, display message
    if title not in util.list_entries():
        messages.error(request, 'What you are searching for is not exist. Click on the side bar to create it if you want to.')
        return HttpResponseRedirect(reverse("encyclopedia:index"))

    # Convert markdown to html by markdown2 package 
    html = markdown_path(f'./entries/{title}.md')

    return render(request, "encyclopedia/wiki.html", {
        "html": html, "title": title.capitalize(), "random_entry": random_entry
    })


"""Create new page"""
def new(request):
    if request.method == "POST":
        data = request.POST.copy()

        title = data.get("title").lower()
        content = data.get("content")

        # Handle title bug
        if title == "" or title in util.list_entries():
            if title == "": messages.error(request, "Please type in your page's title")
            else: messages.error(request, "Your title has been taken")
            return render(request, "encyclopedia/new.html", {
                "title":"Create New Page", "content": content
            })

        # Save
        content = f"# {title.capitalize()}\n" + content
        util.save_entry(title, content)
        return HttpResponseRedirect(reverse("encyclopedia:wiki", args=[title]))

    return render(request, "encyclopedia/new.html", {
        "title":"Create New Page", "content": "Enter markdown content here"
    })


"""Edit entry"""
def edit(request, title):
    title = title.lower()
    content = util.get_entry(title)

    # Get content from <textarea> and then save it
    if request.method == "POST":
        data = request.POST.copy()
        content = data.get("edit")

        util.save_entry(title, content)
        return HttpResponseRedirect(reverse("encyclopedia:wiki", args=[title]))

    return render(request, "encyclopedia/edit.html",{
        "title": title.capitalize(), "content": content
    })
