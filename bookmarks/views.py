from django.shortcuts import render
from .models import Bookmark, PrivateBookmark

# Create your views here.


def index(request):
    # context = {
    #     "bookmarks": Bookmark.objects.all(),
    #     "private_bookmarks": PrivateBookmark.objects.filter(user=request.user)
    # }

    if request.user.is_anonymous:
        pbids = PrivateBookmark.objects.values_list('id')
        bookmarks = Bookmark.objects.filter(id=pbids)
        context = {
            "bookmarks": bookmarks,
            "private_bookmarks": PrivateBookmark.objects.none()
        }
    else:
        context = {
            "bookmarks": Bookmark.objects.all(),
            "private_bookmarks": PrivateBookmark.objects.filter(user=request.user)
        }

    return render(request, 'bookmarks/index.html', context)
