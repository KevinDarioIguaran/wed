from django.http import HttpResponse
from django.template import  loader



def login(request): 

    ext_doc_login =  loader.get_template('login.html')
    resul = ext_doc_login.render()

    return HttpResponse(resul)

def create_account(request): 

    ext_doc_create_account =  loader.get_template('create_account.html')
    resul = ext_doc_create_account.render()

    return HttpResponse(resul)