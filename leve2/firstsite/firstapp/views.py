from django.shortcuts import render,HttpResponse
from django.template import Context,Template
from firstapp.models import People,Article,Comment
from django import forms


# Create your views here.

class CommentForm(forms.Form):
    name = forms.CharField(max_length=50)
    comment = forms.CharField()
def index(request):
    print (request)
    print('==='*20)
    print (dir(request))
    queruset = request.GET.get('tag')
    print (queruset)
    if queruset:
        article_list = Article.objects.filter(tag=queruset)
    else:
        article_list = {}
    context = {}
    context['article_list'] = article_list
    index_page = render(request,'first_web_2.html', context)
    #assert False
    return index_page

def detail(request):
    form = CommentForm
    context = {}
    comment_list = Comment.objects.all()
    context['comment_list'] = comment_list
    context['form'] = form
    return render(request,'detail.html',context)
