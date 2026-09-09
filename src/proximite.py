from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from src.vectorisation import vectorisation
def proximite(question,base):
    """
    Cette fonction calcule la similarité entre l'embedding de la question et l'enbedding de mes chunks 
    et me retourne les indices dont le sens des embeddings du documents sont plus proches de la question
    """
    question = vectorisation([question])
    similarite = cosine_similarity(question,base)
    similarite = similarite[0]                    
    indices = np.argsort(similarite)[-4:][::-1]    
    

    return indices