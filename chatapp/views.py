from django.shortcuts import render

# Create your views here.
def get_frontpage(request):
    return render(request, 'chatapp/frontpage.html')