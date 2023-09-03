from textblob import TextBlob
from googletrans import Translator
class Polarity:
    def polarity(self, text ):
        polarity = TextBlob(text)
        return polarity.sentiment.polarity

class Sentimiento: 
    def __init__(self,sentimiento, color):
        self.sentimiento =sentimiento
        self.color = color
    def __str__(self):
        return f"\x1b[1;{self.color}mLa sensacion es {self.sentimiento}\x1b[0;37m" 
        
        
class AnalizadorSentimientos:
    def analizador(self, rango, polarity):
        for rango, sentimiento in rango:
            if rango[0]<polarity<rango[1]:
                return sentimiento
            
        return Sentimiento("Muy negativo","31")
rango =[
((-0.6, -0.3), Sentimiento("negativo","31")),
((-0.3, -0.1), Sentimiento ("algo negativo", "31")),
((-0.1,0.1), Sentimiento ("neutral", "33")),
((0.1,0.4), Sentimiento ("algo positivo","32")),
((0.4,0.9), Sentimiento ("positivo", "32")),
((0.9,1.1), Sentimiento("muy positivo", "32"))
]
while True:
    
    manuel = Polarity() 
    usuario = input("Diga su frase en espanol: ")
    traducir = Translator()
    user =  traducir.translate(usuario,dest="en")
    manuel = manuel.polarity(user.text)
    print(user.text)
    print(manuel)
    
    sentimiento_manuel = AnalizadorSentimientos()
    sentimiento_manuel = sentimiento_manuel.analizador(rango, manuel)
    print(sentimiento_manuel)