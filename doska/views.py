from django.http import HttpResponse

def home(request):
    print request
    return HttpResponse("""Hello world. From server gfdgdfgdfg 
dfgfdgdf dfgdfgkldlfkg d;flkg dlfkg""")


