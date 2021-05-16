# CP_Automation_Tools

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
   - `python contest_scraper.py abc200` を実行したときに生成されるディレクトリの構造は下図のよう(`C` 以降は省略)

```
abc200/
├── A
│   ├── Makefile
│   ├── sample
│   │   ├── input1.txt
│   │   ├── input2.txt
│   │   ├── output1.txt
│   │   └── output2.txt
│   ├── taskA
│   └── taskA.cc
├── B
│   ├── Makefile
│   ├── sample
│   │   ├── input1.txt
│   │   ├── input2.txt
│   │   ├── input3.txt
│   │   ├── output1.txt
│   │   ├── output2.txt
│   │   └── output3.txt
│   └── taskB.cc
```

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
- `.template/Makefile` の `CC`, `CFLAGS`, `PYTHON` をローカルの環境に応じて適切なものに変更すること
- `.template/template.cc` に解答用のテンプレートとして利用する C++ ファイルを配置しておくこと
  - 解答用のテンプレートはコンパイル可能なファイルである必要がある(例えば空のファイルであってはならない)
  - これはサンプル入出力のダウンロード中に `{contest}/A/taskA.cc` のコンパイルを並列で行い、g++ が RAM に載るようにして初回の `make test` の実行を高速化するため
- ABC 級と ARC 級が同時開催されたときのコンテストでは URL が不規則でダウンロードに失敗することがある
- 古い問題(ABC41 以前)では html ソースの差異によりサンプル入出力がダウンロードできない

## オプション

- 必須の `.template/template.cc` 以外に以下の 4 種類の解答用のテンプレートを配置できる
  1. `.template/template_998244353.cc`
     - mod 998244353 の値を出力させるような問題の解答用のテンプレート
  2. `.template/template_1000000007.cc`
     - mod 1000000007 の値を出力させるような問題の解答用のテンプレート
  3. `.template/template_YESNO.cc`
     - YES/NO を出力させるような問題の解答用のテンプレート
  4. `.template/template_YesNo.cc`
     - Yes/No を出力させるような問題の解答用のテンプレート
  - 問題文に特定のキーワードを発見した際にオプションの解答用のテンプレートが自動的に選択される
  - オプションの解答用のテンプレートが存在しなかった場合はデフォルトの `.template/template.cc` が選択される
- コンテストの全問題ではなく単一の問題のサンプル入出力をダウンロードしたいときはオプションで `-p A` のように指定する
  - 例: `python contest_scraper abc200 -p A`
  - `abc200/A` のみが作成される
  - このときは並列での `{contest}/A/taskA.cc` のコンパイルは行われない
  - 引数は大文字でも小文字でも構わない(`-p A` と `-p a` は同じ結果になる)
- 旧 ABC 等、問題数が 6 問でないコンテストのサンプル入出力をダウンロードする際はオプションで `-n 4` のように指定する
  - 例: `python contest_scraper abc100 -n 4`

## TODO

- [x] バイナリ提出機能の実装
- [ ] Codeforces への対応
- [x] Cookie へのアクセス権限の変更処理の実装
- [ ] Cookie の削除機能の実装
- [ ] 多言語のサポート
- [x] `taskA` の削除の実装
- [x] CE があったときに `make status` が失敗するバグの修正