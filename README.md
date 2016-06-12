# Jukusai

スマホアプリ用のバックエンドシステム
※このシステムはpythonのフレームワーク Djangoをベースに開発されている。以下に構築方法を記す

###環境構築
pyenvとvirtualenvを用いる事を推奨する

#####install

```
git clone https://github.com/yyuu/pyenv.git ~/.pyenv
git clone https://github.com/yyuu/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv
```

#####shellの設定ファイルに以下を記述する

```
export PYENV_ROOT=$HOME/.pyenv
export PATH=$PYENV_ROOT/bin:$PATH
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

#####本体のインストールとpython3.5

```
pyenv install 3.5.0
pyenv virtualenv 3.5.0 jukusai
git clone https://github.com/Alice-tech/AliceAnimeServer.git
```

#####pythonライブラリ

```
pip install -r requrements.txt
```

###テスト

* DB初期化

```
python manage.py migrate
```

* スーパーユーザー作成

```
python manage.py createsuperuser
```


* テストサーバー起動

```
python manage.py runserver
```


#####Project Tree

```
.
├── Jukusai
│   ├── __init__.py
│   ├── __init__.pyc
│   ├── __pycache__
│   ├── jsonResponse.py
│   ├── paginator.py
│   ├── settings.py
│   ├── settings.pyc
│   ├── urls.py
│   └── wsgi.py
├── README.md
├── db.sqlite3
├── manage.py
├── program
│   ├── __init__.py
│   ├── __pycache__
│   ├── admin.py
│   ├── migrations
│   ├── models.py
│   ├── programSerializer.py
│   ├── tests.py
│   └── views.py
└──requrements.txt


6 directories, 39 files
```




