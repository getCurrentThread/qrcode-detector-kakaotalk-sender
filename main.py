import qrcode as qr
import kakaotalk as kakao
import time

def init():
    kakao.initialize()

def sendMessage(msg):
    try:
        kakao.run_kakao()
        kakao.enter_chatroom(0)
        kakao.send_msg(msg)
        return True
    except Exception as e:
        print(f'Error: {e}')
        return False

def getQROnScreen():
    image = qr.screenshot()
    return qr.detect_barcode(image)

if __name__ == "__main__":
    init()
    s = set()
    while(True):
        try:
            print("capture...")
            urls = getQROnScreen();
            messages = []
            for url in urls:
                if url not in s:
                    s.add(url)
                    print("[INFO] 새로운 QR 코드 : {}".format(url))
                    messages.append("[INFO] 새로운 QR 코드 : {}".format(url))
            if messages: # 보낼께 있다면 보냄
                sendMessage('\n'.join(messages))
            time.sleep(3)
        except Exception as e:
            print(e)
            break
    print("프로그램을 종료합니다.");
