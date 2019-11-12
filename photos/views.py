from django.shortcuts import render
from django.http  import HttpResponse
from .models import Photo

# Create your views here.
def welcome(request):
    images=Photo.objects.all()
    
    return render(request,'welcome.html',{'images':images})

def search_results(request):
    
    if 'image' in request.GET and request.GET["image"]:
        
        search_term = request.GET.get("image")
        
        searched_articles = Photo.search_by_title(search_term)
        message = "{}".format(search_term)

        return render(request, 'all-photos/search.html',{"message":message,"photo": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html',{"message":message})
    
#def photo(request,article_id):
#    try:
#       photo =Photo.objects.get(id =photo_id)
#    except DoesNotExist:
#        raise Http404()
#    return render(request,"all-news/article.html", {"article":article})       