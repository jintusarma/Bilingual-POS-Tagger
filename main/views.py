from datetime import timezone
from django.shortcuts import render,redirect
from accounts.models import *
from .models import *
from .utils import *
from django.core.paginator import Paginator
import csv
import zipfile
from django.http import HttpResponse
from io import BytesIO
# Create your views here.

def home(request):
    # ver1 = Verifier.objects.filter(verifier_type = 'verfier_1')
    # ver2 = Verifier.objects.filter(verifier_type = 'verfier_2')
    # ver3 = Verifier.objects.filter(verifier_type = 'admin')
    ver_list1 = check_verifier1()
    ver_list2 = check_verifier2()
    ver_list3 = check_verifier_admin()

    # for x in ver1:
    #     ver_list1.append(x.verifier)
    
    # for x in ver2:
    #     ver_list2.append(x.verifier)

    # for x in ver3:
    #     ver_list3.append(x.verifier)

    return render(request,'index.html',{'ver1':ver_list1,'ver2':ver_list2,'admin':ver_list3})


def add_metadata(request):
    ver_list = check_verifier_admin()
    if request.user in ver_list:
        if request.method == "POST":
            batch = request.POST['batch']
            domain = request.POST['domain']
            language = request.POST['language']
            MetaData.objects.create(language=language,domain=domain,name=batch)
            return redirect(add_sentences)
            
        return render(request,"upload/metadata_upload.html")
    return render(request,"404error.html",)


def add_sentences(request):
    # ver = Verifier.objects.filter(verifier_type = 'admin')
    ver_list = check_verifier_admin()

    # for x in ver:
    #     ver_list.append(x.verifier)
    
    if request.user in ver_list:
        if request.method == "POST":
            file = request.FILES['files']
            action = request.POST['action']
            metadata_id = request.POST['metadata']
            metadata = MetaData.objects.get(pk=metadata_id)
            if file:
                for line in file:
                    text= line.decode('utf-8').strip()
                    if action == 'nontag':
                        sentence = Dataset.objects.create(raw_sentence=text,metadata=metadata)
                    elif action == 'tag':
                        raw_text = sentence_form(text)
                        sentence = Dataset.objects.create(raw_sentence= raw_text,tagged_sentence=text,is_default_tagged=True,metadata=metadata)
            # if action == 'nontag':
            #     return HttpResponse("Non Tag")
            # elif action == 'tag':
            #     return HttpResponse("Tag ")
            # if file:
            #     for line in file:
            #         text= line.decode('utf-8').strip()
            #         sentence = Dataset.objects.create(raw_sentence=text)
                return render(request,"suceess.html")
        metadata = MetaData.objects.all()
        return render(request,"search.html",{'metadatas':metadata})
    
    return render(request,"404error.html",)


def raw_sentences(request):
    # ver = Verifier.objects.filter(verifier_type = 'verfier_1')
    # ver_list =[]

    # for x in ver:
    #     ver_list.append(x.verifier)

    ver_list = check_verifier1()
    
    if request.user in ver_list:
        # obj = Dataset.objects.filter(is_tagged = False).order_by('?')
        obj = Dataset.objects.filter(is_tagged = False,is_default_tagged=False)
        p = Paginator(obj,10)
        page = request.GET.get('page')
        venues = p.get_page(page)

        
        if len(obj) == 0:
            return render(request,"clear.html")
        return render(request,"validator1.html",{'outputs':obj,'venues':venues})
    return render(request,"404error.html",)

from django.db.models import Q


def tagged_sentences(request):
    # store all verifer labeled as verifier 2 in ver
    # ver = Verifier.objects.filter(verifier_type = 'verfier_2')

    # create an blank list so that we store the values in the list
    # ver_list =[]
    
    # Since ver retuen a query , so we create a loop and added the users in ver_list 
    # for x in ver:
    #     ver_list.append(x.verifier)
    
    # print(ver_list)
     
    # Checking if the requested user in ver_list

    ver_list = check_verifier2()

    if request.user in ver_list:
        obj = Dataset.objects.filter(Q(is_tagged=True) | Q(is_default_tagged=True) , Q(is_verified=False))
        # obj = Dataset.objects.filter(is_verified = False, is_default_tagged=True)
        p = Paginator(obj,10)
        page = request.GET.get('page')
        venues = p.get_page(page)

        if len(obj) == 0:
            return render(request,"clear.html")

        return render(request,"validator2.html",{'outputs':obj,'venues':venues})
    
    return render(request,"404error.html",)


