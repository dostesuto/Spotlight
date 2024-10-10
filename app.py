import os
import tkinter as tk
import keyboard
import subprocess
import re
from PIL import Image, ImageTk, ImageDraw

def search_files_apps(query):
    search_directories = [
        "C:\\Program Files",
        os.path.expanduser("~\\Documents")
    ]
    results = []

    for search_directory in search_directories:
        for root, dirs, files in os.walk(search_directory):
            for file in files:
                if query.lower() in file.lower():
                    results.append(os.path.join(root, file))
            for dir in dirs:
                if query.lower() in dir.lower():
                    results.append(os.path.join(root, dir))

    return results

def handle_search(event=None):
    query = entry.get().strip()
    result_list.delete(0, tk.END)
    if query:
        if re.match(r'^\d+[\+\-\*/]\d+$', query):
            try:
                result = eval(query)
                result_list.insert(tk.END, f"計算結果: {result}")
            except Exception as e:
                result_list.insert(tk.END, f"計算エラー: {e}")
        else:
            results = search_files_apps(query)
            if results:
                for result in results[:10]:
                    result_list.insert(tk.END, result)
            else:
                result_list.insert(tk.END, "検索結果が見つかりませんでした。")
    else:
        result_list.insert(tk.END, "検索ワードを入力してください。")

def open_in_explorer(event):
    try:
        selected = result_list.get(result_list.curselection())
        subprocess.run(['explorer', '/select,', selected])
    except tk.TclError:
        pass

def show_search_window():
    root.deiconify()
    entry.focus_set()

def hide_search_window(event=None):
    root.withdraw()

try:
    root = tk.Tk()
    root.title("Spotlight-like Search")
    
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 600
    window_height = 200
    
    x_cordinate = int((screen_width / 2) - (window_width / 2))
    y_cordinate = int((screen_height / 2) - (window_height / 2))
    
    root.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

    root.overrideredirect(True)
    root.attributes("-topmost", True)
    root.attributes("-alpha", 0.5)

    search_box_canvas = tk.Canvas(root, width=600, height=50, highlightthickness=0, bg='white')
    search_box_canvas.place(x=0, y=0)

    entry = tk.Entry(root, font=("Arial", 18), bd=0, bg='white', fg='black', justify="center")
    entry.place(x=50, y=10, width=500, height=30)
    entry.bind("<Return>", handle_search)

    result_list = tk.Listbox(root, font=("Arial", 14), fg="black", bg="white", relief="flat", height=5)
    result_list.place(x=50, y=80, width=500, height=100)
    result_list.bind("<Double-Button-1>", open_in_explorer)

    keyboard.add_hotkey('ctrl+space', show_search_window)
    root.bind("<Escape>", hide_search_window)

    root.mainloop()

except Exception as e:
    print(f"エラーが発生しました: {e}")
