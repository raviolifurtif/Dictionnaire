# -*-coding: utf-8 -*

import os
import math
from operator import itemgetter

dico_test={"cle_1":31,"cle_2":12,"souris":1,"absurde":1000}

class DicoOrdonne:

    """On construit le dictionnaire ordonné à partir des données
    fournies par l'utilisateur : soit rien, soit un dictionnaire existant,
    soit de nouvelles données entrées directement par l'utilisateur
    """
    def __init__(self, *dico_envoye, **nouvelles_donnees):
        self.liste_cles=[]
        self.liste_valeurs=[]
        dico_envoye=list(dico_envoye)
        if dico_envoye == [] and nouvelles_donnees == {}: #Si aucune variable n'est passée, le dictionnaire sera vide
            print("Votre objet est créé. Il est vide pour le moment")
        elif nouvelles_donnees == {}: #Si on entre un dictionnaire existant, la variable nouvelles_données est vide
            try :
                dico_envoye=dico_envoye[0]
                self.liste_cles=list(dico_envoye.keys())
                self.liste_valeurs=list(dico_envoye.values())
                print("Votre objet a été créé avec succès à partir du dictionnaire proposé")
            except AttributeError:
                print("L'objet proposé n'est pas un dictionnaire existant !")
            except TypeError:
                print("L'objet proposé n'est pas un dictionnaire existant !")

        elif dico_envoye == [] and nouvelles_donnees != {}:
            self.liste_cles=[]
            self.liste_valeurs=[]
            for elt in nouvelles_donnees.keys():
                if elt in self.liste_cles:
                    raise ValueError("Vous avez rentré la clé {} plusieurs fois !".format(elt))
                else:
                    self.liste_cles.append(elt)
            for valeur in nouvelles_donnees.values():
                try :
                    valeur=float(valeur)
                except ValueError:
                    print("Info : La valeur saisie ({}) n'est pas un nombre.".format(valeur))
                self.liste_valeurs.append(valeur)
            print("Votre objet a été créé avec succès à partir des données proposées")


    """La fonction print renverra un dictionnaire classique
    """
    def __repr__(self):
        if self.liste_cles==[]:
            chaine_a_montrer="{}"
        else:
            chaine_a_montrer="{"+str(self.liste_cles[0])+": "+str(self.liste_valeurs[0])
            for i in range(1,len(self.liste_cles)):
                chaine_a_montrer=chaine_a_montrer+", "+str(self.liste_cles[i])+": "+str(self.liste_valeurs[i])
            chaine_a_montrer=chaine_a_montrer+"}"
        return chaine_a_montrer
    
    
    
    """Appeler une clé renverra la valeur correspondante à cette clé
    """
    def __getitem__(self,index):
        if index not in self.liste_cles:
            return "La clé {} n'est pas présente dans le dictionnaire !".format(index)
        else:
            i=0
            while self.liste_cles[i] != index:
                i += 1
            return self.liste_valeurs[i]

            
            
    """Méthode permettant de changer la valeur correspondant à une clé
    (le tout étant ajouté au dictionnaire si la clé n'est pas déjà présente
    """
    
    def __setitem__(self,index, valeur):
        if index in self.liste_cles:
            i=0
            while self.liste_cles[i] != index:
                i += 1
            self.liste_valeurs[i] = valeur
            print("La valeur associée à la clé {} est maintenant : {}.".format(index,valeur))
        else:
            self.liste_cles.append(index)
            self.liste_valeurs.append(valeur)
            print("La clé {} a été ajoutée au dictionnaire avec la valeur {}.".format(index,valeur))

            
            
            
    """Supprime la clé précisée et la valeur correspondante
    """
    
    def __delitem__(self,index):
        if index not in self.liste_cles:
            print("La clé à supprimer n'est pas présente dans le dictionnaire !")
        else:
            i=0
            while self.liste_cles[i] != index:
                i += 1
            del self.liste_cles[i]
            del self.liste_valeurs[i]
            print("La clé {} et la valeur correspondante ont été supprimées avec succès !".format(index))

            
            
    """Renvoie "True" si la clé est dans le dictionnaire, "False" sinon
    """
    
    def __contains__(self,index):
        if index in self.liste_cles:
            return True
        else:
            return False

            
            
    """Renvoie le nombre de clés du dictionnaire"""
    
    def __len__(self):
        return len(self.liste_cles)
    
    
    
    """Permet de trier les clés par ordre alphabétique (les objets suivent)
    """
    
    def sort(self):
        liste_tri=[]
        for i in range(len(self.liste_cles)):
            liste_tri.append((self.liste_cles[i],self.liste_valeurs[i]))
        liste_tri=sorted(liste_tri, key=itemgetter(0))
        for i in range(len(liste_tri)):
            self.liste_cles[i]=liste_tri[i][0]
            self.liste_valeurs[i]=liste_tri[i][1]

    
    """Inverse l'ordre des clés
    """
    
    def reverse(self):
        self.liste_cles.reverse()
        self.liste_valeurs.reverse()
        
        
        
    """Rend le parcours des clés du dictionnaire possible
    """
    
    def __iter__(self):
        return iter(self.liste_cles)
        
    
    
    """Renvoie un générateur de la liste des clés
    """
    
    def keys(self):
        for elt in self.liste_cles:
            yield elt
    
    
    
    """Renvoie un générateur de la liste des valeurs
    """
    
    def values(self):
        for elt in self.liste_valeurs:
            yield elt
            
    
    
    """Renvoie un générateur des couples (clé,valeur)
    """
    
    def items(self):
        for i in range(len(self.liste_cles)):
            yield (self.liste_cles[i],self.liste_valeurs[i])
    
    
    """Ajoute un dictionnaire à un autre
    """
    
    def __add__(self,dico_2):
        if type(dico_2) != DicoOrdonne:
            raise TypeError("Il faut ajouter un objet de type dictionnaire ordonné !")
        else:
            for elt in dico_2.liste_cles:
                self.liste_cles.append(elt)
            for elt in dico_2.liste_valeurs:
                self.liste_valeurs.append(elt)
        return self
        
    
test=DicoOrdonne(dico_test)
print(test["cle"])
print(test["cle_1"])

       


os.system("pause")
