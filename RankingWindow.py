from tkinter import *
from tkinter import ttk

class RankingWindow:

    def __init__(self, players_ranking):
        self.ranking_window = Tk()
        self.ranking_window.title("Ranking")
        self.ranking_window.resizable(0,0)
        print("hola1")

        self.ranking_label = ttk.Label( self.ranking_window, text="RANKING").grid( column=0, row=0)
        # Creamos la tabla donde se colocarán los datos del ranking.
        self.ranking_table = ttk.Treeview( self.ranking_window, columns=('#0','#1','#2','#3','#4'))
        self.ranking_table.grid( column=0, row=1)
        print("hola2")

        self.ranking_table.heading("#0", text="Lista")
        self.ranking_table.heading("#1", text="Nombre")
        self.ranking_table.heading("#2", text="Edad")
        self.ranking_table.heading("#3", text="Tiempo")
        self.ranking_table.heading("#4", text="Errores")
        print("hola3")
        # Tomamos la lista de ranking brindada y acomodamos cada
        # dato de la persona en su respectiva categoría.
        for x in range( len(players_ranking)):
            self.ranking_table.insert( "", END, text=f"{x+1}", values= (players_ranking[x][0], players_ranking[x][1], players_ranking[x][2], players_ranking[x][3]))
        print("hola4")