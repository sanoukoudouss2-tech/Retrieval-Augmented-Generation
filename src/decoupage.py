def coupure(text, nbre, chevauchement):
    """
    Découpe text en chunks de nbre mots, avec un chevauchement 
    de `chevauchement` mots entre chunks consécutifs.
    """
    mots = text.split() if isinstance(text, str) else text
    #split decoupe une chaine de caracteres en plusieurs mots selon un separateur et retourne le tout dans une liste"
    pas = nbre - chevauchement
    if pas <= 0:
        raise ValueError("chevauchement doit être < nbre")

    chunks = []
    for i in range(0, len(mots), pas):
        chunk = mots[i:i + nbre]
        if chunk:
            chunks.append(chunk)
        if i + nbre >= len(mots):
            break
    textes = [" ".join(c) if isinstance(c, list) else c for c in chunks]
    return textes