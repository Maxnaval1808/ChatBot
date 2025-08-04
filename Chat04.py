import spacy
from goose3 import Goose
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

g = Goose()
url = "https://pt.wikipedia.org/wiki/Guerra_Russo-Ucraniana"

noticia = g.extract(url)

nlp = spacy.load("pt_core_news_sm")
texto = [sent.text for sent in nlp(noticia.cleaned_text).sents]

boas_vindas_usuario = ("olá", "opa", "oi", "e aí")
boas_vindas_bot = ("Olá", "Opa", "Bem-vindo", "Oi", "Como posso ajudá-lo?")

def mensagem_inicio(texto):
    for palavra in texto.split():
        if palavra.lower() in boas_vindas_usuario:
            return random.choice(boas_vindas_bot)

texto_principal = texto[:3]
texto_principal.append(texto[0])

#vetor_palavras = TfidfVectorizer()
#palavras_rotuladas = vetor_palavras.fit_transform(texto_principal)
#print(palavras_rotuladas)
#print(vetor_palavras.get_feature_names_out()) # Displaying the feature names
#print(vetor_palavras.vocabulary_) # Displaying the vocabulary

#similaridade = cosine_similarity(palavras_rotuladas[0], palavras_rotuladas[2])

#similaridade_todos = cosine_similarity(palavras_rotuladas[0], palavras_rotuladas)

#print(similaridade_todos) # Quanto mais próximo de 1, mais similar é o texto

#print(similaridade_todos.argsort()) # Displaying the indices of the sorted similarities

#x = similaridade_todos.argsort()[0] # Displaying the index of the second most similar text
#print(x[2])

def resposta(texto_usuario):
    resposta_bot = ''
    texto_principal.append(texto_usuario)
    tfidf = TfidfVectorizer()
    palavras_rotuladas = tfidf.fit_transform(texto_principal)
    similaridade_todos = cosine_similarity(palavras_rotuladas[-1], palavras_rotuladas)
    indice_similaridade = similaridade_todos.argsort()[0][-2]  # Getting the index of the second most similar text
    vetor_similaridade = similaridade_todos.flatten() # Getting the similarity vector
    vetor_similaridade.sort() # Sorting the similarity vector
    vetor_encontrado = vetor_similaridade[-2]  # Getting the second highest similarity value

    if (vetor_encontrado == 0):
        resposta_bot = "Desculpe, mas não entendi"
        return resposta_bot
    else:
        resposta_bot = texto_principal[indice_similaridade]
        return resposta_bot
    
def main():
    continuar = True
    print("Olá sou o TwBot e vou te ajudar com algumas perguntas")
    while continuar:
        texto_usuario = input()
        texto_usuario = texto_usuario.lower()
        print(texto_usuario)

        if texto_usuario != "sair":
            if mensagem_inicio(texto_usuario) != None:
                print("TwBot:" + mensagem_inicio(texto_usuario))
            else:
                print("TwBot:")
                print(resposta(texto_usuario))
                texto_principal.remove(texto_usuario)  # Remove the user's input from the main text list    
           
        else:
            continuar = False
            print("TwBot: Até breve!")

main()
            