def view_raw_sentences(request,id):
    # ver_list = check_verifier1()

    # if request.user in ver_list:
        all_data = Dataset.objects.get(pk=id)
        return render(request,'show_raw_sentence.html',{'sentence':all_data})
    
    # return render(request,"404error.html",)


def view_tagged_sentences(request,id):
    # ver_list = check_verifier2()
    # if request.user in ver_list:
    if request.method == "POST":
        text = request.POST['tag_sentence']
        action = request.POST.get('action')
        if action == 'verify':
            obj=Dataset.objects.get(id=id)
            obj.verified_sentence = text
            obj.is_verified = True
            obj.save()
            return redirect(tagged_sentences)
        elif action == "edit":
            ver = Dataset.objects.get(id=id)
            words = ver.raw_sentence.split()
            tag_word = ver.tagged_sentence.split()
            print(tag_word)
            
            return render(request,'update_verifier2.html',{'ver':ver,'words':words,'words_tag':tag_word})
        
    all_data = Dataset.objects.get(pk=id)
    return render(request,'show_tagged_sentence.html',{'sentence':all_data})
    # return render(request,"404error.html",)


def edit_raw_sentences(request,id):
    # verifier_1 = Verifier.objects.filter(verifier_type = 'verfier_1')
    # ver_list =[]

    # for x in verifier_1:
    #     ver_list.append(x.verifier)

    ver = Dataset.objects.get(id=id)
    words = ver.raw_sentence.split()

    if request.method == 'POST':
    
        selected_words = request.POST.getlist('word')
        tags = request.POST.getlist('tag')
        list_3 = []

        for i in range(len(selected_words)):
            item_1 = selected_words[i]
            item_2 = tags[i].upper()
            join_item =  item_1+ '\\' + item_2
            # join_item =  item_1+ '<' + item_2 + ">"
            list_3.append(join_item)
        
        print(list_3)
        sentence = ' '.join(list_3)
        print(sentence)

        obj=Dataset.objects.get(id=id)
        obj.tagged_sentence=sentence
        obj.is_tagged=True
        obj.save()
        all_data = Dataset.objects.get(pk=id)
        return render(request,'Results/verifer1_result.html',{'sentence':all_data})

        # test = sentence_test(text)
    return render(request,'update_verifier1.html',{'ver':ver,'words':words})
    # return render(request,"404error.html",)


def edit_tagged_sentences(request,id):
    ver = Dataset.objects.get(id=id)
    words = ver.raw_sentence.split()

    if request.method == 'POST':
    
        selected_words = request.POST.getlist('word')
        tags = request.POST.getlist('tag')
      
        # storing previously tagged word list in a new a new variable      
        previous_tagged_sentence = ' '.join(selected_words)
        # print("Tagged Data",previous_tagged_sentence)

        # Untagging the sentence
        untagging_sentence = sentence_form(previous_tagged_sentence)
        # print("Untagged Data",untagging_sentence)
        
        # Store the untagged word in a list
        selected_words = untagging_sentence.split()

        list_3 = []

        for i in range(len(selected_words)):
            item_1 = selected_words[i]
            item_2 = tags[i].upper()
            join_item =  item_1+ '\\' + item_2
            # join_item =  item_1+ '<' + item_2 + ">"
            list_3.append(join_item)
        
        print(list_3)
        sentence = ' '.join(list_3)
        print(sentence)
        # sentence = sentence_form(sentence)
        # print(sentence)

        obj=Dataset.objects.get(id=id)
        obj.verified_sentence = sentence
        obj.is_verified = True
        obj.save()
        # return HttpResponse("Verify ")
        all_data = Dataset.objects.get(pk=id)
        return render(request,'Results/verifer2_result.html',{'sentence':all_data})

        # test = sentence_test(text)
    # return render(request,'update_verifier1.html',{'ver':ver,'words':words})
    return HttpResponse("Fail ")


