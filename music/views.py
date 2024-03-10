from django.shortcuts import render
from musicbeats.models import Song

def index(request):
    song = Song.objects.all()
    return render(request,'index.htm',{'song':song})

def songs(request):
    return render(request,'songs.htm')

def songpost(request,id):
    song = Song.objects.filter(song_id=id).first()
    return render(request,'musicbeats/songpost.htm',{'song':song})
def singer(request):
    return render(request,'singer.htm')



