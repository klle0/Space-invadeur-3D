from ursina import *
import time
import random
import pyautogui

jeu = Ursina()

window.fps_counter.enabled=False # Desactive le compteur de fps (Frames Per Second, donc images par secondes)
window.title=('C quoi le nom du jeu ?')
ciel = Sky(texture='espace.jpg')

vitesse = 200
rangees = [i for i in range(-18, 19, 6)] #dispertion d'espace 6 entre les enemis ou obstacles sur le tunnel
colonnes = [i for i in range(2, 45, 7)]

# Creation du tunnel
sol = Entity(model='plane',texture='lune.jpg', collider='box', color=color.dark_gray,
             position=(0, 0, -1000), scale=(50, 1, 1000000), rotation_x=180)


plafond = Entity(model='plane',texture='lune.jpg', collider='box', color=color.dark_gray,
                 position=(0, 0, -1000), scale=(50, 1, 1000000))

mur_gauche = Entity(model='cube', texture='lune.jpg', collider='box', color=color.gray,
                      position=(-25, 25, 0), scale=(1, 50, 100000))

mur_droite = Entity(model='cube', texture='lune.jpg', collider='box', color=color.gray,
                      position=(25, 25, 0), scale=(1, 50, 100000))

# Creation du joueur (joueur.visible=True)
joueur = FrameAnimation3d('avion_model', texture='avion_texture', collider='box',
                          double_sided=True, position=(0, 1, -1000), scale=2.5, rotation_y = 140)

# Creation des ennemis
for i in range(0, 10000, 50):
    ennemis = Entity(model='barrier', texture='barrierTX', collider='box',
                     position=(random.choice(rangees), random.choice(colonnes), i), scale=(4), rotation_y=90)

# Creation de la camera, qui suit le joueur
camera.add_script(SmoothFollow(target=joueur, offset=(0, 5, -20)))

def update():
    # Deplacement du joueur et bouton quitter
    coordonnees_joueur = [joueur.x, joueur.y, joueur.z]
    joueur.z = joueur.z + time.dt * vitesse

    if held_keys['f']: # Gauche
        joueur.x = joueur.x - time.dt * 25
    if held_keys['h']: # Droite
        joueur.x = joueur.x + time.dt * 25
    if held_keys['t']: # Haut
        joueur.y = joueur.y + time.dt * 25
    if held_keys['g']: # Bas
        joueur.y = joueur.y - time.dt * 25
    if held_keys['enter']: # Quitter
        quit()
    
    # Collisions du joueur avec le tunnel et les ennemis
    if joueur.y < 1:
        joueur.y = 1
    if joueur.y > 44:
        joueur.y = 44
    if joueur.x < -23:
        joueur.x = -23
    if joueur.x > 19:
        joueur.x = 19
    
    if joueur.intersects().hit:
        camera.shake(duration=0.5)
        camera.fov = -10
        joueur.visible=False

jeu.run()