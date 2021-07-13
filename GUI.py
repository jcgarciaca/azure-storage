import tkinter
from tkinter import filedialog
import time
import os

class App:
    def __init__(self, window, window_title, video_source=0):
        self.folder = None
        self.logfile = None
        self.valid_folder = False
        self.valid_logfile = False
        self.background = '#d9d9d9'
        self.window = window
        self.window.title(window_title)
        self.window.geometry('640x450')
        self.window.configure(background=self.background)
        self.window.columnconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=1)

        # Command buttons
        self.btn_imgs_folder = tkinter.Button(window, text="Select Images Folder", width=20, command=self.search_folder)
        self.btn_imgs_folder.grid(column=0, row=0)
        self.btn_logfile = tkinter.Button(window, text="Select Log File", width=20, command=self.search_file)
        self.btn_logfile.grid(column=1, row=0)

        self.imgs_lb = tkinter.Listbox(window, height=20, width=40)
        self.scrollbar = tkinter.Scrollbar(window)        
        self.imgs_lb.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.imgs_lb.yview)        
        self.imgs_lb.grid(column=0, row=2)
        self.scrollbar.grid(column=0, row=2, sticky=tkinter.NS+tkinter.E)
        
        self.lbl_logfile = tkinter.Text(window, height=5, width=35, font=("Helvetica", 10), bg=self.background)
        self.lbl_logfile.grid(column=1, row=2)

        self.btn_upload = tkinter.Button(window, text="Upload", width=20, command=self.upload_files)
        self.btn_upload.grid(column=1, row=3)

        self.window.mainloop()
        
    def search_folder(self):
        self.valid_folder = False
        self.imgs_lb.delete(0, 'end')
        self.folder = filedialog.askdirectory(initialdir = '/', title = "Select images folder")
        if isinstance(self.folder, str):
            if os.path.isdir(self.folder):
                self.imgs_lb.config(yscrollcommand=self.scrollbar.set)
                for item in os.listdir(self.folder):
                    self.imgs_lb.insert('end', item)
                self.valid_folder = True

    def search_file(self):
        self.valid_logfile = False
        self.lbl_logfile.delete('1.0', 'end')
        self.logfile = filedialog.askopenfilename(initialdir = '/', title = "Select logfile")
        if isinstance(self.logfile, str):
            if os.path.isfile(self.logfile):
                self.lbl_logfile.insert('end', 'Selected file:\n' + self.logfile)
                f = open(self.logfile, 'r')
                data = []
                for line in f:
                    data.append(line)
                print('data:', len(data), data)
                self.valid_logfile = True

    def upload_files(self):
        if self.valid_folder and self.valid_logfile:
            print('Upload')
        

if __name__ == "__main__":
    # Create a window and pass it to the Application object
    App(tkinter.Tk(), "GM Azure Photo Uploader")