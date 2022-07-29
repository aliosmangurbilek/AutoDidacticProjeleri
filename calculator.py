import tkinter as tk

yazi_font = ("Arial", 40 ,"bold")
rakam_font = ("Arial", 24, "bold")
class Calculator:
    def __init__(self):
        self.pencere = tk.Tk()
        self.pencere.geometry("375x667")
        self.pencere.resizable(0, 0)
        self.pencere.title("Hesap Makinesi")

        self.sonuc = ""
        self.current_expression = ""
        self.ekran_frame = self.ekran_frame_olustur()

        self.son_label,  self.label = self.ekran_label()

        self.rakamlar = {7: (1, 1), 8: (1, 2), 9: (1, 3),                                     #Rakamları sözlük düzeninde girdim.
                         4: (2, 1), 5: (2, 2), 6: (2, 3),
                         1: (3, 1), 2: (3, 2), 3: (3, 3),
                         0: (4, 2), ".": (4, 1),}

        self.oparatorler = {"/": "/","*": "x", "+": "+", "-": "-"}
        self.buton_frame = self.buton_frame_olustur()
        self.buton_frame.rowconfigure(0, weight=1)
        for i in range(1,5):
            self.buton_frame.rowconfigure(i, weight= 1)                                # Rowconfigure verdiğimiz ağırlıga göre satır boyutlandırma yapar.
            self.buton_frame.columnconfigure(i, weight=1)                              # Columnconfigure ise verdiğimiz ağırlığa göre sütun boyutlandırma yapar.
        self.rakamlari_olustur()
        self.oparator_butonu_olustur()
        self.ozel_butonlar()

    def ozel_butonlar(self):
        self.esittir_butonu()
        self.komple_sil_buton()

                                                                                        # Pencere aracı olarak label kullandım.
    def ekran_label(self):                                                              # Ekranımızı oluşturan fonksiyon
        son_label = tk.Label(self.ekran_frame, text = self.sonuc, anchor = tk.E, bg = "WHITE", fg = "BLACK", padx = 24, font = yazi_font)      # Anchor metnin taşarsa ne olacağını ayarlar.                                                                                 # Padx metnin sağına ve soluna extra boşluk ekler.
        son_label.pack(expand = True, fill="both")                                      # Expand ekran genişlese bile ekranı doldurur.

        label = tk.Label(self.ekran_frame, text=self.current_expression, anchor=tk.E, bg="WHITE",fg="BLACK", padx=24, font= yazi_font)
        label.pack(expand=True, fill='both')

        return son_label, label

    def ekran_frame_olustur(self):                                                      # Pencere aracı olarak Frame kullandım.
        frame = tk.Frame(self.pencere, height=221, bg = "RED")                          # Yükseklik ve arka plan rengini tanımladım.
        frame.pack(expand = True, fill="both")                                          # Expand ekran genişlese bile ekranı doldurur.
        return frame

    def add_to_expression(self, deger):
        self.current_expression += str(deger)
        self.update_label()

    def rakamlari_olustur(self):
        for rakam,izgara_degeri in self.rakamlar.items():                               # İtems metodu bir sözlüğün hem anahtarlarını hem de değerlerini aynı anda almamızı sağlar.
            buton = tk.Button(self.buton_frame, text=str(rakam), bg = "WHITE", fg = "BLACK", font = rakam_font, borderwidth=5, command = lambda x=rakam: self.add_to_expression(x)) # Lambda fonksiyonu ise fonksiyon içinde fonksiyon tanımlamamıza olanak sağlar.
            buton.grid(row = izgara_degeri[0], column = izgara_degeri[1], sticky = tk.NSEW)   #Grid metodu ızgara şeklinde sıralar. Sticky metodu hücreye girilen değer hücreden büyükse öğeyi ortalar.

    def operator_ekle(self,operator):
        self.current_expression += operator
        self.sonuc += self.current_expression
        self.current_expression=""
        self.update_total_label()
        self.update_label()

    def temizle(self):
        self.current_expression=""
        self.sonuc=""
        self.update_label()
        self.update_total_label()

    def komple_sil_buton(self):
        buton = tk.Button(self.buton_frame, text=str("C"), bg="WHITE", fg="BLACK", font=rakam_font, borderwidth=5, command=self.temizle)
        buton.grid(row = 0, column = 1, columnspan = 3, sticky = tk.NSEW)

    def değerle(self):
        self.sonuc += self.current_expression
        self.update_total_label()

        self.current_expression = str(eval(self.sonuc))    # Eval fonksiyonu matematiksel işlemleri kendi değerlendirip sonuç veren bir fonksiyondur

        self.sonuc= ""
        self.update_label()

    def esittir_butonu(self):
        buton = tk.Button(self.buton_frame, text=str("="), bg="WHITE", fg="BLACK", font=rakam_font, borderwidth=5, command=self.değerle)
        buton.grid(row = 4, column = 3, columnspan = 2, sticky = tk.NSEW)

    def buton_frame_olustur(self):
        frame = tk.Frame(self.pencere)
        frame.pack(expand = True, fill="both")
        return frame

    def oparator_butonu_olustur(self):
        a = 0
        for oparator,sembol in self.oparatorler.items():
            buton = tk.Button(self.buton_frame, text=str(sembol), bg="WHITE", fg="BLACK", font=rakam_font, borderwidth=5, command=lambda x=oparator:self.operator_ekle(x))
            buton.grid(row = a, column = 4, sticky = tk.NSEW)
            a += 1

    def update_total_label(self):
        ifade = self.sonuc
        self.son_label.config(text=ifade)

    def update_label(self):
        self.label.config(text=self.current_expression) # config komutu ile butona tıklanıldığında vereceği tepkiyi ayarladım.



    def run(self):
        self.pencere.mainloop()


if __name__ == "__main__": #fonksiyon çağrıldığında ismi farklı görünür.
    calc = Calculator()
    calc.run()
##eval kullan
