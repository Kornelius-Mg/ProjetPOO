#!/usr/bin/python3
# -*- encoding : utf8 -*-

from personne import *

# Classe cours 
class Cours:
    def __init__(self,acro,intitule):
        assert(isinstance(acro,str) and len(acro)<7)
        assert(isinstance(intitule,str))
        self.__acro = acro 
        self.__intitule = intitule
        
    # Methodes d'acces à acronyme
    def getAcro(self):
        return self.__acro
    def setAcro(self,val):
        assert(isinstance(val,str) and len(val)<7)
        self.__acro = val

    # Methodes d'acces à Intitule
    def getIntitule(self):
        return self.__intitule
    def setIntitule(self,val):
        assert(isinstance(val,str))
        self.__intitule = val
    
    
class Classe:
    def __init__(self,nom):
        self.__nom = nom
        self.__enseignant = enseignant
        self.__eleves = {}
    
    # Methodes d'acces au nom de la classe
    def getNom(self):
        return self.__nom
    def setNom(self,val):
        self.__nom = val

    # Methodes d'acces à enseignant
    def getEnseignant(self):
        return self.__enseignant
    def setEnseignant(self,val):
        self.__enseignant = val
    def getNomsEnseignant(self):
        return self.__enseignant.getNomComplet()
        
    # Methode d'acces au dictionnaire des eleves
    def getEleves(self):
        return self.__eleves
    def setEleves(self,val):
        if not isinstance(val,dict):
            raise(TypeError,"La valeur doit etre un dictionnaire")
    def getListeEleves(self):
        return self.getEleves().values()

    # Methode de creation du matricule d'un eleve
    def create_matricule(self,eleve):
        nom = (eleve.nom)[0]
        post = (eleve.postnom)[0]
        nb = len(self.__eleves) + 1
        number = ""
        for i in range(3-len(nb)):
            number+="0"
        return nom+post+number+nb
        
    # Ajouter un eleve dans la classe
    def enreg_eleve(self,eleve):
        if not isinstance(eleve,Eleve):
            raise(TypeError,"L'argument doite etre une instance de type Eleve")
        matricule = self.create_matricule(eleve)
        (self.__eleves)[matricule]=eleve
    
    # Supprimer un eleve d'une classe
    def del_eleve(self,mat):
        del((self.__eleves)[mat])
    
    # Autres methodes
    def getNombreEleves(self):
        return len(self.__eleves)


class Promotion:
    def __init__(self,niveau):
        if not isinstance(val,int):
            raise(TypeError,"L'argument doit etre de type entier")
        elif not val in range(1,7):
            raise(ValueError,"Le niveau doit être compris entre 1 et 6")
        self.__niveau = niveau
        self.__classes = {}
        self.__cours = {}
    
    # Methodes d'acces à niveau
    def getNiveau(self):
        return self.__niveau

    def setNiveau(self,val):
        if not isinstance(val,int):
            raise(TypeError,"L'argument doit etre de type entier")
        elif not val in range(1,7):
            raise(ValueError,"Le niveau doit être compris entre 1 et 6")
        else:
            self.__niveau = val
    
    # Methodes d'acces aux classes
    def getClasses(self):
        return self.__classes

    def setClasse(self,val):
        if not isinstance(val,dict):
            raise(ValueError,"L'argument doit etre un dictionnaire qui contient les classes")
        self.__classes = val

    def getNomClasse(self,classe):
        return str(self.getNiveau())+str(classe.getNom())

    def enreg_classe(self,classe):
        assert(instance(classe,Classe))
        mat = classe.getNomClasse()
        (self.__classes)[mat] = classe
    def del_classe(self,cle):
        del((self.__classes)[cle])
    
    # Methodes d'acces à cours
    def getCours(self):
        return self.__cours

    def setCours(self,val):
        if not isinstance(val,dict):
            raise(TypeError,"L'argument doit etre un dictionnaire contenant les cours.")
        self.__cours = val
    def enreg_cours(self,cours):
        if not isinstance(cours,Cours):
            raise(TypeError,"L'argument doit etre un objet de type cours")
        (self.__cours)[cours.acro] = cours
    
    #Autres methodes
    def  getNombreCours(self):
        return len(self.__cours)

    def getNombreClasses(self):
        return len(self.__classes)

    def ListeClasses(self):
        return self.getClasses().values()

    def listeEleves(self):
        liste = self.getClasses().values()
        listeEl = list()
        for classe in liste:
            listeEl+=classe.getListeEleves()
        return listeEl

    def listeEnseignants(self):
        liste = self.getClasses()
        return liste.values()
    
    def listeCours(self):
        liste = self.getCours()
        return liste.values()

        


 
        
        
