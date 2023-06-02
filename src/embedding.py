from openai.embeddings_utils import get_embedding
from openai.embeddings_utils import cosine_similarity
import openai
import pandas as pd
import numpy as np
import os

openai.api_key = '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'

def embed_text(path="texto.csv"):
    conocimiento_df = pd.read_csv(path)
    conocimiento_df['Embedding'] = conocimiento_df['texto'].apply(lambda x: get_embedding(x, engine='text-embedding-ada-002'))
    conocimiento_df.to_csv('./database/embeddings.csv',index=False)
    return conocimiento_df

def buscar(busqueda, datos):
    busqueda_embed = get_embedding(busqueda, engine="text-embedding-ada-002")
    datos['Embedding'] = datos['Embedding'].apply(lambda x: np.fromstring(x.strip(']['), sep=','))
    datos['Similitud'] = datos['Embedding'].apply(lambda x: cosine_similarity(x, busqueda_embed))
    filtro = datos.query('Similitud>.86')
    # return filtro.iloc[:5][["texto", "flujo", "Similitud", "Embedding"]]
    if filtro.empty:
        flow = 404
    else:
        flow = filtro.iloc[:1]['flujo'].values[0]
    return flow

# texto_emb = embed_text("./database/chatbot_qa.csv")

# conocimiento = pd.read_csv('./database/embeddings.csv')
# pregunta = 'es el 13 91 43 432'
# respuesta = buscar(pregunta, conocimiento)
# print(respuesta)

# export OPENAI_API_KEY="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"

