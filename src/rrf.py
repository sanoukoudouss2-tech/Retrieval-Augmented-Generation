def rrf(liste_bm25,liste_embeddings,k=60):

    """
    rrf permet de calculer un score qui est un compromis entre le sens et le lexique. 
    En effet, par BM25 et par FAISS on retrieve les chunks pertinents. D'une part BM25 nous rapporte les chunks
    proches de notre question en terme de lexique(mots ou expressions identiques). Et d'autre part FAISS 
    nous retourne les chunks proches de notre question en terme de sens. Et un score est calculé en fonction
    du rang d'un chunk dans les des deux listes (semantiques et lexicales)
    
    """


    scores_fusion = {}
    for rang,idx in enumerate(liste_bm25):
        scores_fusion[idx] = scores_fusion.get(idx,0)+ 1/(k + rang +1)

    for rang,idx in enumerate(liste_embeddings):
        scores_fusion[idx] = scores_fusion.get(idx,0)+ 1/(k + rang +1)

    classement = sorted(scores_fusion.items(),key=lambda x: x[1],reverse=True)

    return [idx for idx,score in classement]