def prompt(question,chunks):
    A = {"role":"system","content":"tu reponds uniquement à partir du contexte fourni. Si le contexte est insuffisant, dis le clairement"}
    B= {"role":"user","content": f""" Contexte : {chunks} \n Question : {question}"""}
    return [A,B]