from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406496076',
        'name': 'Raffi Dewangga Susanto',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)
