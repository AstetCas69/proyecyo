from flask import Flask
import random as r
app = Flask(__name__)

facts = [
    "La mayoría de las personas que sufren adicción tecnológica experimentan un fuerte estrés cuando se encuentran fuera del área de cobertura de la red o no pueden utilizar sus dispositivos",
"Según un estudio realizado en 2018, más del 50% de las personas de entre 18 y 34 años se consideran dependientes de sus smartphones"
"Según un estudio de 2019, más del 60% de las personas responden a mensajes de trabajo en sus smartphones en los 15 minutos siguientes a salir del trabajo",
"Una forma de combatir la dependencia tecnológica es buscar actividades que aporten placer y mejoren el estado de ánimo",
"Elon Musk afirma que las redes sociales están diseñadas para mantenernos dentro de la plataforma, para que pasemos el mayor tiempo posible viendo contenidos",
"Elon Musk también aboga por la regulación de las redes sociales y la protección de los datos personales de los usuarios. Afirma que las redes sociales recopilan una enorme cantidad de información sobre nosotros, que luego puede utilizarse para manipular nuestros pensamientos y comportamientos",
"Las redes sociales tienen aspectos positivos y negativos, y debemos ser conscientes de ambos cuando utilicemos estas plataformas"


]



@app.route("/")
def home():
    a = '<h1>Hello, World!</h1>'
    b = '<a href="/random_fact">¡Ver dato aleatorio!</a>'
    return f'{a}\n{b}' 


@app.route("/random_fact")
def random_fact():
    fact= r.choice(facts)
    return f'<p>{fact}</p>'




app.run(debug=True,port=8000)