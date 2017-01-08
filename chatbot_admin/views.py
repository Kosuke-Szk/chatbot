import json
from django.http import HttpResponse
from django.core import serializers
from chatbot_admin.models import User, Account

def dispose():
  outputlist = []
  usernames = Account.objects.all().values()
  for a in usernames:
    username = a["username"]+ ","
    outputlist.append(username)
  print(outputlist)
  return outputlist

def show_users(request):
  return HttpResponse(serializers.serialize("json", User.objects.all()))

def show_usernames(request):
  print(request)
  outputlist = dispose()
  return HttpResponse(outputlist)