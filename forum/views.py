from django.shortcuts import render
from django.urls import reverse
from django.db.models import Count
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def home(request):
    threads = thread.objects.all()
    formulir = threadForm()
    data = {'threads' : threads, 'formulir' : formulir}
    return render(request, 'forum/index.html', data)

# CRUD Postingan

def post(request):
    pass

def createPost(request):
    formulir = threadForm()
    if request.method == "POST":
        formulir = threadForm(request.POST)
        if formulir.is_valid():
            formulir.save()
            return redirect(reverse('home'))
    date = {'formulir' : formulir}
    pass

def showPost(request, id):
    singleThread = thread.objects.filter(id = id).first()
    komentarThread = reply.objects.filter(thread_id = id).all()
    formulir = komentarForm(initial={'thread_id' : singleThread})
    data = {'thread' : singleThread, 'komentars' : komentarThread, 'formulir_komentar': formulir}
    return render(request, 'forum/show.html', data)

def editPost(request, id):
    singleThread = thread.objects.filter(id = id).first()
    formulir = threadForm(instance=singleThread)
    if request.method == "POST":
        formulir = threadForm(request.POST, instance=singleThread)
        if formulir.is_valid():
            formulir.save()
            return redirect('/thread/show/'+str(id))
    data = {'thread':singleThread,'formulir':formulir}
    return render(request, 'forum/edit_thread.html', data)

def deletePost(request, id):
    singleThread = thread.objects.filter(id = id).first()
    singleThread.delete()
    return redirect('home')

def createKomentar(request, thread_id):
    singleThread = thread.objects.filter(id = thread_id).first()
    if request.method == "POST":
        formulir = komentarForm(request.POST)
        print(request.POST)
        if formulir.is_valid():
            formulir.save()
            return redirect('/thread/show/'+str(thread_id))

def editKomentar(request, thread_id, id):
    komentar = reply.objects.filter(id = id).first()
    formulir = komentarForm(instance=komentar)
    if request.method == "POST":
        formulir = komentarForm(request.POST, instance=komentar)
        if formulir.is_valid():
            formulir.save()
            return redirect('/thread/show/'+str(thread_id))
    data = {'komentar':komentar,'formulir_komentar':formulir}
    return render(request, 'forum/edit_komentar.html', data)

def deleteKomentar(request, thread_id, id):
    komentar = reply.objects.filter(id = id).first()
    komentar.delete()
    return redirect('/thread/show/'+str(thread_id))

def authorThreads(request, penulis):
    threads = thread.objects.filter(penulis = penulis)
    formulir = threadForm()
    data = {'threads' : threads, 'formulir' : formulir}
    return render(request, 'forum/index.html', data)
