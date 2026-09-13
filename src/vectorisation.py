
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("all-MiniLM-L6-v2")
import faiss

def vectorisation(chunks,model_embedding):
    """
    Cette fonction recoit la liste des mots decoupés et retourne une matrice des embeddings des mots correspondants
    """
    base = model_embedding.encode(chunks).astype("float32")
    faiss.normalize_L2(base)

    return base