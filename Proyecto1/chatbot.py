import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    (r'Hola|Hola!', ['Hola!', 'Hola, ¿cómo estás?']),
    (r'¿Cómo estás?', ['Estoy bien, gracias. ¿Y tú?']),
    (r'¿Cuál es tu nombre?', ['Soy un chatbot.']),
    (r'Adiós|Hasta luego', ['Adiós!', 'Hasta luego!']),
    (r'(.*)', ['Lo siento, no entiendo eso.']),
]

def chatbot():
    print("Hola, soy un chatbot. Escribe 'Adiós' para salir.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    nltk.download('punkt')
    chatbot()
