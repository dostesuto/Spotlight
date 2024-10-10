import os
import tkinter as tk
import keyboard
import subprocess
import re  # 正規表現モジュールをインポート
from PIL import Image, ImageTk, ImageDraw

# 検索結果を表示する関数
def search_files_apps(query):
    search_directories = [
        "C:\\Program Files",
        os.path.expanduser("~\\Documents")
    ]
    results = []

    # ファイルやフォルダの検索
    for search_directory in search_directories:
        for root, dirs, files in os.walk(search_directory):
            for file in files:
                if query.lower() in file.lower():
                    results.append(os.path.join(root, file))
            for dir in dirs:
                if query.lower() in dir.lower():
                    results.append(os.path.join(root, dir))

    return results

# 検索を処理して結果を表示
def handle_search(event=None):
    query = entry.get().strip()
    result_list.delete(0, tk.END)  # 結果をリセット
    if query:
        # 計算式かどうかを確認
        if re.match(r'^\d+[\+\-\*/]\d+$', query):  # 構文をチェック
            try:
                result = eval(query)  # 数式を評価
                result_list.insert(tk.END, f"計算結果: {result}")
            except Exception as e:
                result_list.insert(tk.END, f"計算エラー: {e}")
        else:
            results = search_files_apps(query)
            if results:
                for result in results[:10]:  # 最大10件表示
                    result_list.insert(tk.END, result)
            else:
                result_list.insert(tk.END, "検索結果が見つかりませんでした。")
    else:
        result_list.insert(tk.END, "検索ワードを入力してください。")

# 検索結果をダブルクリックしたときにエクスプローラーで開く
def open_in_explorer(event):
    try:
        selected = result_list.get(result_list.curselection())  # 選択された項目を取得
        subprocess.run(['explorer', '/select,', selected])  # エクスプローラーで開く
    except tk.TclError:
        pass  # 何も選択されていない場合はエラーを無視

# ウィンドウを表示
def show_search_window():
    root.deiconify()  # ウィンドウを表示
    entry.focus_set()

# ウィンドウを非表示
def hide_search_window(event=None):
    root.withdraw()

# GUIの設定
try:
    root = tk.Tk()
    root.title("Spotlight-like Search")
    
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 600
    window_height = 200
    
    # 中央にウィンドウを配置
    x_cordinate = int((screen_width / 2) - (window_width / 2))
    y_cordinate = int((screen_height / 2) - (window_height / 2))
    
    root.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

    # ウィンドウの透明度と見た目の設定
    root.overrideredirect(True)  # ウィンドウフレームを非表示
    root.attributes("-topmost", True)  # 常に最前面に表示
    root.attributes("-alpha", 0.5)  # ウィンドウを半透明に

    # 検索ボックスのキャンバスを作成
    search_box_canvas = tk.Canvas(root, width=600, height=50, highlightthickness=0, bg='white')
    search_box_canvas.place(x=0, y=0)

    # 検索バーのデザイン
    entry = tk.Entry(root, font=("Arial", 18), bd=0, bg='white', fg='black', justify="center")
    entry.place(x=50, y=10, width=500, height=30)
    entry.bind("<Return>", handle_search)

    # 検索結果リストのデザイン（透明にしない）
    result_list = tk.Listbox(root, font=("Arial", 14), fg="black", bg="white", relief="flat", height=5)
    result_list.place(x=50, y=80, width=500, height=100)
    result_list.bind("<Double-Button-1>", open_in_explorer)  # ダブルクリックでエクスプローラーを開く

    # ウィンドウ表示のホットキー (Ctrl + Space)
    keyboard.add_hotkey('ctrl+space', show_search_window)

    # Escapeキーでウィンドウを非表示
    root.bind("<Escape>", hide_search_window)

    # Tkinterメインループ
    root.mainloop()

except Exception as e:
    print(f"エラーが発生しました: {e}")
