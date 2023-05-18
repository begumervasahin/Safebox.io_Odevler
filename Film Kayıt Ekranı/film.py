import tkinter as tk
import json

def film_Ekle():
    movie = {
        "FilmAd": entry.get(),
        "turler": genre_entry.get().split(",")
    }
    movie_list.insert(tk.END, movie["FilmAd"])
    entry.delete(0, tk.END)
    genre_entry.delete(0, tk.END)
    movie_library.append(movie)
    kaydet()

def film_Ara():
    query = entry.get()
    movie_list.delete(0, tk.END)
    for movie in movie_library:
        if query.lower() in movie["FilmAd"].lower():
            movie_list.insert(tk.END, movie["FilmAd"])

def film_Sil():
    selected_movie = movie_list.get(tk.ACTIVE)
    movie_list.delete(tk.ACTIVE)
    for movie in movie_library:
        if movie["FilmAd"] == selected_movie:
            movie_library.remove(movie)
            break
    kaydet()

def kaydet():
    with open("movie_library.json", "w") as file:
        json.dump(movie_library, file, indent=4)  # JSON dosyasına düzgün bir biçimlendirme eklemek için indent parametresini kullandık

def yükle():
    try:
        with open("movie_library.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


movie_library = yükle()

window = tk.Tk()
window.title("Film Arama Ekranı")

window.geometry("600x500")


label = tk.Label(window, text="Film Adı:", bg="#c9ead5")
label.pack()


entry = tk.Entry(window)
entry.pack()


genre_label = tk.Label(window, text="Film Türleri (Virgülle Ayırarak Girin):", bg="#c9ead5")
genre_label.pack()


genre_entry = tk.Entry(window)
genre_entry.pack()


add_button = tk.Button(window, text="Film Ekle", command=film_Ekle, bg="#C8E6C9")
add_button.pack()


search_button = tk.Button(window, text="Film Ara", command=film_Ara, bg="#C8E6C9")
search_button.pack()


delete_button = tk.Button(window, text="Film Sil", command=film_Sil, bg="#C8E6C9")
delete_button.pack()


movie_list = tk.Listbox(window,bg="white",width=100)
movie_list.pack()

for movie in movie_library:
    movie_list.insert(tk.END, movie["FilmAd"])
  
window.configure( bg="#c9ead5")

window.mainloop()
