from django.http import HttpResponse
from django.shortcuts import render, redirect
import docker
import time
from random import randint

# Create your views here.
def index(request):
    # fetch all images
    image_list = get_images()
    image_list = [i.short_id[7:] for i in image_list]
    context = {'image_list': image_list}
    return render(request, 'dctrl/index.html', context)


def get_images():
    image_list = []
    client = docker.from_env()
    image_list = client.images.list()
    return image_list

def container(request, container_id, action):
    client = docker.from_env()
    host_port = randint(3000, 3999)
    container = client.containers.run('project2:v6',
                                      detach=True,
                                      auto_remove=True,
                                      ports={'3000/tcp': host_port})
    print(container.status)
    time.sleep(5)
    # context = {'container': container}
    # return render(request, 'dctrl/container.html', context)
    return redirect('http://localhost:'+str(host_port))
