from django.shortcuts import render
from django.http import HttpResponse
from .forms import Target_CHOICES, mainform, Public_CHOICES
from decimal import *
from scraping import note_compettivite,note_site
import os
import json
from .models import cache, Site

def sauvegarder_cache_recherche(a):
    with open('cache.json', 'r') as fp:
        data = json.load(fp)

    if a not in data.keys():
        data[a]= note_compettivite(a)   
        with open('cache.json', 'w') as fp:
            json.dump(data, fp)

    return data[a]

def sauvegarder_base_recherche(a):

    cache_supposé = cache.objects.filter(Activité=a)
    if cache_supposé.exists() :
        return cache_supposé[0].Competitivité
    else : 
        new_enregistrement = cache(Activité = a, Competitivité= note_compettivite(a))
        new_enregistrement.save()
        return new_enregistrement.Competitivité

def sauvegarder_base_recherche2(nomSite):

    Site_supposé = Site.objects.filter(nomSite=nomSite)
    if Site_supposé.exists() :
        print("yayx")
        return [Site_supposé[0].NoteGlobal,Site_supposé[0].Note_meta,Site_supposé[0].Note_page_quality,Site_supposé[0].Note_page_structure,Site_supposé[0].Note_link_structure,Site_supposé[0].Note_Server,Site_supposé[0].Note_Social]
      
    else :
        try:
                pour_site = note_site(nomSite)
         
        except:
                pour_site = [0,0,0,0,0,0,0]

        new_enregistrement = Site(nomSite = nomSite, NoteGlobal = pour_site[0], Note_meta = pour_site[1], Note_page_quality = pour_site[2],Note_page_structure=pour_site[3],Note_link_structure = pour_site[4], Note_Server = pour_site[5],Note_Social=pour_site[6] )
        new_enregistrement.save()
        return pour_site



def home(request):
    form = mainform()
    context = {
                'form': form,
            }
    return render(request,'home-page.html',context)

def cal_fin_indice(ca, inv, md, fluc):

    if(inv==0):
         r = 1
    else:
        r = ca/inv
        d= md/inv
    
    s = 1/(d*fluc*10)


    if(s>1): s=1 

    i = (1.3*r+0.7*s)/2

    return  [i,s,r]


def results(request):
    
    if len(request.POST) > 0:
        form = mainform(request.POST)
        if form.is_valid():

            a = form.cleaned_data["nom_entr"]
            Activité = form.cleaned_data["Activité"]
            CA = float(form.cleaned_data["CA"])
            M_inve = float(form.cleaned_data["M_inve"])
            M_dette = float(form.cleaned_data["M_dette"])
            fluctuation = float(form.cleaned_data["fluctuation"])
            nom_site = form.cleaned_data["nom_site"]
            Systeme= float(form.cleaned_data["Systeme"])
            target=  int(form.cleaned_data["Target"])
            budget_pub = float(form.cleaned_data["budget_pub"])
            
            
            
            
           
            # indice financier
            liste_donné_finacier = cal_fin_indice(CA,M_inve,M_dette,fluctuation)
            pour_finance = liste_donné_finacier[0]        
            if(pour_finance>1): pour_finance=1 
            
            message_finacier_1 = ["Votre stabilité est trop basse","Votre stabilité est bonne"]
        
            message_finacier_2 = ["Votre rentabilité est trop basse","Votre rentabilité est bonne"]

            summary = ["Tout votre business plan est a refaire","Pensez a reinvestire dans la reduction de vos dettes","Pensez a prendre plus de risque","Bravo! Vous êtes sur la bonne voie"]

            msgf_f = summary[3]
            if(liste_donné_finacier[1]*100>=40): msgf_1 = message_finacier_1[1]
            else :  
                msgf_1 = message_finacier_1[0]
                msgf_f = summary[1]

            if(liste_donné_finacier[2]*100>=40): msgf_2 = message_finacier_2[1]
            else :  
                msgf_2 = message_finacier_2[0]
                msgf_f = summary[2]

          
            if(pour_finance*100<35):msgf_f = summary[0]


            # indice site
        
            pour_site = sauvegarder_base_recherche2(nom_site)
         
         
      
            # indice marketing
                # 1ere partie 50
            try:
              
                competitivité = sauvegarder_base_recherche(Activité)
            except:
                competitivité = 0
            
            if(competitivité>30): gold = "haute"
            else: gold= "basse"
            
            msg_mm = "Votre Targeting ("+ str(Public_CHOICES[target-1][1]) +")" + " ne convient pas a la competitivié " + gold +"."
            
            msg_mb = "Votre Targeting ("+ str(Public_CHOICES[target-1][1]) +")" + " convient bien a la competitivié " + gold +"."
            
            if(competitivité>=30 and target == 1):
                ind_targ_comp = 0
            elif(competitivité>=30 and target == 2):
                ind_targ_comp = 50
            elif(competitivité<30 and target == 1):
                ind_targ_comp = 50
            elif(competitivité<30 and target == 2):
                ind_targ_comp = 0
                # 2ere partie 50
            print(Systeme,budget_pub)
            indi1 = 50 - abs(Systeme - budget_pub) 
            print(ind_targ_comp)

            if(ind_targ_comp==0): msg_f=msg_mm
            else: msg_f=msg_mb
            
            msg_ratio1= "Votre budget pub est de: "+ str(budget_pub) +"%\n" + "L'ideal selon votre systeme de clientèle est: " + str(Systeme) + "%"
            ind_mark_final = indi1 + ind_targ_comp

        else :
            print(form.errors)

    context = {
        "pour_finance" : pour_finance*100,
        "com_pour_finance" : 100- pour_finance*100,

        "msgf_1": msgf_1,
        "msgf_2":  msgf_2,
        "msgf_f": msgf_f,

        "pour_site" : pour_site[0],
        "com_pour_site" : 100 - pour_site[0],

        "nom_site" : nom_site +"",
        "page_quality" : pour_site[2],
        "page_structure" : pour_site[3],
        "link_structure" : pour_site[4],
        "Server_configuration" : pour_site[5],
        "reseau_sociaux": pour_site[6],
        
        "msg_m" : msg_f,
        "msg_ratio1": msg_ratio1,

        "ind_mark_final" : ind_mark_final,
        "com_ind_mark_final" : 100 - ind_mark_final,

        'form': mainform(),
    }
    return render(request,'results.html',context)
