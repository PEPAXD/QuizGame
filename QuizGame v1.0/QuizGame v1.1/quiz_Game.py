#LIBRARIES
import DeveloperCredits
import os

class arraysQuiz:

    def cienciaQuiz(self):
        arrayQuestionCiencia = {
            "Pregunta 1": {
                    "question": "¿Cuál es el proceso por el cual las plantas convierten la luz solar en energía química?",
                    "falseAnswer1": "Fotosíntesis ",
                    "falseAnswer2": "Respiración",
                    "falseAnswer3": "Transpiración",
                    "falseAnswer4": "Germinación",
                    "answer": "Fotosíntesis"
                },
            "Pregunta 2": {
                    "question": "¿Qué elemento químico es el más abundante en la atmósfera terrestre?",
                    "falseAnswer1": "Hidrógeno",
                    "falseAnswer2": "Nitrógeno",
                    "falseAnswer3": "Oxígeno",
                    "falseAnswer4": "Dióxido de carbono",
                    "answer": "Nitrógeno"
                },
            "Pregunta 3": {
                    "question": "¿Qué órgano del cuerpo humano es responsable de la producción de insulina?",
                    "falseAnswer1": "Páncreas",
                    "falseAnswer2": "Hígado",
                    "falseAnswer3": "Pulmones",
                    "falseAnswer4": "Riñones",
                    "answer": "Páncreas"
                },
            "Pregunta 4": {
                    "question": "¿Qué teoría científica propone que todas las formas de vida comparten un ancestro común?",
                    "falseAnswer1": "Teoría de la evolución",
                    "falseAnswer2": "Teoría de la relatividad",
                    "falseAnswer3": "Teoría de la selección natural",
                    "falseAnswer4": "Teoría de la generación espontánea",
                    "answer": "Teoría de la evolución"
                },
            "Pregunta 5": {
                    "question": "¿Qué fenómeno natural causa la formación de arcoíris?",
                    "falseAnswer1": "Refracción de la luz en las nubes",
                    "falseAnswer2": "Reflexión de la luz en las gotas del agua",
                    "falseAnswer3": "Refracción de la luz en las hojas de los árboles",
                    "falseAnswer4": "Interferencia de la luz en la atmósfera",
                    "answer": "Reflexión de la luz en las gotas del agua"
                },
        }

        return arrayQuestionCiencia

    def historiaQuiz(self):
        arrayQuestionHistoria = {
            "Pregunta 1": {
                    "question": "¿Quién fue el primer presidente de la Nación Argentina?",
                    "falseAnswer1": "Carlos Menem",
                    "falseAnswer2": "Mauricio Macri",
                    "falseAnswer3": "Domingo Faustino Sarmiento",
                    "falseAnswer4": "Bernardino Rivadavia",
                    "answer": "Bernardino Rivadavia",
                },
            "Pregunta 2": {
                    "question": "¿En qué año se sancionó la Constitución Nacional Argentina?",
                    "falseAnswer1": "1816",
                    "falseAnswer2": "1820",
                    "falseAnswer3": "1853",
                    "falseAnswer4": "1860",
                    "answer": "1853"
                },
            "Pregunta 3": {
                    "question": "¿Quién lideró la Revolución de Mayo en 1810?",
                    "falseAnswer1": "José de San Martín",
                    "falseAnswer2": "Manuel Belgrano",
                    "falseAnswer3": "Mariano Moreno",
                    "falseAnswer4": "Juan Manuel de Rosas",
                    "answer": "Manuel Belgrano"
                },
            "Pregunta 4": {
                    "question": "¿Qué presidente argentino implementó el Plan de Convertibilidad?",
                    "falseAnswer1": "Néstor Kirchner",
                    "falseAnswer2": "Carlos Menem",
                    "falseAnswer3": "Raúl Alfonsín",
                    "falseAnswer4": "Eduardo Duhalde",
                    "answer": "Carlos Menem"
                },
            "Pregunta 5": {
                    "question": "¿En qué año se produjo el Golpe de Estado en Argentina que dio inicio a la última dictadura militar?",
                    "falseAnswer1": "1971",
                    "falseAnswer2": "1974",
                    "falseAnswer3": "1976",
                    "falseAnswer4": "1979",
                    "answer": "1976"
                },
        }

        return arrayQuestionHistoria

    def musicaQuiz(self):
        arrayQuestionMusic = {
            "Pregunta 1": {
                    "question": "¿Qué instrumento tocaba el famoso músico Wolfgang Amadeus Mozart?",
                    "falseAnswer1": "Guitarra",
                    "falseAnswer2": "Piano",
                    "falseAnswer3": "Batería",
                    "falseAnswer4": "Violin",
                    "answer": "Piano",
                },
            "Pregunta 2": {
                    "question": "¿Qué banda lideró Freddie Mercury?",
                    "falseAnswer1": "Nirvana",
                    "falseAnswer2": "Queen",
                    "falseAnswer3": "Rolling Stones",
                    "falseAnswer4": "The Beatles",
                    "answer": "Queen"
                },
            "Pregunta 3": {
                    "question": "¿Qué cantante popularizó la canción 'Thriller'?",
                    "falseAnswer1": "Shakira",
                    "falseAnswer2": "Beyoncé",
                    "falseAnswer3": "Madonna",
                    "falseAnswer4": "Michael Jackson",
                    "answer": "Michael Jackson"
                },
            "Pregunta 4": {
                    "question": "¿En qué década apareció el famoso grupo de rock 'The Rolling Stones'?",
                    "falseAnswer1": "1950",
                    "falseAnswer2": "1960",
                    "falseAnswer3": "1970",
                    "falseAnswer4": "1980",
                    "answer": "1960"
                },
            "Pregunta 5": {
                    "question": "¿Cuál es el nombre real de la cantante pop conocida como Lady Gaga?",
                    "falseAnswer1": "Stefani Joanne Angelina Germanotta",
                    "falseAnswer2": "Katheryn Elizabeth Hudson",
                    "falseAnswer3": "Robyn Rihanna Fenty",
                    "falseAnswer4": " Alecia Beth Moore",
                    "answer": "Stefani Joanne Angelina Germanotta"
                },
        }

        return arrayQuestionMusic

    def deportesQuiz(self):
        arrayQuestionDeportes = {
            "Pregunta 1": {
                    "question": "¿Qué equipo de fútbol argentino es conocido como 'El Xeneize'?",
                    "falseAnswer1": "River Plate",
                    "falseAnswer2": "San Lorenzo",
                    "falseAnswer3": "Racing Club",
                    "falseAnswer4": "Boca Juniors",
                    "answer": "Boca Juniors",
                },
            "Pregunta 2": {
                    "question": "¿Quién es el tenista argentino que ha ganado más títulos de Grand Slam en la historia del país?",
                    "falseAnswer1": "Guillermo Vilas",
                    "falseAnswer2": "Juan Martín Del Potro",
                    "falseAnswer3": "David Nalbandian",
                    "falseAnswer4": "Gastón Gaudio",
                    "answer": "Guillermo Vilas"
                },
            "Pregunta 3": {
                    "question": "¿Qué boxeador argentino es conocido como 'El Chino' y ha sido campeón mundial en varias categorías?",
                    "falseAnswer1": "Julio César Chávez",
                    "falseAnswer2": "Marcos Maidana",
                    "falseAnswer3": "Juan Manuel Márquez",
                    "falseAnswer4": "Óscar De La Hoya",
                    "answer": "Marcos Maidana"
                },
            "Pregunta 4": {
                    "question": "¿En qué deporte destacó la atleta argentina Paola Suárez?",
                    "falseAnswer1": "Vóley",
                    "falseAnswer2": "Natación",
                    "falseAnswer3": "Tenis",
                    "falseAnswer4": "Atletismo",
                    "answer": "Tenis"
                },
            "Pregunta 5": {
                    "question": "¿Qué piloto argentino de Fórmula 1 ganó el Campeonato Mundial en 1975 y 1977?",
                    "falseAnswer1": "Juan Manuel Fangio",
                    "falseAnswer2": "Carlos Reutemann",
                    "falseAnswer3": "Nico Rosberg",
                    "falseAnswer4": "Ayrton Senna",
                    "answer": "Carlos Reutemann"
                },
        }

        return arrayQuestionDeportes

    def frikiQuiz(self):
        arrayQuestionFriki = {
            "Pregunta 1": {
                    "question": "¿Cuál es el nombre del personaje principal de la saga de videojuegos 'The Legend of Zelda'?",
                    "falseAnswer1": "Mario",
                    "falseAnswer2": "Pikachu",
                    "falseAnswer3": "Master Chief",
                    "falseAnswer4": "Link",
                    "answer": "Link",
                },
            "Pregunta 2": {
                    "question": "¿En qué año se lanzó el primer videojuego de la saga 'Super Mario Bros'?",
                    "falseAnswer1": "2005",
                    "falseAnswer2": "1985",
                    "falseAnswer3": "1983",
                    "falseAnswer4": "1995",
                    "answer": "1985"
                },
            "Pregunta 3": {
                    "question": "¿Quién es el creador de la famosa saga de videojuegos 'Metal Gear Solid'?",
                    "falseAnswer1": "Shigeru Miyamoto",
                    "falseAnswer2": "Gabe Newell",
                    "falseAnswer3": "Hideo Kojima",
                    "falseAnswer4": "Tim Schafer",
                    "answer": "Hideo Kojima"
                },
            "Pregunta 4": {
                    "question": "¿Cuál es el nombre del personaje principal de la saga de videojuegos 'Assassin's Creed'?",
                    "falseAnswer1": "Desmond Miles",
                    "falseAnswer2": "Marcus Fenix",
                    "falseAnswer3": "John Marston",
                    "falseAnswer4": "Ezio Auditore",
                    "answer": "Desmond Miles"
                },
            "Pregunta 5": {
                    "question": "¿En qué año se lanzó la consola de videojuegos 'PlayStation 2'?",
                    "falseAnswer1": "1998",
                    "falseAnswer2": "1995",
                    "falseAnswer3": "2000",
                    "falseAnswer4": "2002",
                    "answer": "2000"
                },
        }

        return arrayQuestionFriki

