from django.shortcuts import render
from aplicaciones.blog.models import categoria, Autor, Post
    
from django.http import HttpResponse
from django.core import serializers

def lista(request, slug):
    listas = serializers.serialize('json', Post.objects.filter(slug = categoria))
    #return HttpResponse(serialize('json', use_natural_foreign_keys = True), 'application/json')

    return HttpResponse(listas, content_type='application/json')

def home(request):

    potss=Post.objects.filter(estado= True)
    return render(request, 'index.html', {"publi":potss})

def post(request, slug):
    potst=Post.objects.get(
        slug = slug
    )
    print(potst)
    return render(request, 'post.html', {'detalle_post':potst})

#def categorias(request):
    #cate=categoria.objects.filter(estado= True)
    #return render(request, 'categorias.html', {"bloc":cate})

def bloca(request, categoria):
    bloc=Post.objects.get(
        categoria = categoria
    )
    return render(request, 'categorias.html', {"catego":cate})


def tecno(request):
    tec = Post.objects.filter(categoria = 3)
    titu = 'Tecnologia'
    return render(request, 'categ.html', {"tecno":tec, "tit":titu}) 

def depo(request):
    dep = Post.objects.filter(categoria = 4)
    titu = 'Deportes'
    return render(request, 'categ.html', {"tecno":dep, "tit":titu}) 

def cien(request):
    cin = Post.objects.filter(categoria = 5)
    titu = 'Ciencias'
    return render(request, 'categ.html', {"tecno":cin, "tit":titu}) 

def espc(request):
    cin = Post.objects.filter(categoria = 6)
    titu = 'Espectáculos'
    return render(request, 'categ.html', {"tecno":cin, "tit":titu}) 

def sal(request):
    salu = Post.objects.filter(categoria = 7)
    titu = 'Salud'
    return render(request, 'categ.html', {"tecno":salu, "tit":titu}) 

def his(request):
    hist = Post.objects.filter(categoria = 8)
    titu = 'Historia'
    return render(request, 'categ.html', {"tecno":hist, "tit":titu}) 


def edu(request):
    educ = Post.objects.filter(categoria = 9)
    titu = 'Educacion'
    return render(request, 'categ.html', {"tecno":educ, "tit":titu}) 

def vid(request):
    vide = Post.objects.filter(categoria = 10)
    titu = 'Videojuegos'
    return render(request, 'categ.html', {"tecno":vide, "tit":titu}) 

#def blogc(request, categoria):
    #blc=Post.objects.get(
        #categoria = categoria
    #)
    #return render(request, 'bcat.html', {'bloc':blc})
    #blc = Post.objects.filter(categoria = 'id')
    #return render(request, 'bcat.html', )