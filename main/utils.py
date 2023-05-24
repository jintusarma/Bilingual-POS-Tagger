import re
from .models import *
from accounts.models import *

def check_verifier1():
    ver = Verifier.objects.filter(verifier_type = 'verfier_1')

    # create an blank list so that we store the values in the list
    ver_list =[]
    
    # Since ver retuen a query , so we create a loop and added the users in ver_list 
    for x in ver:
        ver_list.append(x.verifier)
    
    return ver_list
    

def check_verifier2():
    ver = Verifier.objects.filter(verifier_type = 'verfier_2')
    ver_list =[]
    
    for x in ver:
        ver_list.append(x.verifier)

    return ver_list


def check_verifier_admin():
    ver = Verifier.objects.filter(verifier_type = 'admin')

    ver_list =[]
    
    for x in ver:
        ver_list.append(x.verifier)

    return ver_list


def list_to_word(list):
    for i in len(list):
        sentence = list[i]+sentence
        return sentence
    

def sentence_form(sentence):
    sentence = sentence.split(" ")
    new_list = []
    new_list2 = []

    for word in sentence:
        words_1 = re.sub(r'\[+\w+\]+', '', word)
        words_2 = re.sub(r'[^\w\s]', '', words_1)
        if words_2 == '':
            pass
        else:
            new_list.append(words_2)

    for input_str in new_list:
        normal_text = re.sub(r'[A-Z_]+', ' ', input_str)
        normal_text = re.sub(r'\s+', ' ', normal_text)
        normal_text = normal_text.rstrip()
        new_list2.append(normal_text)
        
        sentence = ' '.join(new_list2)

    return sentence

def assamese_sentence_form(sentence):
    clean_text = re.sub(r'\\[A-Z_]+', '', sentence)
    return clean_text