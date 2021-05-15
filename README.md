# CP_Automation_Tools
<!-- Automation tools for competitive programming. 

競プロでサンプル入出力の取得、サンプルのチェック、提出等を自動化するツール

パスの扱いは Linux 環境を想定 -->

## これはなに

競技プログラミングでサンプル入出力のダウンロード、サンプルのテスト、ソースコードの提出、提出結果の確認等をコマンドラインから行えるツール

## 対応サイト

- AtCoder

## 要求

- Python3.8 以降が動作すること
  - Beautifulsoup および requests モジュールのインストールが必要
    - `pip install beautifulsoup4`
    - `pip install requests`
- 解答には C++ を使用することを想定
- g++ が動作すること
- Makefile を利用できること
- WSL(Ubuntu 18.04)でのみ動作確認済み

## 使い方

1. このリポジトリをクローンして `src/` に移動
2. ログイン
   - `python login.py`
   - ユーザ名とパスワードを尋ねられるので入力する
3. サンプル入出力のダウンロード
   - `python contest_scraper.py {contest_name}`
   - `python contest_scraper.py abc200` を実行したときに生成されるディレクトリの構造は下図のよう
4. サンプルのテスト
   - `task[A-F].cc` のあるディレクトリで `make test`
5. ソースコードの提出
   - `task[A-F].cc` のあるディレクトリで `make submit`
6. 提出結果の確認
   - `task[A-F].cc` のあるディレクトリで `make status`

## 注意

- 上記の `pip` はローカルの環境に応じて適切なものを使うこと
  - `pip3`, `python -m pip`, `python3.9 -m pip`, ...
- 上記の `python` はローカルの環境に応じて適切なものを使うこと
  - `python3`, `python3.9`, ...
- `.template/Makefile` の `CC`, `CFLAGS`, `PYTHON` をローカルの環境に応じて適切に変更すること
- `.template/template.cc` に解答用のテンプレートとして利用する C++ ファイルを用意しておくこと
  - 解答用のテンプレートはコンパイル可能なファイルである必要がある(例えば空のファイルであってはならない)
- ABC 級と ARC 級が同時開催されたときのコンテストでは URL が不規則でダウンロードに失敗することがある
- 古い問題(ABC41 以前)では html ソースの差異によりサンプル入出力がダウンロードできない

## オプション

## TODO

- [ ] バイナリ提出機能の実装
- [ ] Codeforces への対応
- [ ] Cookie へのアクセス権限の変更処理の実装
- [ ] Cookie の削除機能の実装
- [ ] 多言語のサポート