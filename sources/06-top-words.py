# On veut obtenir la fréquence de chaque mot

def get_freq(nom_fich):
    fich=open(nom_fich)
    contenu=fich.read()
    liste_frag=contenu.split() # coupe sur 'espace' et \
    liste_mot=list()
    for fragment in liste_frag: 
        fragment_min=fragment.lower()
        frag_clean=clean(fragment_min)
        liste_mot.append(frag_clean)
        
    
    return liste_mot
        
def clean(fragment):
    
    result=""
    for c in fragment:
        if c.isalpha():
            result+=c
    
    return result
    
    
        
def tri(d):
    list_tuples=list()
    for clé, valeur in d.items():
        list_tuples.append((valeur, clé))
    list_tuples.sort(reverse=True)
    print(list_tuples)
    return d

nom_fich="ruffin.txt"
f=get_freq(nom_fich)
print(f)




