# 情報科学演習IV 第3回 Starter（Webアプリケーション開発）

このリポジトリは「情報科学演習IV 第3回：Webアプリケーションの開発」の
スタータコードです。

## 前提環境
- Windows 学生は **WSL + VS Code（WSL 接続）** を使用してください
- 以降のコマンドは **すべて WSL 上で実行**します

## ディレクトリ構成
本演習で実際に作業するのは `webapp-dev/` ディレクトリです。

```
webapp-dev/
├── docker-compose.yml
├── backend/
│ 	├── app.py
│ 	├── Dockerfile
│ 	├── requirements.txt
│ 	└── templates/
│ 		├── index.html
│ 		└── edit.html
└── db/
	└── init.sql
```

## 含まれているもの
- ディレクトリ構成（backend / db）
- HTML テンプレート
- 空の設定ファイル（Dockerfile / requirements / compose / init.sql）

## 含まれていないもの（演習中に作成）
- Flask の実装（Create / Read / Update）
- docker-compose.yml の完成版
- DB 初期化 SQL の完成版

## 作業開始
演習資料に従って作業してください。
