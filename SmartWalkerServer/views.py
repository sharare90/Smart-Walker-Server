from datetime import datetime

from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def create_file(request):
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

