from sentence_transformers import CrossEncoder
def encode(question,chunks,indices,reranker,top_k=4):

    """
    Cette fonction calcule la pertinence d'un ensemble de mots. Une fois que j'obtiens mes chunks après avoir
    appliqué rrf j'obtiens un ensemble de chunks succeptibles de correspondre à la réponse de ma question.
    
    Je fais donc entrer à tour de rôle les paires {question,chunk} et je retourne à la fin les chunks dont 
    la paire {question,chunk} à un certain score de pertinence. Chunks qui seront envoyé au LLM
    
    """
    chunks_candidats = [chunks[i] for i in indices]
    paires = [[question,chunk] for chunk in chunks_candidats]
    scores = reranker.predict(paires)

    classement = sorted(zip(chunks_candidats,scores),key=lambda x : x[1],reverse=True)
    top_chunks = [chunk for chunk,score in classement[:top_k]]

    return top_chunks