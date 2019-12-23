# ctf_discord_bot
CTFチームサーバー用のDiscord Botを作ろうとしている。

## Commands
- `!base64 mode string`: base64でエンコード(`-e`)したりデコード(`-d`)したりするよ、エンコードの方はprintableな文字列しか対応してないよ。
- `!rot13 string --num`: ROT13するよ、`--num`に数字を指定するとその分だけずらすよ
- `!ascii hex_num`: 16進表記として有効な数字をASCIIコードを用いて文字列に変換するよ
- `!hex string`: 文字列をASCIIコードを用いて16進数の数字に変換するよ
