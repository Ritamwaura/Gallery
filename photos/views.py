from django.shortcuts import render
from django.http  import HttpResponse
from .models import Photo

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')

def search_results(request):
    
    if 'photo' in request.GET and request.GET["photo"]:
        search_term = request.GET.get("photo")
        searched_articles = photo.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-photos/search.html',{"message":message,"photo": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html',{"message":message})
def photo(request,article_id):
    try:
       photo =Photo.objects.get(id =photo_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-news/article.html", {"article":article})       