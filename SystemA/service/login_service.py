from django.http import HttpResponse
from ..data.login_data import login_data
from ..data.getCourse_data import getCourse_data

def login(request):
    account=request["account"]
    password=request["password"]
    valid=login_data(account,password)
    if valid:
        #TODO get student info

        #TODO get course list
        courseInfo=getCourse_data(sid)
    else:
        return HttpResponse("Wrong")