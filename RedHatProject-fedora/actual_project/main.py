import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from player import Player
from enemy import Enemy
from functions import *

class Window(tk.Tk):                            #                       (tk.Tk)
    def __init__(self):                         #                         /|\
        super().__init__()                      #makes the rooting correct |
        self.inicialization_of_window()

        #  ------------Making actual player------------------
        self.player = Player(master=self)

        #  ------------Setting UI------------------
        self.main_menu()

        #  ------------Status for more buttons------------------
        self.item_buttons = []

        #  ------------Binding keys------------------
        self.bind("<Key>", lambda e: key_pressed(self, e))
        self.bind("<Escape>", self.main_menu_esc)

        #maybe some addicional parameters in future

        #  ------------App running------------------
        self.mainloop()

    def inicialization_of_window(self):
        #  ------------Setting a title------------------
        self.title("Wizard Cooking")
        #  ------------Setting a resolution------------------
        self.geometry("1200x960+0+0")                              #widthxheigh+adjucted_offset_width(like spawning already moved)+adjucted_offset_height
        #  ------------Making not resizable------------------
        self.resizable(False, False)

    def content(self):
        #  ------------Variable for esc key------------------
        self.in_menu = False
        #  ------------Variable for spawning farm mechanic------------------
        self.in_farm = False

        #  ------------CHECK AREA FOR CLEARING------------------
        self.clear_screen()
                  
        #  ------------Making main UI------------------

        img = Image.open("pictures/street_background.png").resize((1200, 960))
        self.img_background = ImageTk.PhotoImage(img)
        self.canvas.create_image(600, 480, anchor="center", image=self.img_background)

        img = Image.open("pictures/cat.png").resize((340, 410))
        self.img_cat = ImageTk.PhotoImage(img)
        self.canvas.create_image(950, 750, anchor="center", image=self.img_cat)
        
        self.cat_area = self.add_clickable_area("cat_area", 825, 600, 1065, 900, self.cat_menu)

        self.arena_area = self.add_clickable_area("arena_area",820,90,1260,430, self.arena_menu)

        self.farm_area = self.add_clickable_area("farm_area",0,785,610,960, self.farm_menu)
        
        self.shop_area = self.add_clickable_area("shop_area",250,480,350,630, self.shop_menu)

        self.cauldron_area = self.add_clickable_area("cauldron_area",665,340,760,500, self.cauldron_menu)

        self.show_money_label(1000,30,"lightblue")
        """self.player.money.set(100)"""                                        #debug only

    def on_hover(self, tag):
        self.canvas.itemconfig(tag, outline="yellow", width=3)                  #debug only
    def on_leave(self, tag):
        self.canvas.itemconfig(tag, outline="", width=0)                        #debug only

    def add_clickable_area(self,name,x1,y1,x2,y2, on_click):
        #  ------------Making invisible shape------------------
        area = self.canvas.create_rectangle(x1, y1, x2, y2, outline="", fill="", stipple="gray12", tags=name)

        #  ------------Adding binds to shape------------------
        """self.canvas.tag_bind(name, "<Enter>", lambda e, t=name: self.on_hover(t))
        self.canvas.tag_bind(name, "<Leave>", lambda e, t=name: self.on_leave(t))"""        
        self.canvas.tag_bind(name, "<Button-1>", lambda e: on_click(e))

        #  ------------Returns id to creating variable------------------
        return area

    def cat_menu(self,event):
        #  ------------Variable for esc key------------------
        self.in_menu = True
        print("cat entered")                                                    #debug only

        #  ------------CHECK AREA FOR CLEARING------------------
        self.clear_screen()

        #  ------------Setting UI------------------
        img = Image.open("pictures/cat_background.png").resize((1200, 960))
        self.cat_background_img = ImageTk.PhotoImage(img)
        self.canvas.create_image(600, 480, anchor="center", image=self.cat_background_img,tag="cat_background")

        img = Image.open("pictures/cat.png").resize((800, 1020))
        self.img_cat = ImageTk.PhotoImage(img)
        self.canvas.create_image(400, 480, anchor="center", image=self.img_cat,tag="cat")

        self.character_label = tk.Label(self, text="Character Area", font=("Arial", 16),bg="lightyellow")
        self.character_label.place(x=100, y=40)

        self.inventory_label = tk.Label(self, text="Inventory", font=("Arial", 16),bg="lightyellow")
        self.inventory_label.place(x=850, y=30)

        img = Image.open("pictures/inventory_background.png").resize((800, 980))
        self.inventory_background_img = ImageTk.PhotoImage(img)
        self.canvas.create_image(900, 480, anchor="center", image=self.inventory_background_img,tag="inventory_background")
        """self.inventory_background = self.canvas.create_rectangle(800,40,1000,800,outline="",fill= "black",tag = "test")"""               #debug only

        self.back_button = tk.Button(text="back",width=20,height=2, font=("Arial", 12),command=self.content)
        self.back_button.place(x=80, y=90)

        #  ------------Runs inventory mechanics------------------
        self.show_cat_inventory()

    def arena_menu(self,event):
        #  ------------Variable for esc key------------------
        self.in_menu = True
        print("arena/dungeon entered")                                      #debug only            #i dont still know how to exactly name it - could be both :/
        #  ------------CHECK AREA FOR CLEARING------------------
        self.clear_screen()

        #  ------------Setting UI------------------
        self.show_money_label(1000,30,"#003300","white")

        self.battle_button = tk.Button(text="battle",width=30,height=2, font=("Arial", 12), command=self.start_finding_opponent)             #this will switch to battle
        self.battle_button.place(relx=.5, rely=.4, anchor="center")

        self.back_button = tk.Button(text="back",width=30,height=2, font=("Arial", 12),command=self.content)                                 #switch back to main menu(not startup menu)
        self.back_button.place(relx=.5, rely=.5, anchor="center")

        img = Image.open("pictures/arena_background.png").resize((1200, 960))
        self.arena_background_img = ImageTk.PhotoImage(img)
        self.canvas.create_image(600, 480, anchor="center", image=self.arena_background_img,tag="arena_background")

    def farm_menu(self,event):
        #  ------------Variable for esc key------------------
        self.in_menu = True
        #  ------------Variable for spawning mechanics------------------
        self.in_farm = True
        print("farm entered")           #debug only
        #  ------------CHECK AREA FOR CLEARING------------------
        self.clear_screen()

        #  ------------Setting UI------------------
        self.farm_area_coords = (200, 250, 1030, 800)
        self.max_items = 5
        self.spawned_items = []
        x1,y1,x2,y2 = self.farm_area_coords

        self.farm_label = tk.Label(self, text="Farm Area", font=("Arial", 16),bg="green")
        self.farm_label.place(x=100, y=20)

        img = Image.open("pictures/farm_background.png").resize((1200, 960))
        self.farm_background_img = ImageTk.PhotoImage(img)
        self.canvas.create_image(600, 480, anchor="center", image=self.farm_background_img,tag="farm_background")

        """self.farm_ground = self.canvas.create_rectangle(x1,y1,x2,y2,outline="",fill= "green",tag = "farm_ground")"""             #debug only
        
        self.back_button = tk.Button(text="back",width=20,height=2, font=("Arial", 12),command=self.content)
        self.back_button.place(relx=.1, rely=.1, anchor="center")                      

        #  ------------Runs spawning mechanics------------------
        start_farm_spawning(self)


    def shop_menu(self,event):
        #  ------------Variable for esc key------------------
        self.in_menu = True
        print("shop entered")           #debug only
        #  ------------CHECK AREA FOR CLEARING------------------
        self.clear_screen()

        #  ------------Setting UI------------------
        """self.shop_background = self.canvas.create_rectangle(250, 100, 1200, 960, outline="", fill="grey", tags="shop_background")"""     #debug only

        self.shop_label = tk.Label(self, text="Shop Area", font=("Arial", 16),bg="lightyellow")
        self.shop_label.place(x=100, y=50)

        self.item_shop_label = tk.Label(self, text="For sale:", font=("Arial", 16),bg="lightyellow")
        self.item_shop_label.place(x=500, y=50)

        img = Image.open("pictures/shop_background.png").resize((1200, 960))
        self.shop_background_img = ImageTk.PhotoImage(img)
        self.canvas.create_image(600, 480, anchor="center", image=self.shop_background_img,tag="shop_background")

        self.show_money_label(60,200,bg="lightyellow")

        self.refresh_time_label = tk.Label(self.canvas, text="Time to restock: 00:00:00", font=("Arial", 16),bg="lightyellow")              #doesnt actually work just a concept
        self.refresh_time_label.place(x=900, y=50)                                                                                          #maybe some day i am gonna do that :)

        self.back_button = tk.Button(text="back",width=20,height=2, font=("Arial", 12),command=self.content)
        self.back_button.place(x=50, y=700)

        #  ------------Runs shop mechanics------------------
        self.display_shop_items()

    def cauldron_menu(self,event):
        #  ------------Variable for esc key------------------
        self.in_menu = True
        print("cauldron entered")                                           #debug only
        #  ------------CHECK AREA FOR CLEARING------------------
        self.clear_screen()

        #  ------------Setting UI------------------
        self.cauldron_label = tk.Label(self, text="Cauldron Area", font=("Arial", 16),bg="gray")
        self.cauldron_label.place(x=250, y=20)

        self.inventory_label = tk.Label(self, text="Inventory", font=("Arial", 16), bg="gray")
        self.inventory_label.place(x=950, y=20)

        img = Image.open("pictures/cauldron_background.png").resize((1200, 960))
        self.cauldron_background_img = ImageTk.PhotoImage(img)
        self.canvas.create_image(600, 480, anchor="center", image=self.cauldron_background_img,tag="cauldron_background")

        self.img_cauldron = ImageTk.PhotoImage(Image.open("pictures/cauldron.png"))
        self.canvas.create_image(600, 480, anchor="center", image=self.img_cauldron,tag="cauldron")

        self.cooking_button = tk.Button(text="cook",width=20,height=2, font=("Arial", 12),command=self.cook_potion)         #completes the cooking/brewing (i use cooking in code bcs it is actually cooking for me :D) to the cauldron
        self.cooking_button.place(x=50,y=300)

        self.back_button = tk.Button(text="back",width=20,height=2, font=("Arial", 12),command=self.content)
        self.back_button.place(x=50,y=700)

        #  ------------Runs inventory cooking mechanics------------------
        self.refresh_inventory_buttons()

    def show_money_label(self,x1,y1,bg="white",fg ="black"):

        self.money_text_label = tk.Label(self.canvas, text="Your money:",  font=("Arial", 16), bg= bg,fg =fg)
        self.canvas.create_window(x1, y1, window=self.money_text_label, anchor="nw")

        self.money_label = tk.Label(self.canvas,textvariable=self.player.money,font=("Arial", 16),bg= bg, borderwidth=0, fg=fg, highlightthickness=0,padx=0,pady=0)
        self.canvas.create_window(x1 + 150, y1+16, window=self.money_label)

    def main_menu(self):
        #  ------------CHECK AREA FOR CLEARING------------------
        self.clear_screen()
        #  ------------Variable for esc key------------------
        self.in_menu = True

        #  ------------Setting UI------------------

        img = Image.open("pictures/mainmenu_background.png").resize((1200, 960))
        self.img_background = ImageTk.PhotoImage(img)
        self.canvas.create_image(600, 480, anchor="center", image=self.img_background)

        self.button_start = tk.Button(text="Start",width=30,height=2, font=("Arial", 12),command=self.content)

        self.button_instructions = tk.Button(text="Instructions",width=30,height=2, font=("Arial", 12),command=self.instructions_menu)
        
        self.button_exit = tk.Button(text="Exit",width=30,height=2, font=("Arial", 12),command=exit)

        self.button_start.place(relx=.5, rely=.3, anchor="center")
        self.button_instructions.place(relx=.5, rely=.4, anchor="center")
        self.button_exit.place(relx=.5, rely=.5, anchor="center")

    def instructions_menu(self):
        #  ------------CHECK AREA FOR CLEARING------------------
        self.clear_screen()
        #  ------------Variable for esc key------------------
        self.in_menu = False

        #  ------------Setting UI------------------
        img = Image.open("pictures/mainmenu_background.png").resize((1200, 960))
        self.img_background = ImageTk.PhotoImage(img)
        self.canvas.create_image(600, 480, anchor="center", image=self.img_background)

        img = Image.open("pictures/smiley.png")
        self.cauldron_background_img = ImageTk.PhotoImage(img)
        self.canvas.create_image(600, 300, anchor="center", image=self.cauldron_background_img,tag="smiley")

        self.instructions_label = tk.Label(self, text="Enjoy playing!", font=("Arial", 16),bg="lightblue")
        self.instructions_label.place(x=540, y=600)

        self.back_button = tk.Button(text="Back",width=30,height=2, font=("Arial", 12),command=self.main_menu)

        self.back_button.place(x=460, y= 650)

        #  ------------Pop up UI------------------
        messagebox.showinfo(
    "Instructions",
    "Story:\n"
    "You are a young wizard who studied under\n"
    "a wise master.\n"
    "One day, your master vanished without a trace.\n"
    "\n"
    "Desperate to follow him, you brewed a\n"
    "teleportation potion — but something went\n"
    "terribly wrong.\n"
    "Instead of reaching your master, the potion\n"
    "transformed you into a cat!\n"
    "\n"
    "Now, with paws instead of hands, you embark\n"
    "on a perilous journey to find your beloved\n"
    "master and reverse the spell.\n"
    "\n"
    "* Press Start to begin\n"
    "* In combat, use the 'Z', 'X', 'C', 'V', 'B', 'N', and 'M' keys to cast specific spells.\n"
    "* Use the Back button to return, or press\n"
    "  Escape to go to the main menu\n"                                     #esc work only from instructions and on main game display/village
    "* If you get stuck, use cheatnote.txt"
)

    def main_menu_esc(self,event=None):
        #  ------------Esc key variable check------------------
        if not self.in_menu:
            #  ------------Returning to main menu------------------
            self.main_menu()

    def throw_item_to_cauldron(self, item):
        #  ------------Remove the item thrown by the player------------------
        self.player.throw_into_cauldron(item)
        #  ------------Refreshs inventory------------------
        self.refresh_inventory_buttons()

    def refresh_inventory_buttons(self):
        #  ------------Cleaning old buttons------------------
        for b in self.item_buttons:
            b.destroy()
        self.item_buttons.clear()

        #  ------------Creating UI inventory buttons------------------
        for idx, item in enumerate(self.player.inventory):
            button = tk.Button(self,text=item.name,width=20,command=lambda i=item: self.throw_item_to_cauldron(i))
            button.place(x=950, y=60 + idx * 40)
            self.item_buttons.append(button)

    def cook_potion(self):
        #  ------------Crafting potion------------------
        potion = self.player.craft_potion()
        #  ------------Refreshing ingredients buttons------------------
        self.refresh_inventory_buttons()
        try:
            print(f"You created: {potion.name}")                #debug only
        except:
            print("Nothing were created")                       #debug only

    def show_cat_inventory(self):
        #  ------------Turns ON scrolling------------------
        self.enable_inventory_scrollwheel()

        #  ------------Varibles for inventory items------------------
        self.cat_inventory_ids = []
        self.cat_inventory_images = []              #prevents GarbageCollector
        start_x = 780
        start_y = 90
        row_height = 110

        #  ------------Cleaning old inventory items------------------
        self.canvas.delete("inventory_item")

        #  ------------Setting inventory UI------------------
        for idx, item in enumerate(self.player.inventory):
            try:
                img_path = f"pictures/{item.name}.png"
                img = ImageTk.PhotoImage(Image.open(img_path).resize((100, 100)))
            except Exception as e:
                print(f"Error loading image for {item.name}: {e}")
                continue

            self.cat_inventory_images.append(img)

            y = start_y + idx * row_height
            tags = (f"inv_{idx}", "inventory_item")

            img_id = self.canvas.create_image(start_x, y, anchor="nw", image=img, tags=tags)
            self.cat_inventory_ids.append(img_id)

            label_id = self.canvas.create_text(start_x + 130, y + 50,text=item.name,font=("Arial", 14),fill="black",tags=tags)
            self.cat_inventory_ids.append(label_id)

            self.canvas.tag_bind(f"inv_{idx}", "<Button-1>",lambda e, it=item, self=self: self.on_inventory_click(it))

        self.inventory_offset_y = 0
        #  ------------Cleaning UI out of visible area------------------
        self.hide_out_of_frame_items()
        #  ------------Update scrolling area------------------
        self.update_inventory_scrollregion()

    def update_inventory_scrollregion(self):
        height = max(len(self.player.inventory) * 110 + 180, self.canvas.winfo_height())
        width = self.canvas.winfo_width()
        self.canvas.config(scrollregion=(0, 0, width, height))

    def scroll_inventory(self, dy):
        dy = -dy
        total_height = max(len(self.player.inventory) * 110 + 180, self.canvas.winfo_height())
        canvas_height = self.canvas.winfo_height()

        new_offset = self.inventory_offset_y + dy
        upper_limit = 0
        lower_limit = -(total_height - canvas_height)

        # sets offset
        if new_offset > upper_limit:
            new_offset = upper_limit
        elif new_offset < lower_limit:
            new_offset = lower_limit

        dy_to_move = new_offset - self.inventory_offset_y

        if dy_to_move != 0:
            self.canvas.move("inventory_item", 0, dy_to_move)
            self.inventory_offset_y += dy_to_move

        self.hide_out_of_frame_items()

    def enable_inventory_scrollwheel(self):

        def on_mousewheel(event):
            if event.delta:  # Windows / Mac
                self.scroll_inventory(int(-event.delta / 120) * 20)
            else:  # Linux: event.num == 4 or 5
                if event.num == 4:
                    self.scroll_inventory(50)
                elif event.num == 5:
                    self.scroll_inventory(-50)

        self.canvas.bind_all("<MouseWheel>", on_mousewheel)      # Win/Mac
        self.canvas.bind_all("<Button-4>", on_mousewheel)        # Linux
        self.canvas.bind_all("<Button-5>", on_mousewheel)
            
    def on_inventory_click(self, item):                          #debug only
        print(f"Clicked inventory item: {item.name}")

    def hide_out_of_frame_items(self):
        canvas_height = self.canvas.winfo_height()
        TOP_MARGIN = 90  #padding top
        BOTTOM_MARGIN = canvas_height - 110  #bottom padding 

        for item in self.canvas.find_withtag("inventory_item"):
            coords = self.canvas.coords(item)
            # coords returns [x1, y1, x2, y2]
            y_pos = (coords[1] + coords[3]) / 2 if len(coords) >= 4 else coords[1]

            if y_pos < TOP_MARGIN or y_pos > BOTTOM_MARGIN:
                self.canvas.itemconfigure(item, state='hidden')
            else:
                self.canvas.itemconfigure(item, state='normal')
    
    def display_shop_items(self):
        #  ------------Variables for items on stock------------------
        self.shop_items = []
        self.item_labels = []
        self.buy_buttons = []

        start_y = 200
        spacing_y = 60

        #  ------------Items on stock UI------------------
        for i in range(5):                  # Show 5 random items, could be even more in the future
            item = random_item()
            self.shop_items.append(item)

            label = tk.Label(self, text=f"{item.name} - ${item.cost}", font=("Arial", 14), bg="lightyellow")
            label.place(x=400, y=start_y + i * spacing_y)
            self.item_labels.append(label)

            buy_button = tk.Button(self, text="Buy", command=lambda i=item: self.buy_item(i))
            buy_button.place(x=600, y=start_y + i * spacing_y)
            self.buy_buttons.append(buy_button)

    def buy_item(self, item):
        #  ------------Money check------------------
        if self.player.money.get() >= item.cost:
            #  ------------Money transfer------------------
            self.player.money.set(self.player.money.get() - item.cost)
            #  ------------Item transfer------------------
            self.player.inventory.append(item)

            print(f"Bought {item.name}")                #debug only
        else:
            print("Not enough money!")                  #debug only

    def start_finding_opponent(self):
        #  ------------CHECK AREA FOR CLEARING------------------
        self.clear_screen()
        #  ------------Setting UI------------------
        self.finding_label = tk.Label(self.canvas, text="Finding opponent...", font=("Arial", 16), bg="#003300",fg="white")
        self.finding_label.place(relx=0.5, rely=0.5, anchor="center")

        img = Image.open("pictures/arena_background.png").resize((1200, 960))
        self.arena_background_img = ImageTk.PhotoImage(img)
        self.canvas.create_image(600, 480, anchor="center", image=self.arena_background_img,tag="finding_background")

        # After 2 seconds, starts combat
        
        def begin():
            self.finding_label.destroy()
            self.start_combat()
        #  ------------Timer to switch UI------------------
        self.after(2000,begin)
    
    def start_combat(self):
        #  ------------CHECK AREA FOR CLEARING------------------
        self.clear_screen()
        print("Combat started!")            #debug only

        #  ------------Variables for fighting------------------
        self.enemy = Enemy(health_points=random.randint(15,30), attack_damage=random.randint(1,7))
        self.player.hp = 20
        self.input_buffer = ""
        self.player_turn = False
        self.combo_timer_id = None
        self.max_combo_length = 6

        #  ------------Setting UI------------------
        self.combo_label = tk.Label(self.canvas, text="", font=("Arial", 14), bg="yellow")
        self.canvas.create_window(600, 100, window=self.combo_label)

        print("Player HP:", getattr(self.player, "hp", "player not ready"))
        print("Enemy HP:", getattr(self.enemy, "hp", "enemy not ready"))
        print("Enemy ATK:", getattr(self.enemy, "atk"))                      #debug check


        img = Image.open("pictures/arena_background.png").resize((1200, 960))
        self.fighting_background_img = ImageTk.PhotoImage(img)
        self.canvas.create_image(600, 480, anchor="center", image=self.fighting_background_img,tag="fighting_background")

        img = Image.open("pictures/cat.png").resize((500, 620))
        self.img_cat = ImageTk.PhotoImage(img)
        self.canvas.create_image(250, 500, anchor="center", image=self.img_cat,tag="cat")

        img = Image.open("pictures/monster.png").resize((500, 620))
        self.img_monster = ImageTk.PhotoImage(img)
        self.canvas.create_image(950, 500, anchor="center", image=self.img_monster,tag="monster")
        #GC tweak

        self.player_hp_label = tk.Label(self.canvas, text=f"Player HP: {self.player.hp}", font=("Arial", 16), bg="lime")
        self.canvas.create_window(250, 750, window=self.player_hp_label)

        self.enemy_hp_label = tk.Label(self.canvas, text=f"Enemy HP: {self.enemy.hp}", font=("Arial", 16), bg="red")
        self.canvas.create_window(900, 750, window=self.enemy_hp_label)

        #  ------------Combat logic start------------------
        start_player_turn(self)
    
    def clear_screen(self):
        #  ------------CHECK AREA FOR CLEARING------------------
        # Successfully deletes all items and creating new canvas if unsuccessfull
        if hasattr(self, "canvas"):
            try:
                self.canvas.delete("all")
            except tk.TclError:
                print("Canvas exists but was destroyed. Recreating.")
                self.canvas = tk.Canvas(self, width=1200, height=960)
                self.canvas.pack()
        else:
            print("Canvas not found. Creating new canvas.")
            self.canvas = tk.Canvas(self, width=1200, height=960)
            self.canvas.pack()

        widgets_to_forget = [
            "button_start",
            "button_instructions",
            "instructions_label",
            "button_exit",
            "button_sound",
            "battle_button",
            "cooking_button",
            "back_button",
            "cauldron_label",
            "inventory_label",
            "item_id",
            "character_label",
            "refresh_time_label",
            "shop_label",
            "farm_label",
            "item_shop_label",
            "combo_label",          
            "player_hp_label",       
            "enemy_hp_label", 
        ]

        for attr in widgets_to_forget:
            widget = getattr(self, attr, None)
            if widget:
                try:
                    widget.place_forget()
                except Exception as e:
                    print(f"Error forgetting {attr}: {e}")

        if hasattr(self, "item_buttons"):
            for btn in self.item_buttons:
                try:
                    btn.destroy()
                except Exception as e:
                    print(f"Error destroying button: {e}")
            self.item_buttons.clear()

        if hasattr(self, "item_labels"):
            for lbl in self.item_labels:
                try:
                    lbl.destroy()
                except Exception as e:
                    print(f"Error destroying label: {e}")
            self.item_labels.clear()
        if hasattr(self, "buy_buttons"):
            for btn in self.buy_buttons:
                try:
                    btn.destroy()
                except Exception as e:
                    print(f"Error destroying button: {e}")
            self.buy_buttons.clear()
        if hasattr(self, "cat_inventory_widgets"):
            for lbl in self.cat_inventory_widgets:
                try:
                    lbl.destroy()
                except Exception as e:
                    print(f"Error destroying cat_inventory widget: {e}")
            self.cat_inventory_widgets.clear()

"""Window()"""            #starting the window/program - its modular can be started in other file...




   