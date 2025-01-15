from Rectangle import RectangleSingletonDeco

from DataRectangle import DataRectangle


def main():

    r = RectangleSingletonDeco(2,3) # Construction longueur =2, largeur= 3

    #region

    #  OldRectangle

    # print(r._Rectangle__largeur,r._Rectangle__longueur)

    # print(r.get_longueur())

    # r.set_longueur(12)

    # assert r.get_longueur() == 12

    # print("surface",r.get_surface())

    #endregion

    r.longueur = 12
    a =  r.longueur 
    print(r.longueur)

    print(r.surface)

    # r.surface = 12 # Erreur
    

    print(50*'-')

    d = DataRectangle(5,6)
    print(d.longueur)
    print(d.largeur)

    d.largeur = 152
    print(d.largeur)

    print(d.surface)
    del d

    print('la fin')
    

    print(50*'-')

    r = RectangleSingletonDeco(2,3) # Construction longueur =2, largeur= 3
    s = str(r)
    print(s)

    r1 = RectangleSingletonDeco(2,3) # Construction longueur =2, largeur= 3

    if r == r1:

        print("ok")

    else:

        print("ko")

    print(50*'-')

    d = DataRectangle(5,6)

    d1 = DataRectangle(5,6)

    if d == d1:

        print('ok')
    print(d)

    print(d1)
    
    
    print(r.get_cpt())

    print(RectangleSingletonDeco.get_cpt())

    print(50*'-')
    

    values = "2;3"   

    r = RectangleSingletonDeco.buildFromStr(values)
    print(r)

    print(50*'-')

    r = RectangleSingletonDeco(2,3)
    print(r)

    # print(r.__dict__)

    r.toto=1589
    print(r.toto)
    print(r.__dict__)
     

if __name__=='__main__':

    main()
    