def scoreUser(arrayQuestion):

    score = 0
    for key, value in arrayQuestion.items():
        print(value['question'])

        print("----------------------------------------------------------")

        #PRINT ANSWER OPTION
        numAnswer = 1
        while numAnswer < 5:
            print(value['falseAnswer'+str(numAnswer)])
            numAnswer += 1

        answer = input("\nRespuesta: ")

        if answer.lower() == value['answer'].lower():
            print("\n---------------------------------------------------")
            print('CORRECTO :)')
            score += 1
            print("PUNTAJE ---> "+str(score)+"/"+str(len(arrayQuestion)))
            print("---------------------------------------------------\n")
        else:
            print("\n---------------------------------------------------")
            print("INCORRECTO :(")
            print("LA RESPUESTA ES ---> "+value['answer'])
            print("PUNTAJE ---> " + str(score) + "/"+str(len(arrayQuestion)))
            print("---------------------------------------------------\n")

    os.system('cls')
    print("TU PUNTUAJE ES ---> "+str(score)+"/"+str(len(arrayQuestion))+" RESPUESTAS CORRECTAS")


def wellcomeQuizGame():

    DeveloperCredits.printCredits()

    print("BIENVENIDO A PY-QUIZ-GAME")
    print("---------------------------------------------------------------------------")
    print("SELECCIONE UNA CATEGORIA Y RESPONDA CORRECTAMENTE PARA GANAR MUCHOS PREMIOS\n")
    print("1) Ciencias")
    print("2) Historia")
    print("3) Musica")
    print("4) Deportes")
    print("5) Gaming")
    print("---------------------------------------------------------------------------")

