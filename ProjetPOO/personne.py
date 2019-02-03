class Personne:
    __numPer = 0
    def __init__(self,nom="",post="",prenom="",age=0,adresse=""):
        Personne.__numPer += 1
        self.num_personne = Personne.__numPer
        self.nom = nom
        self.postnom = post
        self.prenom = prenom
        self.age = age
        self.adresse = adresse
        assert(self.__class__ is not Personne)
        
    def getNomComplet(self):
        return self.nom+" "+self.postnom+" "+self.prenom

class Eleve(Personne):
    __numEl = 0
    def __init__(self,nom,post,prenom,age,adresse,lieu_naiss,date_naiss,parent):
        Personne.__init__(self,nom,post,prenom,age,adresse)
        Eleve.__numEl += 1
        self.num_eleve = Eleve.__numEl
        self.lieu_naiss = lieu_naiss
        self.date_naiss = date_naiss
        self.parent = parent
        
class Parent(Personne):
    __numPar = 0
    def __init__(self,nom,post,prenom,age,adresse,profession):
        Personne.__init__(self,nom,post,prenom,age,adresse)
        Parent.__numPar += 1
        self.numero = Personne.__num
        self.profession = profession

class Personnel(Personne):
    __numPers = 0
    def __init__(self,nom,post,prenom,age,adresse,salaire):
        Personne.__init__(self,nom,post,prenom,age,adresse)
        Personnel.__numPers += 1
        self.num_pers = Personnel.__numPers
        self.salaire = salaire
        assert(self.__class__ is not Personnel)

class Enseignant(Personnel):
    def __init__(self,nom,post,prenom,age,adresse,salaire):
        Personnel.__init__(self,nom,post,prenom,age,adresse,salaire)
    def creer_seance(self,cours,promotion):
        pass
    def annuler_seance(self,seance):
        pass

class Ouvrier(Personnel):
    def __init__(self,nom,post,prenom,age,adresse,salaire):
        Personnel.__init__(self,nom,post,prenom,age,adresse,salaire)
        self.num_ouv = Ouvrier.__numOuv

class Directeur(Personnel):
    def __init__(self,nom,post,prenom,age,adresse,salaire):
        Personnel.__init__(self,nom,post,prenom,age,adresse,salaire)
    

class Comptable(Personnel):
    def __init__(self,nom,post,prenom,age,adresse,salaire):
        Personnel.__init__(self,nom,post,prenom,age,adresse,salaire)
    