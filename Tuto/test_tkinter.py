from tkinter import *


Arene = Tk()
Arene.title('Arene')
Arene.geometry("500x500")
#---------------------------------------------------------------------------------------------
bouton = Button(Arene, text ="Quitter",command=Arene.destroy)
bouton.pack()
#---------------------------------------------------------------------------------------------
texte = Label(Arene, text = "FiveGuys")
texte['fg'] = 'red'
texte.pack()




#---------------------------------------------------------------------------------------------
Entree = Entry(Arene)
Entree.pack()
#--------------------------------------------------------------------------------------------
zone_dessin =Canvas(Arene, width=300, height=300)
zone_dessin.pack()
zone_dessin.create_line(0,0,300,300)
zone_dessin.create_rectangle(100,100,200,200)
zone_dessin.create_text(200,380, text = "Robot",fill = 'black')




Arene.mainloop()#obligatoire


