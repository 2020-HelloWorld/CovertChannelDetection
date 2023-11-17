from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
import subprocess, threading
import os, json


# Create your views here.
@login_required(login_url="/login/")
def dashboard_api(request):
    return render(request, "dashboard_file.html")


def startFlowAnalysis(request):
    if request.method == "POST":
        value = request.POST.get("value")

        # Clear all the previous data
        subprocess.call(["sh", "./cleanup.sh"])
        os.system("python3 ./cleanup.py")

        # Start new analysis
        print("Start Detection:", value)

        def run_command(command):
            try:
                subprocess.run(command, check=True)
            except subprocess.CalledProcessError as e:
                print(f"Threads stopped: {command}: {e}")

        def capture_data():
            command1 = [
                "timeout",
                str(300),
                "bash",
                "./delay_detect/layer2_detect.sh",
            ]
            command2 = [
                "timeout",
                str(300),
                "bash",
                "./ttl_detect/layer1_detect.sh",
            ]

            # Create threads for each command
            thread1 = threading.Thread(target=run_command, args=(command1,))
            thread2 = threading.Thread(target=run_command, args=(command2,))

            # Start the threads
            thread1.start()
            thread2.start()

            # Wait for both threads to finish
            thread1.join()
            thread2.join()

        def analyse_capture():
            subprocess.run(["bash", "./delay_detect/layer2_analysis.sh"], check=True)
            subprocess.run(["bash", "./ttl_detect/layer1_analysis.sh"], check=True)

        if value == True:
            data = []

            try:
                capture_data()
                analyse_capture()

            except Exception as e:
                print("Unexpected Exception:", e)

            with open("./temp_json/flow_result.json", "r") as json_file:
                json_data = json.load(json_file)
                for flow in json_data:
                    if flow["isCovert"]:
                        data.append(
                            {
                                "src": flow["src"],
                                "dst": flow["dst"],
                                "status": "Covert" if flow["isCovert"] else "Overt",
                                "type": "IAT",
                            }
                        )
            # Load JSON data from file
            with open("./temp_json/currently_covert.json", "r") as json_file:
                json_data = json.load(json_file)
                # Construct the command based on JSON data
                for key, value in json_data.items():
                    source_ip, dest_ip = key.split(" - ")
                    data.append(
                        {
                            "src": source_ip,
                            "dst": dest_ip,
                            "status": "Covert",
                            "type": "TTL",
                        }
                    )
            return JsonResponse({"data": data}, status=201)
        else:
            return HttpResponse("False received", status=201)

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
