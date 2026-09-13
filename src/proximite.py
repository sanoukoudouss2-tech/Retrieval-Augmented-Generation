#from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
def proximite_embedding(question_vec,index_faiss,k):
    """
    Cette fonction calcule la similarité entre l'embedding de la question et l'enbedding de mes chunks 
    et me retourne les indices dont le sens des embeddings du documents sont plus proches de la question
    """
    ## k represente les vecteurs les plus proches que je cherche a retourner

    distance,indices = index_faiss.search(question_vec,k)
 
    return distance,indices

def proximite_bm25(question,bm25,k):

    scores = bm25.get_scores(question)
    top_indices = np.argsort(scores)[-k:][::-1]
     
    return list(top_indices)