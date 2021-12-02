from ipycanvas import Canvas
from math import pi, sin, cos


# Création d'une toile support pour le  dessin
toile = Canvas(width = int(input('Largeur en pixels ?')), height = int(input('Hauteur en pixels ?')))  
    
# Fonction point()
def point(x, y, couleur, taille) :
    toile.fill_style = couleur
    toile.fill_arc(x, y, taille, 0, 2*pi)

# Fonction point_carre()
def point_carre(x, y, couleur, taille) :
    toile.fill_style = couleur
    toile.fill_rect(x-(taille/2),y-(taille/2),taille)
    
# Fonction cercle()
def cercle(x, y, couleur, taille, epaisseur) :
    toile.line_width = epaisseur
    toile.fill_style = couleur
    toile.stroke_arc(x, y, taille, 0, 2*pi)
    
# Fonction carre()
def carre(x, y, couleur, taille, epaisseur) :
    toile.line_width = epaisseur
    toile.fill_style = couleur