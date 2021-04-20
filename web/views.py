from django.shortcuts import render
from django.http import JsonResponse
from json import JSONEncoder
from django.views.decorators.csrf import csrf_exempt
from web.models import Token, Purchaseinq, post, User
from datetime import datetime
# Create your views here.

@csrf_exempt
def submit_post(request):
    """ user submit request to post here. """
    print ("we are in submit post")
    print (request.POST)
    
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token=this_token).get()
    if 'date' not in request.POST:
        date = datetime.now()
    post.objects.create(user = this_user,title = request.POST['title'], text = request.POST['text'], price = request.POST['price'] ,date=date)
    

    return JsonResponse({
        "status":"ok"
    },encoder= JSONEncoder)

@csrf_exempt
def submit_Purchaseinq(request):
    """ user submit request to post here. """
    print ("we are in submit purchaseinq")
    print (request.POST)
    
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token=this_token).get()
    if 'date' not in request.POST:
        date = datetime.now()
    Purchaseinq.objects.create(user = this_user,title = request.POST['title'], text = request.POST['text'], priceTarget = request.POST['priceTarget'] ,date=date)
    

    return JsonResponse({
        "status":"ok"
    },encoder= JSONEncoder)
