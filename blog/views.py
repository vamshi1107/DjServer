from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from blog.serializers import BlogSerializer, UserSerializer
from blog.models import *

from django.core.paginator import Paginator


def index(request):
    return HttpResponse("hi")


@api_view(['POST'])
def adduser(request):
    r = JSONParser().parse(request)
    if not checkuser(r["username"]):
        u = User(username=r["username"], password=r["password"],
                 name=r["name"], email=r["email"], dp=r["dp"])
        u.save()
        return JsonResponse({"status": True, "msg": "user added"})
    else:
        return JsonResponse({"status": False, "msg": "username already exists"})


def checkuser(username):
    users = User.objects.filter(username=username)
    return len(users) > 0


@api_view(['POST'])
def loginuser(request):
    parser = JSONParser()
    r = parser.parse(request)
    u = User.objects.filter(username=r["username"], password=r["password"])
    if len(u) > 0:
        return JsonResponse({"status": True, "data": UserSerializer(u[0]).data})
    else:
        return JsonResponse({"status": False})


@api_view(['POST'])
def addblog(request):
    r = JSONParser().parse(request)
    if checkuser(r["username"]):
        b = BlogSerializer(data=r)
        if b.is_valid():
            b.save()
        return JsonResponse({"status": True, "msg": "blog added"})
    else:
        return JsonResponse({"status": False, "msg": "unable to add"})


@api_view(['POST'])
def myblogs(request):
    r = JSONParser().parse(request)
    if checkuser(r["username"]):
        b = Blog.objects.filter(username=r["username"])
        if len(b) > 0:
            data = []
            for i in b:
                data += [BlogSerializer(i).data]
            return JsonResponse({"status": True, "data": data})
        else:
            return JsonResponse({"status": True, "data": []})
    else:
        return JsonResponse({"status": False})


@api_view(['POST'])
def getblogs(request):
    r = JSONParser().parse(request)
    page = r["page"]
    b = Blog.objects.order_by("date").all()
    paginator = Paginator(b[::-1], 5)
    pages = paginator.num_pages
    if page <= pages:
        p = paginator.page(page)
        data = []
        for i in p:
            data += [BlogSerializer(i).data]
        return JsonResponse({"status": True, "data": data, "last": False})
    else:
        return JsonResponse({"status": True, "data": [], "last": True})


@api_view(['POST'])
def getpopular(request):
    b = Blog.objects.order_by("-date",).order_by("-count").all()
    data = []
    for i in b:
        v = BlogSerializer(i).data
        v["head"] = "".join(v["content"].split(".")[:6])
        data += [v]
    return JsonResponse({"status": True, "data": data, "last": False})
