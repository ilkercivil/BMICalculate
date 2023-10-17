import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        height = float(entry_height.get())
        weight = float(entry_weight.get())

        bmi = weight / (height ** 2)

        result_label.config(text=f"Vücut Kitle İndeksi (VKİ): {bmi:.2f}")
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli boy ve kilo değerleri girin.")

# GUI oluşturma
root = tk.Tk()
root.title("Vücut Kitle İndeksi Hesaplama")

# Etiketler
label_height = tk.Label(root, text="Boy (metre):")
label_height.grid(row=0, column=0, padx=10, pady=5)
label_weight = tk.Label(root, text="Kilo (kg):")
label_weight.grid(row=1, column=0, padx=10, pady=5)

# Giriş kutuları
entry_height = tk.Entry(root)
entry_height.grid(row=0, column=1, padx=10, pady=5)
entry_weight = tk.Entry(root)
entry_weight.grid(row=1, column=1, padx=10, pady=5)

# Hesapla butonu
calculate_button = tk.Button(root, text="Hesapla", command=calculate_bmi)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

# Sonuç etiketi
result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2, pady=5)

root.mainloop()

