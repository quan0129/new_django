import websocket
try:
    import thread
except ImportError:
    import _thread as thread
import time
import json
import os

def on_message(ws,message):
    jso = json.loads(message)
    if jso["message"] == "batpaint":
        os.system("mspaint")
    
    print(message)


def on_error(ws,error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    print("### open ###")
    def run(*args):
        for i in range(3):
            time.sleep(1)
            ws.send('{"message":"quan nguyen"}')
        time.sleep(1)
        print("thread terminating...")
    thread.start_new_thread(run,())

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws:http://127.0.0.1:8000/chat/quan/",
                                on_message=on_message, on_error=on_error, on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()