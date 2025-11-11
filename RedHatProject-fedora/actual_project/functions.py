import random
from PIL import Image, ImageTk
from items import random_item
from enemy import *
import tkinter as tk

#  ------------Combos dictionary------------------
COMBOS = {
    "Flame Strike": {"keys": "zxz", "damage": 5},
    "Ice Blast": {"keys": "cvb", "damage": 7},
    "Shadow Claw": {"keys": "nmz", "damage": 10},
    "Darkness":{"keys":"xzx","damage": 8},                                          #made by tester :]  Thx for testing
    "Earthquake":{"keys":"xnzc","damage": 12},
    "Admin": {"keys": "cvbcvb", "damage": 1000000}
}

def start_player_turn(window):
    window.player_turn = True
    window.input_buffer = ""
    window.combo_label.config(text="Type a combo...")
    window.combo_timer_id = window.after(5000, lambda: evaluate_combo(window))

def key_pressed(window, event):
    if not hasattr(window, "player_turn") or not window.player_turn:
        return

    key = event.keysym.lower()
    if key not in "zxcvbnm":
        return

    window.input_buffer += key
    window.combo_label.config(text=f"Typing: {'-'.join(window.input_buffer.upper())}")

    if len(window.input_buffer) >= window.max_combo_length:
        if window.combo_timer_id:
            window.after_cancel(window.combo_timer_id)
        evaluate_combo(window)

def evaluate_combo(window):
    window.player_turn = False

    if window.combo_timer_id:
        window.after_cancel(window.combo_timer_id)

    buffer = window.input_buffer
    matched = False

    for name, data in COMBOS.items():
         if buffer == data["keys"]:
             window.enemy.hp -= data["damage"]
             window.enemy_hp_label.config(text=f"Enemy HP: {window.enemy.hp}")
             window.combo_label.config(text=f"{name} hit! -{data['damage']} HP")
             matched = True
             print("Combo matched!")
             break

    if not matched:
        window.combo_label.config(text="Invalid combo!")

    if window.enemy.hp <= 0:
        window.after(1000, lambda: end_combat(window, True))
    else:
        window.after(1500, lambda: enemy_attack(window))

def enemy_attack(window):
    damage = window.enemy.atk
    alive = window.player.getting_damage(damage)
    window.player_hp_label.config(text=f"Player HP: {window.player.hp}")
    window.combo_label.config(text=f"Enemy damage: {window.enemy.atk}HP!")

    if not alive:
        window.after(1000, lambda: end_combat(window, False))
    else:
        window.after(1000, lambda: start_player_turn(window))

def end_combat(window, won):
    window.clear_screen()

    if won:
        prize = random.randint(15,30)
        window.player.add_money(prize)
        result = f"You won!\n You got {prize} Money!"
    else:
        result = "You lost!"

    img = Image.open("pictures/arena_background.png").resize((1200, 960))
    window.fighting_background_img = ImageTk.PhotoImage(img)
    window.canvas.create_image(600, 480, anchor="center", image=window.fighting_background_img,tag="fighting_background")

    window.combo_label = tk.Label(window.canvas, text=result, font=("Arial", 16), bg="#0C250C",fg="white")
    window.combo_label.place(relx=0.5, rely=0.4, anchor="center")

    window.back_button = tk.Button(text="Back to Arena", width=30, height=2, font=("Arial", 12), command=lambda: window.arena_menu(None))
    window.back_button.place(relx=0.5, rely=0.5, anchor="center")


def pickup_item(window, event, item_id):
    print("item picked up!")
    window.canvas.delete(item_id)

    if item_id in window.spawned_items:
        window.spawned_items.remove(item_id)

    item = random_item()
    window.player.inventory.append(item)
    print("Item picked and added to inventory:", item)
 
def spawn_random_item(canvas, bounds, on_click_callback):
    x1, y1, x2, y2 = bounds
    x, y = random.randint(x1+20, x2-70),random.randint(y1+20,y2-70)
    size = 50

    img_plant_top = ImageTk.PhotoImage(Image.open("pictures/plant_top.png"))
    item_id = canvas.create_image(x, y, anchor="nw", image=img_plant_top, tags="farm_item")
    """item_id = canvas.create_rectangle(x, y, x + size, y + size, fill="gold", tags="farm_item")"""

    # Store a reference to the image or it will be garbage collected :/ python why...
    if not hasattr(canvas, "images"):
        canvas.images = []
    canvas.images.append(img_plant_top)

    canvas.tag_bind(item_id, "<Button-1>", lambda e: on_click_callback(e, item_id))

    return item_id

def start_farm_spawning(window):
    if not window.in_farm:
        return
    print("spawning loop activated")
    if len(window.spawned_items) < window.max_items:
        item_id = spawn_random_item(window.canvas,window.farm_area_coords,lambda e, i=None: pickup_item(window, e, i))
        window.spawned_items.append(item_id)

    if window.in_farm:
        window.after(2000, lambda: start_farm_spawning(window))             #time needs to be fixed - ms is random - tkinter tweak

def throw_item_to_cauldron(window, item):
    window.player.throw_into_cauldron(item)
    print(f"Thrown into cauldron: {item.name}")
    window.refresh_inventory_buttons()

def refresh_inventory_buttons(window):
    for b in window.item_buttons:
        b.destroy()
    window.item_buttons.clear()

    for idx, item in enumerate(window.player.inventory):
        button = tk.Button(
            window,
            text=item.name,
            command=lambda i=item: window.throw_item_to_cauldron(i),
            width=20
        )
        button.place(x=800, y=50 + idx * 40)
        window.item_buttons.append(button)