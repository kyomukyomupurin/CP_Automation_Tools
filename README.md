# CP_Automation_Tools
Automation tools for competitive programming. 

競プロでサンプル入出力の取得、サンプルのチェック、提出等を自動化するツール

パスの扱いは Linux 環境を想定

## 追加していく機能

- サンプル入出力の取得・保存
- サンプルが合うかチェック
- コマンドラインから提出

## 対応するサイト(予定)

- AtCoder
- Codeforces
- AOJ
- yosupo judge
- LeetCode

## 実装メモ

### AtCoder

#### コンテスト情報

- URL の形式 : https://atcoder.jp/contests/{contest}

- 問題数を取得するのが地味にむずい
  - 6 問で決め打ちでもあまり困らないかも？

#### サンプル入出力の取得

- URL の形式 : https://atcoder.jp/contests/{contest}/tasks/{contest}_{id}

- TO DO : 文字列 {contest} に - が含まれてるときは {contest}_{id} の部分では - を _ に置換する必要がある
  - 例 : https://atcoder.jp/contests/m-solutions2020/tasks/m_solutions2020_a

- ABC 級と ARC 級の企業コンが同時開催されてると URL と id の規則性がちょっと複雑

- id は 6 問なら a-f

- 太古の問題は a-f の部分が 1-4 だったりする
  - つらい　どうしてこんなことに
  - 対策 : 太古の問題は、解かない！

- h3 タグで "Sample Input", "Sample Output" の直後の pre タグで囲まれた部分に入力・出力があるのでそれを抜く
  - 太古のコンテストだと英語版が用意されていなくて "入力例"、"出力例" を見つけて抜く必要がある
  - とはいえ、ソースコードに日本語を書くのは気が進まない
  - 対策 : 太古の問題は、解かない！

### サンプルのチェック

- 余分な空白、改行は許容してチェックする必要がある
  - まず ```"\n"``` を ```" "``` に置換
  - re モジュール(正規表現ライブラリ)で連続する ```" "``` を 1 つの ```" "``` に圧縮
  - 先頭・末尾の ```" "``` を除去して比較

- 複数の出力が正解になり得るような問題
  - 対応できないので、自分で出力を眺めて確認する

- 出力が浮動小数点数になる問題
  - TO DO : スクレイピングの際に許容誤差の情報も抜く

- ターミナル起動後初回のコンパイルが遅いので、サンプルダウンロード中に非同期でコンパイルを実行しておく
- 実行時間制限はとりあえず 2 秒で決め打ち
  - TO DO : html ソースから情報を抜く

### ログインと提出

- ```requests.Session()``` でできる
- csrf token の有効期限がよくわかってない
  - ログイン時と提出時の csrf token は一緒でいいのか？
  - ググって出てきた実装ではログイン時と提出時には別々に取得しているものが多かったのでとりあえずその方針でやる