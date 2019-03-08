@@ -24,6 +24,7 @@ def __init__(self,nb_ligne, nb_colonne):
        self.matrice=np.zeros((nb_ligne,nb_colonne))
        self.list_rob=[]
        self.list_obj=[]
        self.coord_rob=[0,0]
        #cree les mur

    def cree_mur(self):
@@ -62,6 +63,8 @@ def inserer_robot(self,r):
        """
        if self.est_dans_matrice(r) and self.est_vide:
            self.matrice[int(r.y),int(r.x)]=2
            self.coord_rob[0]=int(r.x)
            self.coord_rob[1]=int(r.y)
            self.list_rob.append(r)

    def inserer_obs(self,o):
@@ -81,16 +84,8 @@ def get_object(self,x,y):
        """
        return int(self.matrice[x,y])

    def supprimer_uns(self) :
        """Supprime les 1 dans la matrice pour supprimer le robot
        """
        for i in range (0, self.nb_ligne) :
            for j in range(0, self.nb_colonne) :
                if self.matrice[i,j]==2:
                    self.matrice[i,j]=0

    def update(self) :
        self.supprimer_uns()
        self.matrice[self.coord_rob[0],self.coord_rob[1]]=0
        l_rob= self.list_rob
        self.list_rob=[]
        for i in l_rob:
