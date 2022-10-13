# roboterパッケージに主要な処理をまとめる
# main.py でインポートして呼び出す
import interlude.roboter.controller.conversation

def main():
    interlude.roboter.controller.conversation.talk_about_restaurant()

if __name__ == '__main__':
    main()