from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse


# Create your views here.
@login_required(login_url="/login/")
def dashboard_api(request):
    return render(request, "dashboard_file.html")


def startFlowAnalysis(request):
    if request.method == "POST":
        value = request.POST.get("value")
        print("Start Detection:", value)
        return JsonResponse(
            {
                "data": [
                    {
                        "src": "10.0.2.4",
                        "dst": "10.0.2.5",
                        "status": "Covert",
                        "type": "IAT",
                    }
                ]
            },
            status=201,
        )
    else:
        return HttpResponse("Only POST requests allowed", status=302)


def insertTcpOverridingModule(request):
    if request.method == "POST":
        value = request.POST.get("value")
        print("TCP Overriding:", value)
        return HttpResponse("Success", status=201)
    else:
        return HttpResponse("Only POST requests allowed", status=302)


def insertDelyaQueue(request):
    if request.method == "POST":
        value = request.POST.get("value")
        print("Delay Overriding:", value)
        return HttpResponse("Success", status=201)
    else:
        return HttpResponse("Only POST requests allowed", status=302)


def applyTtlMaximization(request):
    if request.method == "POST":
        value = request.POST.get("value")
        print("TTL Overriding:", value)
        return HttpResponse("Success", status=201)
    else:
        return HttpResponse("Only POST requests allowed", status=302)
