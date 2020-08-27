from django.shortcuts import render


def homepage(request):

    context = {
        "title": "First Django project",
        "msg" : "Hello World!"
    }

    return render(request, "index.html", context)
