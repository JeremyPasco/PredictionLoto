# Convertir chaque élément du paramètre liste en integer de caractères et renvoyer la liste modifiée
def o(liste):
    try :
        liste = [int(i) for i in liste]
        return liste
    except :
        print("Problème avec la liste")
