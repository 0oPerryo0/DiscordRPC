import tkinter
import rpc
from tkinter import *


client_id = '583620449511014410' #Your application's client ID as a string. (This isn't a real client ID)
rpc_obj = rpc.DiscordIpcClient.for_platform(client_id) #Send the client ID to the rpc module
tkinter.window = tkinter.Tk()
tkinter.window.title("Discord RPC")
lbl_1 = tkinter.Label(tkinter.window,text="Discord RPC not yet started")
lbl_1.grid(column=0, row=0)

def misaka():
    lbl_1.configure(text="啟動了「御板20001號」")
    oao = {
            "state": "最後之作喔",
            "details": "我可是控制御板妹妹的控制台",
            "assets": {
                "large_text": "目前和一方通行同居",
                "large_image": "lastorder_accel"
            }
        }
    rpc_obj.set_activity(oao)

misaka_btn = tkinter.Button(tkinter.window, text="Start",command=misaka)
misaka_btn.grid(column=0, row=2,)





