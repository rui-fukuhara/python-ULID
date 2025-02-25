from ulid import new
import pyperclip

# ユーザーから生成したいULIDの数を入力として受け取る
try:
    count = int(input("生成したいULIDの数を入力してください: "))

    # 生成したULIDを保存するリスト
    ulids = []
    
    # 指定された数だけULIDを生成
    for _ in range(count):
        ulid = new()
        ulids.append(str(ulid))
        print(ulid)

    # 生成したULIDをクリップボードにコピー
    pyperclip.copy("\n".join(ulids))
    print("生成したULIDをクリップボードにコピーしました。")
except ValueError:
    print("正しい数値を入力してください。")