## 画像投稿

画像投稿機能を作るときは以下のライブラリをインストール

```xml
pip install pillow
```

## formのポスト先

`action` を省略したフォームは「現在のURL」にPOSTされる

## 主なコマンド

### プロジェクト作成

```xml
django-admin startproject プロジェクト名
```

### アプリ作成

```xml
python manage.py startapp アプリ名
```

### サーバー起動

```xml
python manage.py runserver
```

### マイグレーションファイルの作成

```xml
python3 manage.py makemigrations 
```

### マイグレーションの実行

```xml
python3 manage.py migrate 
```

## デバッグ

止めたい場所で以下を記述する。htmlには書けない

```xml
import pdb; pdb.set_trace()
```