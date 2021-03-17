# Discord 日体大コールBot

## 利用方法
[こちら](https://discord.com/api/oauth2/authorize?client_id=820995277511065650&permissions=0&scope=bot)からBotをお好きなサーバーに招待してください。

Herokuの無料枠を利用していますので、動作が遅い場合があります。

### Docker セルフホスト
Dockerを使うことで、セルフホストすることも可能です。
Dockerの導入方法、Dockerの基本的な使い方についてはここでは紹介しません。

#### 1. セルフホスト用のBotを作成
セルフホストで利用するには、ご自身のDiscordアカウントでBotを作成する必要があります。

[ここ](https://discord.com/developers/applications)にアクセスし、New Applicationをクリックします。

![](https://user-images.githubusercontent.com/38001048/111465178-1a711f80-8765-11eb-8e04-9aa18d35eef5.png)

BotタブからAdd Botをクリックし、Botを作成します。

![](https://user-images.githubusercontent.com/38001048/111465800-d29ec800-8765-11eb-9008-f457a2d19573.png)

Botが作成できたら、TOKENの下にあるCOPYボタンを押してアクセストークンをコピーし、どこかに控えておきます。

![](https://user-images.githubusercontent.com/38001048/111466019-1691cd00-8766-11eb-90bb-00e870a88efa.png)

Oauth2タブへ移動し、SCOPESの欄からbotを選択すると、Botの招待リンクが発行されます。COPYボタンでコピーできます。

#### 2. .envファイルを作成
リポジトリをclone or downloadしたら、以下のようにコマンドを実行して.envファイルを作成します。

Linux/MacOSの場合
```
cd discord_bot/
touch .env
```

Windows(PowerShell)の場合
```
cd discord_bot/
New-Item -Type File .env
```

作成できたら、.envを開いて、先程コピーしたBotのアクセストークンを記入します。

```
DISCORD_BOT_TOKEN=<コピーしたトークン>
```


#### 3. docker-composeで起動
下記のコマンドを実行してコンテナを実行します。
コンテナの実行時にBotのスクリプトも実行されるようになっています。

```
docker-compose up -d --build
```


## お問い合わせ
バグ報告などは[Twitter](https://twitter.com/penguin_4glte)までお願いします。

IssueやPull Requestも確認していますので、なにかあればそちらもお願いします。