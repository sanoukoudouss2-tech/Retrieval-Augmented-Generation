# RAG - Système de Question/Réponse sur Document PDF

Ce projet implémente un pipeline **RAG (Retrieval-Augmented Generation)** simple, construit "from scratch", permettant de poser des questions sur le contenu d'un document PDF. Le système extrait le texte, le découpe en chunks, calcule des embeddings, retrouve les passages les plus pertinents par similarité cosinus, puis génère une réponse via un LLM (Groq) en se basant uniquement sur le contexte retrouvé.

## Fonctionnement du pipeline

1. **Extraction** — Le texte est extrait du PDF page par page avec `PyMuPDF (fitz)`.
2. **Découpage** — Le texte est découpé en chunks de N mots avec un chevauchement configurable, pour préserver le contexte entre chunks.
3. **Vectorisation** — Chaque chunk est transformé en embedding avec le modèle `SentenceTransformer` (`all-MiniLM-L6-v2`).
4. **Recherche de proximité** — La question est elle aussi vectorisée, puis comparée à tous les chunks via la similarité cosinus (`scikit-learn`). Les 4 chunks les plus proches sont sélectionnés.
5. **Construction du contexte** — Les chunks sélectionnés sont récupérés à partir de leurs indices.
6. **Génération du prompt** — Un prompt système + utilisateur est construit, contraignant le modèle à répondre uniquement à partir du contexte fourni.
7. **Génération de la réponse** — Le prompt est envoyé à un LLM via l'API Groq (modèle `openai/gpt-oss-120b`), qui génère la réponse finale.

## Architecture du projet

```
mon_env/
├── src/
│   ├── __init__.py
│   ├── extraction.py      # Extraction du texte depuis un PDF
│   ├── decoupage.py        # Découpage du texte en chunks avec chevauchement
│   ├── vectorisation.py     # Génération des embeddings (SentenceTransformer)
│   ├── proximite.py        # Calcul de similarité cosinus et sélection des chunks pertinents
│   ├── contexte.py         # Reconstruction du contexte à partir des indices
│   └── prompt.py            # Construction du prompt system/user pour le LLM
├── .env                    # Variables d'environnement (clé API Groq)
├── .gitignore
├── requirements.txt
├── test.ipynb               # Notebook de démonstration
└── le_petit_prince.pdf      # Document exemple utilisé pour les tests
```


## Utilisation

Exemple d'utilisation complète (voir `test.ipynb`) :

```python
from src.extraction import extraction
from src.decoupage import coupure
from src.vectorisation import vectorisation
from src.proximite import proximite
from src.contexte import contexte
from src.prompt import prompt
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# 1. Extraction du texte
texte = extraction("./le_petit_prince.pdf")

# 2. Découpage en chunks
chunks = coupure(texte, nbre=100, chevauchement=15)

# 3. Vectorisation des chunks
base_vec = vectorisation(chunks)

# 4. Recherche des chunks pertinents pour une question
question = "Qui est le renard ?"
indices = proximite(question, base_vec)
ctxte = contexte(indices, chunks)

# 5. Construction du prompt
requete = prompt(question, ctxte)

# 6. Génération de la réponse
response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=requete
)

print(response.choices[0].message.content)
```

## Détail des modules

| Module | Fonction principale | Rôle |
|---|---|---|
| `extraction.py` | `extraction(chemin)` | Extrait le texte brut d'un PDF |
| `decoupage.py` | `coupure(text, nbre, chevauchement)` | Découpe le texte en chunks avec chevauchement |
| `vectorisation.py` | `vectorisation(chunks)` | Encode les chunks en vecteurs (embeddings) |
| `proximite.py` | `proximite(question, base)` | Trouve les chunks les plus proches sémantiquement de la question |
| `contexte.py` | `contexte(indices, chunks)` | Reconstitue le texte du contexte à partir des indices sélectionnés |
| `prompt.py` | `prompt(question, contexte)` | Construit le prompt (system + user) envoyé au LLM |

## Technologies utilisées

- **PyMuPDF (fitz)** — extraction de texte PDF
- **Sentence-Transformers** (`all-MiniLM-L6-v2`) — embeddings sémantiques
- **scikit-learn** — calcul de similarité cosinus
- **NumPy** — manipulation des vecteurs
- **Groq API** — génération de texte via LLM (`openai/gpt-oss-120b`)
- **python-dotenv** — gestion des variables d'environnement

## Améliorations possibles

- Remplacer le découpage par mots par un découpage par phrases ou par tokens
- Utiliser une base vectorielle persistante (FAISS, ChromaDB, Qdrant...) plutôt qu'un array en mémoire
- Ajouter une interface (Streamlit, Gradio) pour interagir avec le système
- Gérer plusieurs documents PDF simultanément
- Ajouter un score de confiance ou une citation des sources dans la réponse


