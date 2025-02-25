from ulid import new

# ユーザーから生成したいULIDの数を入力として受け取る
try:
    count = int(input("生成したいULIDの数を入力してください: "))
    
    # 指定された数だけULIDを生成
    for _ in range(count):
        ulid = new()
        print(ulid)
except ValueError:
    print("正しい数値を入力してください。")