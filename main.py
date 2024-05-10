import tkinter 
from tkinter import StringVar, Button, Label , Entry , messagebox
from pytube import Stream, YouTube
import requests 
from PIL import ImageTk, Image


top = tkinter.Tk()
top.geometry("800x450")
top.resizable(width=False, height=False)


link= StringVar()
itags = {}

def Err():
    messagebox.showerror("ERR", "Check your internet!")
    main()

def start():
    message_info_yes_or_no(link)

def len_itags_and_BTs(itags):
    lens = len(itags)
    return lens

def button_click(button_num, yt, panel, top1):
    if button_num == 720:
        stream = yt.streams.get_by_itag(137)
        stream.download()
        messagebox.showinfo("Completed", "The download was successfully done with 720p quality!")
        panel.destroy()
        top1.destroy()
        main()
    if button_num == 480:
        stream = yt.streams.get_by_itag(135)
        stream.download()
        messagebox.showinfo("Completed", "The download was successfully done with 480p quality!")
        panel.destroy()
        top1.destroy()
        main()
    if button_num == 360:
        stream = yt.streams.get_by_itag(134)
        stream.download()
        messagebox.showinfo("Completed", "The download was successfully done with 360p quality!")
        panel.destroy()
        top1.destroy()
        main()
    if button_num == 240:
        stream = yt.streams.get_by_itag(133)
        stream.download()
        messagebox.showinfo("Completed", "The download was successfully done with 240p quality!")
        panel.destroy()
        top1.destroy()
        main()
    if button_num == 144:
        stream = yt.streams.get_by_itag(160)
        stream.download()
        messagebox.showinfo("Completed", "The download was successfully done with 144p quality!")
        panel.destroy()
        top1.destroy()
        main()

def download(link, panel):
    top1= tkinter.Tk()
    top1.geometry("300x300")
    yt = YouTube(link)

    try:
        title = yt.title
        stream_info = yt.streams.filter(file_extension='mp4')
    except:
        panel.destroy()
        Err()
        top1.destroy()
    streams = stream_info.all()
    stream_info_list = []

    for stream_str in streams:
        stream_info = {}
        stream_info["itag"] = stream_str.itag
        stream_info["mime_type"] = stream_str.mime_type
        stream_info["res"] = stream_str.resolution
        stream_info["type"] = stream_str.type
        stream_info_list.append(stream_info)

    for info in stream_info_list:
        # 160 = 144p | 133 = 240p | 134= 360p | 135 = 480p | 136 = 720p | 137 = 1080p

        itag = info.get("itag")
        if itag == 160:
            itags[144] = itag 
        if itag == 133:
            itags[240]= itag
        if itag == 134:
            itags[360]= itag
        if itag == 135:
            itags[480]= itag
        if itag == 136:
            itags[720]= itag
        if itag == 137:
            itags[1080]= itag

    
    len = len_itags_and_BTs(itags)

    if len != 0 :
        for i in itags:
            button = tkinter.Button(top1, text=f"{i}p / mp4", command=lambda i=i: button_click(i, yt, panel, top1))
            button.pack()
            top1.quit()



    top1.mainloop()

def message_info_yes_or_no(link):
    link = link.get()
    try:
        yt = YouTube(link)
        title = yt.title
        image_url = yt.thumbnail_url

        img_data = requests.get(image_url).content
        with open('image.jpg', 'wb') as handler:
            handler.write(img_data)
    except:
        Err()

    image = Image.open("image.jpg")
    image = image.resize((800, 450))
    img = ImageTk.PhotoImage(image)
    panel = Label(top, image=img)
    panel.place(relwidth=1, relheight=1)


    yes_or_no = messagebox.askyesno("check title", "Is this title correct?:\n " "("+title+")")

    if yes_or_no == True:
        download(link, panel)
        panel.destroy()
    else:
        messagebox.showinfo("Try again", "If the video is wrong, please check the link and try again!")
        panel.destroy()
        main()
        

def main():
    top.config( bg = "#B0C4DE")
    L1 = Label(top, text="Enter your YouTube link:")
    L1.place(x=120, y=200)

    Entry_link = Entry(top, bd =1, textvariable = link)
    Entry_link.place(x=260,y=200, height=25, width=260)

    B1 = Button(text ="download", command = start)
    B1.place(x=250,y=250, height=25, width=100)

main()

top.mainloop()