# Pour chaque élément de l'argument liste :
# - si le nombre de caractère vaut 1 : ajoute le caractère '0' devant la valeur
# - sinon ne fait rien
# Renvoie ensuite la liste modifiée
def r(liste):
    return [texte if len(texte) == 2 else '0'+texte for texte in liste]