def userOption():

    userOption = 0
    while userOption < 1 or userOption > 5:

        print('\rELIJO LA OPCION ---> ', end='')
        userOption = int(input())
        os.system('cls')

    return userOption

def quizThemeSelection(userOption):

    if userOption == 1:
        print("\nTEMATICA CIENCIA\n")
        userOption = arraysQuiz().cienciaQuiz()

    elif userOption == 2:
        print("\nTEMATICA HISTORIA\n")
        userOption = arraysQuiz().historiaQuiz()

    elif userOption == 3:
        print("\nTEMATICA MUSICA\n")
        userOption = arraysQuiz().musicaQuiz()

    elif userOption == 4:
        print("\nTEMATICA DEPORTES\n")
        userOption = arraysQuiz().deportesQuiz()

    elif userOption == 5:
        print("\nTEMATICA GAMING\n")
        userOption = arraysQuiz().frikiQuiz()

    return userOption

def endGame():

    startNewGame = input("\nQUIERE VOLVER A JUGAR? Y/N: ")

    if startNewGame.lower() == "y":
        os.system('cls')
        main()

#Execute Command
def main():

    #PRINT TRIVIA THEMES OPTIONS
    wellcomeQuizGame()

    #SELECT THEME TARGET
    userInput = userOption()
    themeTarget = quizThemeSelection(userInput)

    #START QUIZGAME
    scoreUser(themeTarget)

    #END-GAME?
    endGame()

# EJECUTAR SCRIPT
if __name__ == '__main__':
    main()