def tagged_admin(request):
    ver_list = check_verifier2()

    if request.user in ver_list:
        obj = Dataset.objects.filter(is_verified = False, is_default_tagged=True,is_tagged = False)
        p = Paginator(obj,10)
        page = request.GET.get('page')
        venues = p.get_page(page)

        if len(obj) == 0:
            return render(request,"clear.html")

        return render(request,"validator2.html",{'outputs':obj,'venues':venues})
    
    return render(request,"404error.html",)



def tagged_user(request):
    ver_list = check_verifier2()

    if request.user in ver_list:
        obj = Dataset.objects.filter(is_verified = False, is_tagged=True)
        p = Paginator(obj,10)
        page = request.GET.get('page')
        venues = p.get_page(page)

        if len(obj) == 0:
            return render(request,"clear.html")

        return render(request,"validator2.html",{'outputs':obj,'venues':venues})
    
    return render(request,"404error.html",)


def list_verified_sentences(request):
    obj = Dataset.objects.filter(is_verified = True).order_by('?')
    p = Paginator(obj,10)
    page = request.GET.get('page')
    venues = p.get_page(page)
    
    return render(request,"validator3.html",{'outputs':obj,'venues':venues})

def export_to_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=sentences.csv'

    writer = csv.writer(response)

    # import dataset model
    sentences = Dataset.objects.filter(is_verified = True)

    # add column headings
    writer.writerow(['Raw Sentences','Tagged Sentences'])
    filelds = sentences.values_list('raw_sentence','verified_sentence')
    
    for item in filelds:
        writer.writerow(item)
    return response


def export_to_text(request):
    # Create a BytesIO object to hold the zip file in memory
    buffer = BytesIO()
    
    data = Dataset.objects.filter(is_verified = True)

    file1 = ["Raw Sentences :\n"]
    
    for value in data:
        file1.append(f'{value.raw_sentence}\n')
    file1 = ''.join(file1)


    file2 = ["Tagged Sentences :\n"]
    
    for value in data:
        file2.append(f'{value.verified_sentence}\n')
    file2 = ''.join(file2)


    # Create the zip file
    with zipfile.ZipFile(buffer, 'w') as zip_file:
        # Add the first text file to the zip
        zip_file.writestr('Raw_Sentences.txt', file1)
        # Add the second text file to the zip
        zip_file.writestr('Tagged_Sentences.txt', file2)

    # Seek to the beginning of the buffer
    buffer.seek(0)
    
    # Create a response object with the appropriate content type and headers
    response = HttpResponse(buffer, content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename="files.zip"'

    return response

def batch_text_download(request):
    if request.method == "POST":
        metadata_id = request.POST['metadata']
        metadata = MetaData.objects.get(pk=metadata_id)
        print(metadata_id,metadata)
        action = request.POST['action']

        data = Dataset.objects.filter(is_verified = True,metadata=metadata)
        if action == "text":
            # Create a BytesIO object to hold the zip file in memory
            buffer = BytesIO()
            

            file1 = []
            
            for value in data:
                file1.append(f'{value.raw_sentence}\n')
            file1 = ''.join(file1)


            file2 = []
            
            for value in data:
                file2.append(f'{value.verified_sentence}\n')
            file2 = ''.join(file2)

            # Create the zip file
            with zipfile.ZipFile(buffer, 'w') as zip_file:
                # Add the first text file to the zip
                zip_file.writestr('Raw_Sentences.txt', file1)
                # Add the second text file to the zip
                zip_file.writestr('Tagged_Sentences.txt', file2)

            # Seek to the beginning of the buffer
            buffer.seek(0)
            
            # Create a response object with the appropriate content type and headers
            response = HttpResponse(buffer, content_type='application/zip')
            response['Content-Disposition'] = 'attachment; filename="files.zip"'

            return response
        
        elif action == "csv":
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename=sentences.csv'

            writer = csv.writer(response)

            # import dataset model
            # sentences = Dataset.objects.filter(is_verified = True)

            # add column headings
            writer.writerow(['Raw Sentences','Tagged Sentences'])
            filelds = data.values_list('raw_sentence','verified_sentence')
            
            for item in filelds:
                writer.writerow(item)
            return response


    metadata = MetaData.objects.all()
    return render(request,"batch_download/text_download.html",{'metadatas':metadata})