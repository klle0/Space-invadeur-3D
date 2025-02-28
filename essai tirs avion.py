from ursina import *
import time
import random
import pyautogui
app = Ursina()
window.fps_counter.enabled = False
window.title = ('Space Game')
ciel = Sky(texture='espace.jpg')
window.size = (1730, 850)  
#window_width = 800
#window_height = 600

def quit():
    application.quit()


player_speed = 10
player_position = Vec3(0, 1, -1000)
player = Entity(model='cube', color=color.blue, position=player_position)

enemies = []

def spawn_enemy():
    rangees = [-18, -12, -6, 0, 6, 12, 18]
    columns = [-22, -15, -8, -1, 6, 13, 20]

    enemy = Entity(model='cube', color=color.red)
    enemy.position = (random.choice(rangees), random.choice(columns), player.z + 50)
    enemies.append(enemy)

def update():
    global player_position

    player_position.z += time.dt * player_speed
    player.position = player_position

    # Player controls
    if held_keys['a']:  # Left
        player_position.x -= time.dt * player_speed
    if held_keys['d']:  # Right
        player_position.x += time.dt * player_speed
    if held_keys['w']:  # Up
        player_position.y += time.dt * player_speed
    if held_keys['s']:  # Down
        player_position.y -= time.dt * player_speed

    # Boundary checks
    player_position.x = clamp(player_position.x, -23, 19)
    player_position.y = clamp(player_position.y, 1, 44)

    # Spawn enemies
    if player.z % 50 == 0:
        spawn_enemy()

    # Check collisions
    for enemy in enemies:
        if player.intersects(enemy).hit:
           quit()


app.run()