import tkinter as tk

def verifier():
    mot_de_passe = password.get()

    if len(mot_de_passe) < 6:
        resultat.config(text="Faible ❌")
    else:
        resultat.config(text="Assez fort ✅")

window = tk.Tk()
window.title("Password Checker")
window.geometry("400x250")

tk.Label(window, text="Password Checker").pack(pady=20)

password = tk.Entry(window, show="*")
password.pack()

tk.Button(window, text="Vérifier", command=verifier).pack(pady=15)

resultat = tk.Label(window, text="")
resultat.pack()

window.mainloop()
