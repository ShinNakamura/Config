# Config

https://docs.python.org/ja/3/library/configparser.html

Python の configparser を使って ini ファイルから設定を読み込む。

階層トップの`Config.ini`を標準で読む仕様で全体の制作を進める。

## in Python

Config モジュールとして使用

## コマンドラインツール

例えば `./Config.ini` が下記のような内容で置かれていた場合

```ini
[Paths]
datad = ./data
```

コマンドラインで次のように実行すると値を返す設計。

```shell
$ python3 /path/to/Config.py "Paths" "datad"
./data # <- 改行なしで印字
```
