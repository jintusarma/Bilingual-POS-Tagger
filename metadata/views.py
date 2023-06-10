from django.shortcuts import render,redirect
from main.models import Tagset
from .utils import *

# Create your views here.
def add_tagset(request):
    # ver_list = check_verifier_admin()
    # if request.user in ver_list:
    if request.method == "POST":
        tagset_name = request.POST['name']
        # tag_name = request.POST['tag_name']
        # tag_value = request.POST['tag_value']
        tag_name = request.FILES['tag_name']
       
        tagset_description = []
        if tag_name:
            for line in tag_name:
                text = line.decode('utf-8').strip()
                tagset_description.append(text)
        
        
        
        tagset_description = ' , '.join(tagset_description)
        # tagset_values = ' , '.join(tagset_values)

        tagset_descrip = tagset_desc(tagset_description)
        tagset_values = tagset_val(tagset_description)


        # print(tagset_descrip,"\n\n",tagset_values)


        # print(tagset_description,tagset_values,"\n\n")
        Tagset.objects.create(tagset_name=tagset_name ,tagset_description=tagset_descrip , tagset_values=tagset_values)
        return redirect(add_tagset)
    return render(request,'tagset.html')