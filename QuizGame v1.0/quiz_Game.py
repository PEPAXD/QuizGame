#LIBRARIES
import DeveloperCredits
import os

class arraysQuiz:

    def cienciaQuiz(self):
        arrayQuestionCiencia = {
            "Pregunta 1": {
                    "question": "¿Cuál es el proceso por el cual las plantas convierten la luz solar en energía química?",
                    "answer": "Fotosíntesis"
                },
            "Pregunta 2": {
                    "question": "¿Qué elemento químico es el más abundante en la atmósfera terrestre?",
                    "answer": "Nitrógeno"
                },
            "Pregunta 3": {
                    "question": "¿Qué órgano del cuerpo humano es responsable de la producción de insulina?",
                    "answer": "Páncreas"
                },
            "Pregunta 4": {
                    "question": "¿Qué teoría científica propone que todas las formas de vida comparten un ancestro común?",
                    "answer": "Teoría de la evolución"
                },
            "Pregunta 5": {
                    "question": "¿Qué fenómeno natural causa la formación de arcoíris?",
                    "answer": "La refracción y reflexión de la luz solar en gotas de agua en suspensión en la atmósfera."
                },
        }

        return arrayQuestionCiencia

    def historiaQuiz(self):
        arrayQuestionHistoria = {
            "Pregunta 1": {
                    "question": "¿Quién fue el primer presidente de la Nación Argentina?",

                    "answer": "Bernardino Rivadavia",
                },
            "Pregunta 2": {
                    "question": "¿En qué año se sancionó la Constitución Nacional Argentina?",
                    "answer": "1853"
                },
            "Pregunta 3": {
                    "question": "¿Quién lideró la Revolución de Mayo en 1810?",
                    "answer": "Manuel Belgrano"
                },
            "Pregunta 4": {
                    "question": "¿Qué presidente argentino implementó el Plan de Convertibilidad?",
                    "answer": "Carlos Menem"
                },
            "Pregunta 5": {
                    "question": "¿En qué año se produjo el Golpe de Estado en Argentina que dio inicio a la última dictadura militar?",
                    "answer": "1976"
                },
        }

        return arrayQuestionHistoria

    def musicaQuiz(self):
        arrayQuestionMusic = {
            "Pregunta 1": {
                    "question": "¿Qué instrumento tocaba el famoso músico Wolfgang Amadeus Mozart?",

                    "answer": "Piano",
                },
            "Pregunta 2": {
                    "question": "¿Qué banda lideró Freddie Mercury?",
                    "answer": "Queen"
                },
            "Pregunta 3": {
                    "question": "¿Qué cantante popularizó la canción 'Thriller' ?",
                    "answer": "Michael Jackson"
                },
            "Pregunta 4": {
                    "question": "¿En qué década apareció el famoso grupo de rock 'The Rolling Stones'?",
                    "answer": "1960"
                },
            "Pregunta 5": {
                    "question": "¿Cuál es el nombre real de la cantante pop conocida como Lady Gaga?",
                    "answer": "Stefani Joanne Angelina Germanotta"
                },
        }

        return arrayQuestionMusic

    def deportesQuiz(self):
        arrayQuestionDeportes = {
            "Pregunta 1": {
                    "question": "¿Qué equipo de fútbol argentino es conocido como 'El Xeneize'?",

                    "answer": "Boca Juniors",
                },
            "Pregunta 2": {
                    "question": "¿Quién es el tenista argentino que ha ganado más títulos de Grand Slam en la historia del país?",
                    "answer": "Guillermo Vilas, con 4 títulos"
                },
            "Pregunta 3": {
                    "question": "¿Qué boxeador argentino es conocido como 'El Chino' y ha sido campeón mundial en varias categorías?",
                    "answer": "Marcos Maidana"
                },
            "Pregunta 4": {
                    "question": "¿En qué deporte destacó la atleta argentina Paola Suárez?",
                    "answer": "Tenis, en la modalidad de dobles"
                },
            "Pregunta 5": {
                    "question": "¿Qué piloto argentino de Fórmula 1 ganó el Campeonato Mundial en 1975 y 1977?",
                    "answer": "Carlos Reutemann"
                },
        }

        return arrayQuestionDeportes

    def frikiQuiz(self):
        arrayQuestionFriki = {
            "Pregunta 1": {
                    "question": "¿Cuál es el nombre del personaje principal de la saga de videojuegos 'The Legend of Zelda'?",

                    "answer": "Link",
                },
            "Pregunta 2": {
                    "question": "¿En qué año se lanzó el primer videojuego de la saga 'Super Mario Bros'?",
                    "answer": "1985"
                },
            "Pregunta 3": {
                    "question": "¿Quién es el creador de la famosa saga de videojuegos 'Metal Gear Solid'?",
                    "answer": "Hideo Kojima"
                },
            "Pregunta 4": {
                    "question": "¿Cuál es el nombre del personaje principal de la saga de videojuegos 'Assassin's Creed'?",
                    "answer": "Desmond Miles"
                },
            "Pregunta 5": {
                    "question": "¿En qué año se lanzó la consola de videojuegos 'PlayStation 2'?",
                    "answer": "2000"
                },
        }

        return arrayQuestionFriki

def scoreUser(arrayQuestion):

    score = 0
    for key, value in arrayQuestion.items():
        print(value['question'])
        answer = input("Respuesta? ")

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
