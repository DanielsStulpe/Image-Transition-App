#Tkinter bibliotēkas importēšana GUI izveidei
import tkinter as tk
from tkinter import filedialog
#Pillow importēšana attēlu apstrādei
from PIL import Image, ImageTk

class ImageTransitionApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Attēlu Pārejas lietotne")

        # Iestatām sākotnējo loga izmērus
        window_width = 1356
        window_height = 525
        
        # Iestatām sākotnējo loga novietojumu lietotāja ekrāna centrā
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2
        self.master.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        # Uzstādām fona krāsu
        self.master.configure(bg="#1f1f1f")

        # Aizliedzam loga izmēru mainīšanu
        self.master.resizable(False, False)

        # Attēli
        self.image1_path = ""
        self.image2_path = ""
        self.image1 = Image.new("RGB", (400, 400), "white")  # Pēc noklusējuma - balts kvadrāts
        self.image2 = Image.new("RGB", (400, 400), "white")  # Pēc noklusējuma - balts kvadrāts
        self.photo1 = self.get_image_tk(self.image1)
        self.photo2 = self.get_image_tk(self.image2)

        # Pievienojam label tekstam virs katram attēlam
        self.label_text1 = tk.Label(self.master, text="Image 1", bg="#1f1f1f", fg="white")
        self.label_text2 = tk.Label(self.master, text="Image 2", bg="#1f1f1f", fg="white") 
        self.label_text3 = tk.Label(self.master, text="Animation", bg="#1f1f1f", fg="white")

        self.label_text1.grid(row=0, column=0, padx=5, pady=4, sticky="s")
        self.label_text2.grid(row=0, column=4, padx=5, pady=4, sticky="s")
        self.label_text3.grid(row=0, column=2, padx=5, pady=4, sticky="s")

        # Vizuālais interfeiss, kur būs redzami 2 attēli un animācija
        self.label1 = tk.Label(self.master, image=self.photo1, bg="#d9d9d9")
        self.label2 = tk.Label(self.master, image=self.photo2, bg="#d9d9d9")
        self.label3 = tk.Label(self.master, image=self.photo1, bg="#d9d9d9")

        self.label1.grid(row=1, column=0, padx=5, pady=5)
        self.label2.grid(row=1, column=4, padx=5, pady=5)
        self.label3.grid(row=1, column=2, padx=5, pady=5)

        # Pogas attēlu izvēlei
        self.button_choose1 = tk.Button(self.master, text="Load image 1", command=self.choose_image1, bg="#2F4F4F", fg="white")
        self.button_choose2 = tk.Button(self.master, text="Load image 2", command=self.choose_image2, bg="#2F4F4F", fg="white")
        self.button_choose3 = tk.Button(self.master, text="Shuffle", command=self.shuffle, bg="#2e6666", fg="white")

        self.button_choose1.grid(row=2, column=0, padx=5, pady=5)
        self.button_choose2.grid(row=2, column=4, padx=5, pady=5)
        self.button_choose3.grid(row=2, column=2, padx=5, pady=5)

        # Pogas animācijas izvēlei
        self.button1 = tk.Button(self.master, text="Swipe", command=lambda: self.animate("swipe"), bg="#251f4f", fg="white")
        self.button2 = tk.Button(self.master, text="Curtain", command=lambda: self.animate("curtain"), bg="#251f4f", fg="white")
        self.button3 = tk.Button(self.master, text="Fade", command=lambda: self.animate("fade"), bg="#251f4f", fg="white")
        self.button4 = tk.Button(self.master, text="Shape", command=lambda: self.animate("shape"), bg="#251f4f", fg="white")
        self.button5 = tk.Button(self.master, text="Snail", command=lambda: self.animate("snail"), bg="#251f4f", fg="white")

        self.button1.grid(row=3, column=0, padx=5, pady=5)
        self.button2.grid(row=3, column=1, padx=5, pady=5)
        self.button3.grid(row=3, column=2, padx=5, pady=5)
        self.button4.grid(row=3, column=3, padx=5, pady=5)
        self.button5.grid(row=3, column=4, padx=5, pady=5)


    # Iegūst attēla objektu, kas nepieciešams tkinter attēla attēlošanai
    def get_image_tk(self, image):
        return ImageTk.PhotoImage(image)
    
    # Atver failu dialogu, lai izvēlētos pirmo attēlu, mainīt tā izmērus uz 400x400 pikseļiem un atjaunina attēla rādītāju
    def choose_image1(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.image1_path = file_path
            self.image1 = Image.open(self.image1_path).resize((400, 400))
            self.photo1 = self.get_image_tk(self.image1)
            self.label1.configure(image=self.photo1)
            self.label3.configure(image=self.photo1)

    # Atver failu dialogu, lai izvēlētos otro attēlu, mainīt tā izmērus uz 400x400 pikseļiem un atjaunina attēla rādītāju            
    def choose_image2(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.image2_path = file_path
            self.image2 = Image.open(self.image2_path).resize((400, 400))
            self.photo2 = self.get_image_tk(self.image2)
            self.label2.configure(image=self.photo2)
            
    # Apmaina vietām pirmo un otro attēlu un atjaunina attēla rādītājus
    def shuffle(self):
        self.image1, self.image2 = self.image2, self.image1
        self.photo1 = self.get_image_tk(self.image1)
        self.photo2 = self.get_image_tk(self.image2)
        self.label1.configure(image=self.photo1)
        self.label3.configure(image=self.photo1)
        self.label2.configure(image=self.photo2)

    # Izvēlas un palaiž animāciju atkarībā no izvēlētā veida       
    def animate(self, animation_type):
        if not self.image1 or not self.image2:
            return

        if animation_type == "swipe":
            self.swipe_transition()
        elif animation_type == "curtain":
            self.curtain_transition()
        elif animation_type == "fade":
            self.fade_transition()
        elif animation_type == "shape":
            self.shape_transition()
        elif animation_type == "snail":
            self.snail_transition()
            
    # Atjauno attēlu rādītāju pēc animācijas beigām       
    def reset(self):
        self.master.after(850)
        self.label3.configure(image=self.photo1)

    # Izpilda animāciju 'Swipe'   
    def swipe_transition(self):
        self.label3.configure(image=self.photo1)

        # Kopējam pikseļus no 2 attēliem
        self.image3 = self.image1.copy()
        pixel_map1 = self.image3.load()
        pixel_map2 = self.image2.load()
        
        # Katra cikla iterācija maina 10 pikseļus no augšas, no pirmā attēla uz otrā attēla pikseļiem, 
        # parāda lietotājam jauno attēlu, aizkavē 25 milisekundes un turpina ciklu
        for i in range(10, 410, 10):
            for x in range(0, 400):
                for y in range(0, i):
                    pixel_map1[x, y] = pixel_map2[x, y]

            self.photo3 = self.get_image_tk(self.image3)
            self.label3.configure(image=self.photo3) # atjaunina attēlu
            self.master.update_idletasks() # parāda to lietotājam
            self.master.after(25)  # Aizkave milisekundēs

        self.reset()

    # Izpilda animāciju 'Curtain'    
    def curtain_transition(self):
        self.label3.configure(image=self.photo1)

        # Kopējam pikseļus no 2 attēliem
        self.image3 = self.image1.copy()
        pixel_map1 = self.image3.load()
        pixel_map2 = self.image2.load()

        # Katra cikla iterācija maina 5 pikseļus no centra uz divām pusēm, no pirmā attēla uz otrā attēla pikseļiem, 
        # parāda lietotājam jauno attēlu, aizkavē 30 milisekundes un turpina ciklu
        for i in range(5, 205, 5):
            for x in range(200 - i, 200):
                for y in range(0, 400):
                    pixel_map1[x, y] = pixel_map2[x, y]
            for x in range(200, 200 + i):
                for y in range(0, 400):
                    pixel_map1[x, y] = pixel_map2[x, y]

            self.photo3 = self.get_image_tk(self.image3)
            self.label3.configure(image=self.photo3) # atjaunina attēlu
            self.master.update_idletasks() # parāda to lietotājam
            self.master.after(30)  # Aizkave milisekundēs

        self.reset()

    # Izpilda animāciju 'Shape'    
    def shape_transition(self):
        self.label3.configure(image=self.photo1)

        # Kopējam pikseļus no 2 attēliem
        self.image3 = self.image1.copy()
        pixel_map1 = self.image3.load()
        pixel_map2 = self.image2.load()

        # Katra cikla iterācija palielina apļa radiusu, ej cauri visiem pikseļiem un ja tie atrodas apļa iekšienē 
        # mainā tos uz otrā attēla pikseļiem, parāda lietotājam jauno attēlu, aizkavē 25 milisekundes un turpina ciklu
        for r in range(1, 41):
            for x in range(0, 400):
                for y in range(0, 400):
                    if (((x - 200) ** 2 + (y - 200) ** 2) < (r * 7.25) ** 2):
                        pixel_map1[x, y] = pixel_map2[x, y]

            self.photo3 = self.get_image_tk(self.image3)
            self.label3.configure(image=self.photo3) # atjaunina attēlu
            self.master.update_idletasks() # parāda to lietotājam
            self.master.after(25)  # Aizkave milisekundēs

        self.reset()

    # Izpilda animāciju 'Snail'    
    def snail_transition(self):
        self.label3.configure(image=self.photo1)

        # Kopējam pikseļus no 2 attēliem
        self.image3 = self.image1.copy()
        pixel_map1 = self.image3.load()
        pixel_map2 = self.image2.load()

        r, d, l = 4, 4, 4
        x1, y1 = 0, 0

        # Atjaunina attēlu, parāda to lietotājam, aizkavē 80 milisekundes
        def update_snail_display():
            self.photo3 = self.get_image_tk(self.image3)
            self.label3.configure(image=self.photo3) # atjaunina attēlu
            self.master.update_idletasks() # parāda to lietotājam
            self.master.after(80)  # Aizkave milisekundēs
        
        # Sadala attēlu 25 zonās pa 80x80 pikseliem un pakāpeniski kustinās pa spirāli, pa šīm zonām sākot no augšējā kreisās 
        # puses, kopējot pikseļus no otra attēla, līdz pirmā attēla zona pilnībā tiek aizvietota ar otro attēlu.
        while r > 1:
            for _ in range(r):
                for x in range(x1, x1+80):
                    for y in range(y1, y1+80):
                        pixel_map1[x, y] = pixel_map2[x, y]
                update_snail_display()
                x1 += 80

            r -= 1
            for _ in range(d):
                for x in range(x1, x1+80):
                    for y in range(y1, y1+80):
                        pixel_map1[x, y] = pixel_map2[x, y]
                update_snail_display()
                y1 += 80

            d -= 1
            for _ in range(l):
                for x in range(x1, x1+80):
                    for y in range(y1, y1+80):
                        pixel_map1[x, y] = pixel_map2[x, y]
                update_snail_display()
                x1 -= 80

            l -= 2
            for _ in range(d):
                for x in range(x1, x1+80):
                    for y in range(y1, y1+80):
                        pixel_map1[x, y] = pixel_map2[x, y]
                update_snail_display()
                y1 -= 80

            d -= 1

        self.reset()

    # Izpilda animāciju 'Fade'   
    def fade_transition(self):
        self.label3.configure(image=self.photo1)

        # Ar katru cikla iterāciju funkcija blend uzliek pirmo attēlu virs otram, izmantojot RGBA (Red,Green,Blue,alpha)
        # krāsu modeli ar krāsas intensitāti (Alpha) un samazina pirmā attēla krāsas intensitāti par 1%.
        for alpha in range(100, -1, -1):
            image = Image.blend(self.image2.convert("RGBA"), self.image1.convert("RGBA"), alpha / 100)
            self.frame = self.get_image_tk(image)
            self.label3.configure(image=self.frame) # atjaunina attēlu
            self.master.update_idletasks() # parāda to lietotājam
            self.master.after(20) # Aizkave milisekundēs
    
        self.reset()

        
# Izveido galveno logu
root = tk.Tk()
app = ImageTransitionApp(root)

# Palaiž lietotni
root.mainloop()