import fitz
def extraction(chemin):

    """ Cette fonction permet à partir du chemin d'un document pdf renseigné de le parcourir 
    et d'en extraire chaque texte de page dans un format texte unique qui sera utilisé par la suite pour être découpé
    """
    doc = fitz.open(chemin)
    ## doc est un type qui contient toutes les informations du pdf
    ## doc est un regroupement de toutes les pages. Mais chaque page contient toutes ses informations, pas seulement du texte
    texte = ""
    for page in doc :
        texte +=page.get_text()

    return texte