from datetime import datetime
import os.path
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

global file_name
file_name = ""


@csrf_exempt
def index(request):
    return HttpResponse(status=204)


@csrf_exempt
def create_file(request):
    global file_name
    if file_name == "":
        file_name = str(datetime.now())
    for char in (":", ".", " "):
        file_name = file_name.replace(char, "-")
    file_name += '.txt'
    with open('./logs/' + file_name, 'w') as f:
        f.write('time, fr, fl, rr, rl, head, roll, pitch, sys, gyro, acc, mag, proximity\n')
    with open('./logs/log.txt', 'w'):
        pass

    return JsonResponse({'file_name': file_name}, status=200)


@csrf_exempt
def add_line(request):
    file_name = request.POST['file_name']
    line = request.POST['line']
    with open('./logs/' + file_name, 'a') as f:
        f.write(line + '\n')
    with open('./logs/log.txt', 'a') as f:
        f.write(line[line.index(',') + 2:].replace(',', '') + '\n')

    return JsonResponse(data={}, status=200)


@csrf_exempt
def create_image_directory(request):
    global file_name
    if file_name == "":
        file_name = str(datetime.now())
    image_directory_name = file_name
    for char in (":", ".", " "):
        image_directory_name = image_directory_name.replace(char, "-")
    os.mkdir('./images_logs/' + image_directory_name)

    return JsonResponse({'directory_name': image_directory_name}, status=200)


@csrf_exempt
def add_image(request):
    image = request.FILES['file']
    image_directory_name = request.POST['directory_name']
    base_address = './images_logs/' + image_directory_name + '/'
    image_file_name = str(len(os.listdir(base_address)) + 1)
    with open(base_address + image_file_name, 'wb+') as f:
        for chunk in image.chunks():
            f.write(chunk)

    return JsonResponse(data={}, status=200)

