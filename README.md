# テック塾 テスト駆動開発実習コード

## 目次

- [使用技術](#使用技術)
- [環境構築の手順](#環境構築の手順)
- [コマンド](#コマンド)
- [ディレクトリ構造](#ディレクトリ構造)

## 使用技術

### bff

- Python 3.12
- FastAPI 0.109.\*

## 環境構築の手順

### 動作環境

- os
  - windws / mac / linux
- software
  - docker / docker-compose

### 初期構築

#### bff(サーバサイド)

##### どちらかを実行
###### フォアグラウンドで起動したい場合
```
% make buildup
```

###### バックグラウンドで起動したい場合
```
% make buildupd
```

##### コンテナ起動後、リンター・フォーマッターのインストール
```
% make build_dev
```

## コマンド

- `make fmt` : フォーマット実行
- `make lint` : リント実行
- `make lintf` : リント実行&修正
- `make up` : フォアグラウンド構築起動
- `make upd` : バックグラウンド構築起動
- `make start` : サービス起動
- `make stop` : サービス停止
- `make restart` : サービス再起動
- `make rm` : プロジェクト内のサービス停止してコンテナ削除
- `make rmi` : プロジェクト内のイメージ、コンテナ、ネットワークを削除
- `make logsf` : サービスからのログ出力を表示&フォロー(表示し続ける)
- `make logs` : サービスからのログ出力を表示

## ディレクトリ構造

```
/
├─ docker_images/              # コンテナ周りの設定
│   └─ app/
├─ src/
│   └─ bff/                    # サーバサイドのルート
│       ├─ api/
│       │   └─ api_v1/
│       │       └─ endpoints/  # APIの処理を記述
│       ├─ core/               # サーバサイドの基本設定・定数の管理
│       ├─ schemas/            # APIのリクエスト・レスポンスの型定義
│       ├─ utils/              # サービスの操作・汎用的な処理など
│       └─ main.py             # サーバサイドで最初に呼び出される(基本いじらない)
├─ .gitignore
├─ compose.yml                 # docker-composeファイル
├─ Makefile                    # Makeコマンド定義
└─ README.md
```
