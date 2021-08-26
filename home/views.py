from .models import Description , Images
from django.shortcuts import render
from django.utils import six
import json
from django.core import serializers
from django.http import HttpResponse

def index_page(request):
    if request.method == "POST":
        images = request.FILES.getlist('image_name')
        post_dict = dict(six.iterlists(request.POST))
        description_name = post_dict["description"]
        # this line don't need but 
        c = 1
        description_name___ = {}
        for thisisname in range(len(description_name)):
            description_name___[str(c)]=description_name[thisisname]
            c += 1
        pic_description = Description.objects.create(Album=request.POST["Album"],pic_description=description_name___)
        pic_description.pic_description = json.dumps(description_name)
        pic_description.save()
        for image in images:
            Images.objects.create(pic_description=pic_description,image = image)
        return render(request, "index.html")
    else:
        return render(request, "index.html")


def image_load(request):
    try:
        img = Images.objects.all()
        img_json = serializers.serialize('json', img)
        return HttpResponse(img_json, content_type='application/json')
    except:
        return render(request, "index.html")


    