## 注意

setting.pyの設定、アプリを追加したら必ず操作、詳しくはsetting.pyを見る

## スーパーユーザー作成コマンド

```xml
python manage.py createsuperuser
```

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

## shell

shellに入る

```xml
python3 manage.py shell
```

### すべてのデータを取得

```python
from アプリ名.models import インポートしたいモデル(テーブル名)
これはなくてもいい

Page.objects.all()
配列で返される
表示はmodels.pyのdef __str__(self)できまる

```

### データ操作

```python
すべてを取得
Page.objects.all()

titleカラムが"ホーム"のものをすべて集める
Page.objects.filter(title="ホーム")

getで一つ取得
Page.objects.get(title="ホーム")
※ .get() は条件に一致するレコードがなければ DoesNotExist、複数あれば MultipleObjectsReturned の例外が出ます。

これで
Page.カラム名 で検索できる
さらに
Page.カラム名 = 値
Page.save()
で更新できる

新しく作る場合は
page = Page.objects.create(title='テストページ', content='これはテストページの内容です。')

✅ filter() の基本

Good.objects.filter(id=33)
条件に合うデータをQuerySet（複数レコードの集合）として返す

データが 1件でも0件でもエラーにならない

結果はリストのように扱える（ループ、.first(), .count() など）

例：
python
コピーする
編集する
# 33番のIDが存在していれば取得、なければ空リスト
results = Good.objects.filter(id=33)

for item in results:
    print(item)
    
    
    
✅ exists() の基本

Good.objects.filter(id=33).exists()
指定した条件で データが1件でも存在するかどうかだけを確認

戻り値は True または False

SQLが最適化されて軽い（SELECT 1 FROM ... LIMIT 1）

例：
python
コピーする
編集する
if Good.objects.filter(id=33).exists():
    print("データあり")
else:
    print("データなし")

```

### 最初の1件だけ取得

```python

コピーする編集する
Page.objects.first()

```

## フラッシュメッセージ

```xml
{% if messages %}
  {% for message in messages %}
    <div class="alert alert-{{ message.tags }}">
      {{ message }}
    </div>
  {% endfor %}
{% endif %}

from django.contrib import messages

def my_view(request):
    messages.success(request, 'ログインに成功しました！')
    messages.warning(request, '注意してください')
    messages.error(request, 'エラーが発生しました')
    messages.info(request, 'お知らせです')
    return redirect('home')
```

## htmlの自動生成 vscode

```xml
shift + !
```

## {{  }}と{% %}の使い分け

```xml
{{ }}は値
{% %}は値以外、forやurl 'urlname'などの制御構文で使用する

```

## python3でインストールするとき

```xml
python3 -m pip install アプリ名
```

## bootstrapの導入方法

以下を貼り付けるだけ

```xml
<!doctype html>
<html lang="ja">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap demo</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">
  </head>
  <body>
    <h1>Hello, world!</h1>
    <div class="btn btn-primary"></div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-geWF76RCwLtnZ8qwWowPQNguL3RmwHVBC9FhGdlKrxdiJJigb/j/68SIy3Te4Bkz" crossorigin="anonymous"></script>
  </body>
</html>
```

https://getbootstrap.jp/docs/5.3/examples/このページのサンプルを実現するには、上のソースコードダウンロードして、貼り付けて、

上のコードのlinkタグとスクリプトタグを読み込ませてbootstrapを読み込ませるだけ

## Jqueryを使う方法

headerかbodyの最後に以下を追加

```xml
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
```