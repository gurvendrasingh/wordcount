from django.http import HttpResponse
from django.shortcuts import render
import operator
def Homepage(request):
    return render(request,"example.html")



def count(request):
    words = request.GET['fulltext']
    word = words.split()
    words_counting = len(word)

    word_dict = {}
    for k in word:
        if k in word_dict:
            word_dict[k] += 1
        else:
            word_dict[k] =1    

    sorted_dict = sorted(word_dict.items(), key = operator.itemgetter(1), reverse = True)
    
    return render(request,"count.html", {'data':words,'alp':words_counting,'worddictionary': sorted_dict})

    


   