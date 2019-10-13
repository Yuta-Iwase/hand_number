# hand_number

## ダウンロード

zipで落とすかgit cloneコマンドで複製する

- zipで落とす  
    https://github.com/Yuta-Iwase/hand_number/archive/master.zip
- git clone
    ```
    git clone https://github.com/Yuta-Iwase/hand_number.git
    ```

## 導入方法
1. anacondaをインストール
2. tensorflowをインストール
    ```
    pip install --upgrade pip
    pip install tf-nightly
    ```
3. serve.pyを実行
    ```
    python serve.py
    ```
4. http://127.0.0.1:8080 を開く

### エラーの場合
- flaskパッケージがないならインストール
    ```
    pip install flask
    ```
- tensorflowのバージョンによっては関数の仕様が変わって実行できなくなる可能性があります

## 使い方
1. 白い四角の中でドラッグして数字を手書きで書く
2. POSTを押すと推定結果がでます
    ※データの関係で0,1,2の推定しかできません

