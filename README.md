# CP_Automation_Tools
Automation tools for competitive programming. 

競プロでサンプル入出力の取得、サンプルのチェック、提出等を自動化するツール

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

- URL の形式 : https://atcoder.jp/contests/{contest_name}

- 問題数を取得するのが地味にむずい
  - 6 問で決め打ちでもあまり困らないかも？

#### サンプル入出力の取得

- URL の形式 : https://atcoder.jp/contests/{contest_name}/tasks/{contest_name}_{id}

- id は 6 問なら a-f

- 太古の問題は a-f の部分が 1-4 だったりする
  - つらい　どうしてこんなことに
  - 対策 : 太古の問題は、解かない！

- h3 タグで "Sample Input", "Sample Output" の直後の pre タグで囲まれた部分に入力・出力があるのでそれを抜く
  - 太古のコンテストだと英語版が用意されていなくて "入力例"、"出力例" を見つけて抜く必要がある
  - とはいえ、ソースコードに日本語を書くのは気が進まない
  - 対策 : 太古の問題は、解かない！

- コンテスト中にサンプル入出力を取得するには参加登録とログインが必要
  - Cookie とかをゴニョゴニョすればできるらしい
  - あまりよくわかっていないが、同じようなことをしている記事をいくつか発見したのでそれを~~パクる~~参考にする