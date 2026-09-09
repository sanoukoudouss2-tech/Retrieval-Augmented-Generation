def contexte(indices,chunks):
    """ Cette fonction recoit les indices et la liste de mots coupés auparavant 
    et renvoie la liste des mots avec les indices correspondants
    
    """
    ctxte = []
    for i in indices:
        ctxte.append(chunks[i])

    return ctxte