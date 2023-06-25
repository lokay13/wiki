import random
import markdown2
from django.shortcuts import render, redirect

from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def create(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        existing_entry = util.get_entry(title)
        if existing_entry:
            return render(request, "encyclopedia/error.html", {
                "error": "An encyclopedia article with that title already exists."
            })
        util.save_entry(title, content)
        return redirect("article", title)
    else:
        return render(request, "encyclopedia/create.html")
    
def edit(request, title):
    if request.method == "POST":
        content = request.POST["content"]
        util.save_entry(title, content)
        return redirect("article", title)
    else:
        entry = util.get_entry(title)
        if entry is None:
            return render(request, "encyclopedia/error.html", {
                "error": "The requested page does not exist."
            })
        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "content": entry
        })

def article(request, title):
    entry = util.get_entry(title)
    if entry:
        entry_html = markdown2.markdown(entry)
        return render(request, "encyclopedia/article.html", {
            "title": title,
            "entry_html": entry_html
        })
    else:
        return render(request, "encyclopedia/error.html", {
            "error": f"The article '{title}' does not exist."
        })
    
def search(request):
    query = request.GET.get('q', '')
    entries = util.list_entries()
    matched_entries = [entry for entry in entries if query.lower() in entry.lower()]
    if query in entries:
        return redirect('article', title=query)
    else:
        return render(request, "encyclopedia/search_results.html", {
            "query": query,
            "matched_entries": matched_entries
        })
    
def random_article(request):
    entries = util.list_entries()
    random_entry = random.choice(entries)
    return redirect('article', title=random_entry)