# Spotlightもどき
windowsで動く、Spotlightもどきを適当に作った。(PowerToysのほうがまし)

# Downlord
[downlord](https://github.com/dostesuto/Spotlight/releases/tag/spotsearch)
# 使い方
まず、「app.exe」を[ダウンロード](https://github.com/dostesuto/Spotlight/releases/tag/spotsearch)し(バグがあるから、app.pyのほうがいいかも)、アプリを起動する。(app.pyの方はcmdで「pip install Pillow」を打って、pillowをインストールしといてください。)
次に、「Ctrl+space」でSpotlightが起動します。
閉じるには、「Esc」で閉じます。

# 機能
基本的にはSpotlightと同じ(Spotlightの下位互換)。ファイルを検索したり、電卓を使ったりできる。





# 主要な機能と構造

**インポートセクション**

必要なモジュールをインポートしています。os, tkinter, keyboard, subprocess, re, PIL（Python Imaging Library）などが含まれています。

**ファイル検索関数 (search_files_apps):**

指定されたクエリに基づいて、特定のディレクトリ（C:\Program Files とユーザーのドキュメントフォルダ）内のファイルとフォルダを再帰的に検索します。
一致するファイルやフォルダのパスをリストに追加して返します。

**検索処理関数 (handle_search):**

ユーザーが入力した検索クエリを処理します。
入力が数式である場合、evalを使って計算し、結果を表示します。
数式でない場合は、search_files_apps関数を呼び出してファイルやフォルダを検索し、最大10件の結果をリストに表示します。

**エクスプローラーでの開放 (open_in_explorer):**

検索結果リストでダブルクリックした項目を、Windowsエクスプローラーで選択状態で開きます。

**ウィンドウ表示・非表示関数:**

show_search_windowでウィンドウを表示し、hide_search_windowでウィンドウを非表示にします。Ctrl + Spaceのホットキーでウィンドウを表示し、Escapeキーで非表示にします。

**GUIの設定:**

Tkinterを使ってウィンドウを作成します。
ウィンドウのサイズ、位置、透明度、最前面表示を設定します。
検索バー（Entry）と検索結果リスト（Listbox）を配置します。

**メインループ**

Tkinterのメインループを開始して、ユーザーからの入力やイベントを待ち受けます。

# 全体の流れ

    アプリを起動すると、透明なウィンドウが画面の中央に表示されます。
    ユーザーがCtrl + Spaceを押すとウィンドウが表示され、検索バーにクエリを入力できます。
    エンターキーを押すと、検索が実行され、結果がリストに表示されます。計算式の場合はその結果が表示されます。
    結果をダブルクリックすると、Windowsエクスプローラーでそのファイルやフォルダを開きます。
    Escapeキーでウィンドウを非表示にできます。
