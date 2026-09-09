import fitz
def extraction(chemin):
    doc = fitz.open(chemin)
    ## doc est un type qui contient toutes les informations du pdf
    ## doc est un regroupement de toutes les pages. Mais chaque page contient toutes ses informations, pas seulement du texte
    texte = ""
    for page in doc :
        texte +=page.get_text()

    return texte