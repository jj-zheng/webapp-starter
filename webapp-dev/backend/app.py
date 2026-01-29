from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

# TODO(演習): psycopg2 を使って DB 接続関数 get_conn() を実装する
# 環境変数：DB_HOST, DB_NAME, DB_USER, DB_PASS を利用すること

# TODO(演習): GET / で notes 一覧を取得して index.html に渡す（Read）
# TODO(演習): POST /notes で新規メモ追加（Create）
# TODO(演習): GET /notes/<id>/edit（編集画面）
# TODO(演習): POST /notes/<id>/edit（Update）

if __name__ == "__main__":
    # TODO(演習): host=0.0.0.0, port=5000 で起動できるようにする
    app.run()