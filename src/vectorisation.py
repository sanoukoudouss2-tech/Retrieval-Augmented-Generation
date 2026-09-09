
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("all-MiniLM-L6-v2")


def vectorisation(chunks):
    """
    Cette fonction recoit la liste des mots decoupés et retourne une matrice des embeddings des mots correspondants
    """
    base = model.encode(chunks)
    return base