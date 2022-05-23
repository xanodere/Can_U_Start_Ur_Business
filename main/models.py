from django.db import models

class cache(models.Model):

    Activité = models.CharField(max_length=500)
    Competitivité = models.IntegerField()

class Site(models.Model):

    #  en ordre [total, meta inf, page quality, page structure, link structure, Server, facteurs externe] 
   
    nomSite = models.CharField(max_length=500)
    NoteGlobal = models.IntegerField()
    Note_meta = models.IntegerField()
    Note_page_quality = models.IntegerField()
    Note_page_structure = models.IntegerField()
    Note_link_structure = models.IntegerField()
    Note_Server = models.IntegerField()
    Note_Social = models.IntegerField()

    def __str__(self):
        return self.nomSite