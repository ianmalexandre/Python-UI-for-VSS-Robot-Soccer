from tkinter import *
import rospy
from std_msgs.msg import String


oponente = "treino"
class Application:
    global oponente
    goalAlly = 0
    goalEnemy = 0
    def __init__(self, master=None):

        self.widget0 = Frame(master)
        self.widget0.pack()
        self.placar = Label(self.widget0, text="Placar\nUnBall " + str(self.goalAlly) + " x " 
                            + str(self.goalEnemy) + " " + oponente)
        self.placar["font"] = ("Arial", "9", "bold")
        self.placar.pack ()

        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text="Equipe UnBall")
        self.msg["font"] = ("Arial", "9", "bold")
        self.msg.pack ()

        self.inicio = Button(self.widget1)
        self.inicio["text"] = "Inicio de jogo"
        self.inicio["bg"] = "blue"
        self.inicio["fg"] = "white"
        self.inicio["width"] = 10
        self.inicio.bind("<Button-1>", self.IniciodeJogo)
        self.inicio.pack()

        self.widget2 = Frame(master)
        self.widget2.pack()
        self.playpause = Button(self.widget2)
        self.playpause["text"] = "Play"
        self.playpause["fg"] = "white"
        self.playpause["bg"] = "green"
        self.playpause["width"] = 10
        self.playpause.bind("<Button-1>", self.mudarTexto)
        self.playpause.pack ()

        self.widget3 = Frame(master)
        self.widget3.pack()
        self.goal = Button(self.widget3)
        self.goal["text"] = "Goal :)"
        self.goal["fg"] = "white"
        self.goal["bg"] = "blue"
        self.goal["width"] = 10
        self.goal.bind("<Button-1>", self.ally)
        self.goal.pack()

        self.goalE = Button(self.widget3)
        self.goalE["text"] = "Goal :("
        self.goalE["fg"] = "white"
        self.goalE["bg"] = "red"
        self.goalE["width"] = 10
        self.goalE.bind("<Button-1>", self.enemy)
        self.goalE.pack()

        self.widget5 = Frame(master)
        self.widget5.pack()
        self.msg2 = Label(self.widget5, text="Lado:")
        self.msg2.pack()
        self.LEFT = Button(self.widget5)
        self.LEFT["text"] = "LEFT"
        self.LEFT["fg"] = "white"
        self.LEFT["bg"] = "midnight blue"
        self.LEFT["width"] = 3
        self.LEFT.bind("<Button-1>", self.left)
        self.LEFT.pack(side = LEFT)

        self.RIGHT = Button(self.widget5)
        self.RIGHT["text"] = "RIGHT"
        self.RIGHT["fg"] = "white"
        self.RIGHT["bg"] = "dark slate gray"
        self.RIGHT["width"] = 3
        self.RIGHT.bind("<Button-1>", self.right)
        self.RIGHT.pack(side = RIGHT)

        self.widget7 = Frame(master)
        self.widget7.pack()
        self.sair = Button(self.widget7)
        self.sair["text"] = "sair"
        self.sair["fg"] = "red"
        self.sair.bind("<Button-1>", self.fimdejogo)
        self.sair["command"] = self.widget5.quit
        self.sair.pack(side = "bottom")

    def left(self, event):
        print ("L")
        #pub.publish("L")
        rate.sleep()
    
    def right(self, event):
        print ("R")
        #pub.publish("R")
        rate.sleep()
    
    def ally(self, event):
        if self.msg["text"] == "O jogo está rodando":
            print("Goal")
            self.goalAlly += 1
            self.placar["text"] = "Placar\nUnBall " + str(self.goalAlly) + " x " + str(self.goalEnemy) + " " + oponente
            self.playpause["text"] = "Play"
            self.playpause["bg"] = "green"
            self.msg["text"] = "O jogo está pausado"
            self.msg["fg"] = "red"
            #pub.publish("P")
            #rate.sleep()
    
    def enemy(self, event):
        if self.msg["text"] == "O jogo está rodando":
            print("E Goal")
            self.goalEnemy += 1
            self.placar["text"] = "Placar\nUnBall " + str(self.goalAlly) + " x " + str(self.goalEnemy) + " " + oponente
            self.playpause["text"] = "Play"
            self.playpause["bg"] = "green"
            self.msg["text"] = "O jogo está pausado"
            self.msg["fg"] = "red"
            #pub.publish("P")
            #rate.sleep()

    def fimdejogo(self, event):
        print ("Q")
    def IniciodeJogo(self, event):
        if self.msg["text"] == "Equipe UnBall":
            self.msg["text"] = "O jogo está rodando"
            self.msg["fg"] = "blue"
            self.playpause["text"] = "Pause"
            self.playpause["bg"] = "red"
            #pub.publish("G")
            #rate.sleep()
            
    def mudarTexto(self, event):
        if self.msg["text"] == "O jogo está rodando":
            self.msg["text"] = "O jogo está pausado"
            self.msg["fg"] = "red"
            self.playpause["text"] = "Play"
            self.playpause["bg"] = "green"
            #pub.publish("P")
            #rate.sleep()
        else:
            self.msg["text"] = "O jogo está rodando"
            self.msg["fg"] = "blue"
            self.playpause["text"] = "Pause"
            self.playpause["bg"] = "red"
            #pub.publish("G")
            #rate.sleep()
  
  
oponente = input("Digite o nome da equipe adversária: ")
root = Tk()

#rospy.init_node('game_commands')
#pub = rospy.Publisher('game_commands', String, queue_size=1)
#rate = rospy.Rate(30)

theLabel = Label(root, text = "Interface de jogo")
theLabel.pack()
Application(root)
root.mainloop()