from django.shortcuts import render

def show_main(request):
    context = {
        'name' : 'Final Fantasy V',
        'price': '600000',
        'description': 'Adventure Video Games'
    }

    return render(request, "main.html", context)