# README
## このアプリでできること
* ユーザー登録
* 画像生成AIを試せる
＊ AI開発会社一覧から、自分が開発したい会社を探せる、登録できる

## 開発言語
* Python 3.12.2+
* Django 4.2.7

## 実行手順
下記ターミナルで実行

```
$ git clone git@github.com:tsuru-ken/AIventure.git
$ cd AIventure
$ python -m venv env
$ source env/bin/activate  # Windowsでは `env\Scripts\activate`
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py loaddata initial_data.json  # またはカスタムスクリプト `python manage.py shell < seed_data.py`
$ python manage.py runserver
```

## カタログ設計, テーブル設計
https://docs.google.com/spreadsheets/d/1MqlPDyp3nqfJNQOZeujCLLJ-UnkzQBSswSWR4RiOUgA/edit?gid=1347183152#gid=1347183152

## ワイヤーフレーム
raw.ioリンク
https://app.diagrams.net/#G1MNwId0UPE0toT7FBSxvm1Ss1MfcRAu0o#%7B%22pageId%22%3A%2203018318-947c-dd8e-b7a3-06fadd420f32%22%7D


## ER図　
raw.ioリンク
https://app.diagrams.net/#G184uY-uuYTlHFZS6ao5c4Sky0D3UVyfsJ#%7B%22pageId%22%3A%22R2lEEEUBdFMjLlhIrx00%22%7D
<img width="1069" alt="ER図" src="https://github.com/tsuru-ken/AIventure/assets/112688051/e82055d2-2025-4cc5-813d-2edf35ab48a7">


## 画面遷移図
draw.ioリンク
https://app.diagrams.net/#G1U4dy4ENPh661sTDGtwJl7VwjsYlE2cqf#%7B%22pageId%22%3A%22jW9cVpwIbL73UsxvOSUH%22%7D
<img width="1201" alt="AI Venture画面遷移図" src="https://github.com/tsuru-ken/AIventure/assets/112688051/a349ae51-dff6-4c24-9a6b-632c8db3e5d9">

