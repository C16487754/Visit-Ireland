from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewAttractionForm
from .models import County, Attraction, Comment
from .forms import CommentForm
from django.db.models import Count

from django.utils import timezone
from django.contrib.auth.decorators import login_required


def home(request):
    counties = County.objects.all()
#Return the page home.html 
    return render(request, 'home.html', {'counties': counties})


def county_attractions(request, pk):
    county = get_object_or_404(County, pk=pk)
    attractions = county.attractions.order_by('-last_updated').annotate(replies=Count('comments'))
    return render(request, 'attractions.html', {'county': county, 'attractions': attractions})



def attraction_comments(request, pk, attraction_pk):
    attraction = get_object_or_404( Attraction, county__pk=pk, pk=attraction_pk)
    attraction.views += 1
    attraction.save()
    return render(request, 'attraction_comments.html', {'attraction': attraction})




@login_required
def reply_attraction(request, pk, attraction_pk):
    attraction = get_object_or_404(Attraction, county__pk=pk, pk=attraction_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.attraction = attraction
            comment.created_by = request.user
            comment.save()
            attraction.last_updated = timezone.now()  # <- here
            attraction.save()                         # <- and here

            return redirect('attraction_comments', pk=pk, attraction_pk=attraction_pk)
    else:
        form = CommentForm()
    return render(request, 'reply_attraction.html', {'attraction': attraction, 'form': form})
