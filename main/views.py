from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'npm' : '2406432910',
        'name': 'Peter Yap',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)
