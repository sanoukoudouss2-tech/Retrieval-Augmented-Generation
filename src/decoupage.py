import spacy





def coupure(text, nbre, chevauchement,nlp):

    """
        Cette fonction permet de decouper un texte en tokens (nlp de spacy). On choisit le nombre de tokens
        que contiendra chaque chunk et aussi la longueur de superposition entre chunks.

        On découpe également le texte de facon sématique.(je pense a faire une deuxieme fonction pour celle la).
        A la sortie on obtient deux lots de chunks. Un suite a un découpage de tokens et un autre dû à un découpage sémentique
        
        Pour le découpage sémantique on choisit en parametre le modele utilisé pour l'embedding

    
    """

    tokens = nlp(text)
    chunks_token = []
    pas = nbre - chevauchement
    for i in range(0, len(tokens), pas):
        chunk = tokens[i:i + nbre]
        if chunk:
            chunks_token.append(chunk)
            
        if i + nbre >= len(tokens):
            break

    token_text = [token.text for token in chunks_token]
    dict_chunks_token = dict(enumerate(token_text))

    
    # tokens.sents contient les phrases de mon texte
    # .text recupere le texte et strip() supprime les espaces inutiles
    
    return dict_chunks_token



