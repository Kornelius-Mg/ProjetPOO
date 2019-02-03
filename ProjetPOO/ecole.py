#!/usr/bin/python3
# -*- encoding : utf8 -*-
from autres import *

class Ecole:
    def __init__(self,nom="",promotions={},administrateurs={},enseignants={},ouvriers={},parents={}):
        self.nomEcole = nom
        self.__promotions = promotions
        self.__admins = administrateurs
        self.__enseignants = enseignants
        self.__ouvriers = ouvriers
        self.__parents = parents
        self.__caisse = 0

    # Methodes d'acces à promotion
    def getPromotions(self):
        return self.__promotions
    
    #Autres methodes
    def listeEleves(self):
        liste = (self.__promotions).values()
        listeEl = list()
        for promotion in liste:
            listeEl+=promotion.ListeEleves()
        return listeEl
    
    def listePromotions(self):
        return self.__promotions.values()

   ##########################################################################     
    #MEMBRES DE L'ADMINISTRATION
    # Methodes d'acces aux membres de l'administration
    def getAdmins(self):
        return self.__admins

    def setAdmins(self,val):
        if not isinstance(val,dict):
            raise(TypeError,"Erreur : LA valeur doite etre un dictionnaire")
        self.__admins = val

    #Enregistrement des membres de l'administration
    def enreg_secretaire(self,secretaire):
        if not isinstance(secretaire,Secretaire):
            raise(TypeError,"L'argument doit etre de type Secretaire")
        self.__admins["secretaire"] = secretaire
    
    def enreg_directeur(self,directeur):
        if not isinstance(directeur,Directeur):
            raise(TypeError,"L'argument doit etre de type Directeur")
        self.__admins["directeur"] = directeur
    
    def enreg_comptable(self,comptable):
        if not isinstance(comptable,Comptable):
            raise(TypeError,"L'argument doit etre de type Comptable")
        self.__admins["comptable"] = comptable

    #supprimer les membres de l'administration
    def del_secretaire(self):
        del(self.__admins["secretaire"])
    
    def del_directeur(self):
        del(self.__admins["directeur"])
    
    def del_comptable(self):
        del(self.__admins["comptable"])
    
########################################################################
    #ENSEIGNANTS
    # Methodes d'acces aux enseignants
    def getEnseignants(self):
        return self.__enseignants

    def setEnseignants(self,val):
        if not isinstance(val,dict):
            raise(TypeError,"Error : La valeur doit etre un dictionnaire")
        self.__enseignants = val

    #Enregistrer un enseignant
    def enreg_enseignant(self,ens):
        if not isinstance(ens,Enseignant):
            raise(TypeError,"L'argument doit etre de type enseignant")
        self.__enseignants[ens.codeEns] = ens
    
    #Supprimer un enseignant
    def del_enseignant(self,code):
        del(self.__enseignants[code])
    
##############################################################################
    #OUVRIERS
    # Methodes d'acces aux ouvriers
    def getOuvrier(self):
        return self.__ouvriers

    def setOuvrier(self,val):
        if not isinstance(val,dict):
            raise(TypeError,"Error : La valeur doit etre un dictionnaire")
        self.__ouvriers = val

    #Enregistrer un ouvrier
    def enreg_ouvrier(self,ouvrier):
        if not isinstance(ouvrier,Ouvrier):
            raise(TypeError,"L'argument doit etre de type Ouvrier")
        self.__ouvriers[ouvrier.code] = ouvrier

    #Supprimer un ouvrier
    def del_ouvrier(self,code):
        del(self.__ouvriers[code])

#############################################################################
    #PARENTS
    # Methodes d'acces aux parents des eleves
    def getParents(self):
        return self.__parents
        
    def setParents(self,val):
        if not isinstance(val,dict):
          raise(TypeError,"Error : La valeur doit etre un dictionnaire")
        self.__parents = val
        
    #Enregistrer un parent
    def enreg_parent(self,parent):
        if not isinstance(parent,Parent):
            raise(TypeError,"L'argument doit etre de type parent")
        self.__parents[parent.code] = parent
    
    #Supprimer un parent
    def del_parent(self,code):
        del(self.__parents[code])

    #generer code du parent
    def code(self,parent):
        pass

    ############################################################################"
    #CAISSE
    def getCaisse(self):
        return self.__caisse
    def setCaisse(self,val):
        try:
            val =float(val)
        except Exception as erreur:
            print("Erreur : %s"%erreur)
        else:
            self.__caisse = val
        
    def incr_caisse(self,val):
        try:
            val =float(val)
        except Exception as erreur:
            print("Erreur : %s"%erreur)
        else:
            self.__caisse += val
    
    def decr_caiss(self,val):
        try:
            val = float(val)
        except Exception as erreur:
            print("Erreur : %s"%erreur)
        else:
            self.__caisse -= val



    

    



    
    


        
