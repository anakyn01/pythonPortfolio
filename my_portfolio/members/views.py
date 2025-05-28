#from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader #불러온다는건 그걸 사용하겠다는 의미

#메인
def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def members(request):
    template = loader.get_template('myfirst.html')
    context = {
        'greeting':1,
    }
    return HttpResponse(template.render())
