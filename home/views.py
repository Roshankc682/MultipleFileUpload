from .models import Informations , Images
from django.shortcuts import render
from django.utils import six
import json

def index_page(request):
    if request.method == "POST":
        images = request.FILES.getlist('image_name')
        # print(images)
        post_dict = dict(six.iterlists(request.POST))
        print(post_dict)
        skills_name = post_dict["skills"]
        c = 1
        name_image = {}
        for thisisname in range(len(skills_name)):
            name_image[str(c)]=skills_name[thisisname]
            c += 1
        print(name_image)
        information = Informations.objects.create(information_name=request.POST["information_name"],json_text_field=name_image)
        information.json_text_field = json.dumps(skills_name)
        information.save()

        for image in images:
            print(image)
            Images.objects.create(information=information,image = image)

        return render(request, "index.html")
    else:
        return render(request, "index.html")
