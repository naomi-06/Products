from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world")
def sum(request):
    a = int(request.GET.get('a', 0))
    b = int(request.GET.get('b', 0))
    result = a + b
    return HttpResponse(f"The sum of {a} and {b} is {result}.")
def user(request,user_id):
    users = {
        1: "Alice",
        2: "Bob",
        3: "Charlie"
    }

    if user_id in users:
        return HttpResponse(f"Hello, {users[user_id]}!")
    return HttpResponse("User not found.")