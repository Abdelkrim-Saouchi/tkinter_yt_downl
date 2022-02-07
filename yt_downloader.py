from tkinter import *
from tkinter import ttk
from tkinter import messagebox, filedialog
import re
import threading
from pytube import YouTube
from pytube.exceptions import PytubeError

LARGE_FONT_STYLE= ("Arial", 20)
MSG_FONT_STYLE= ("Arial", 10)
BUTTON_FONT_STYLE= ("Arial", 13)

Quality_list= ['144p', '240p', '360p', '480p', '720p', 'only audio']
Error_msg= "For some raison the download is failed! make sure of: \n -your internet connexion.\n -the video is not deleted.\n -the video is not age restricted or private.\n -the video is not livestream.\n -the video is not download restricted by the owner."

class Yt_Structure:
	def __init__(self):
		self.window = Tk()
		self.window.title("Krimou's Youtube Downloader")
		self.window.geometry("400x500")
		self.window.resizable(0,0)
		self.title_label = self.create_title_lable()
		self.put_link_msg_label = self.create_put_link_msg_label()
		self.link_box = Entry(self.window, width=50, borderwidth=5)
		self.link_box.pack(pady=10)
		self.quality_msg = self.create_quality_msg()
		self.quality_menu = ttk.Combobox(self.window, values= Quality_list)
		self.quality_menu.pack(pady=10)
		self.choose_folder_msg = self.create_choose_folder_msg()
		self.browse_button = self.create_browse_button()
		self.label_current_downlod_folder_msg= Label(self.window, text= "your current Download directory is: ", fg= "red", font= MSG_FONT_STYLE)
		self.label_current_downlod_folder_msg.pack(pady=10)
		self.download_button = self.create_download_button()
		self.download_path = StringVar()
		self.percent = 0
		self.download_percent_label = Label(self.window, text="", font=MSG_FONT_STYLE, fg="red")
		self.download_percent_label.pack(pady=10)
		self.create_mouse_menu()
		


	def create_title_lable(self):
		label= Label(self.window, text="Krimou's Youtube Downloader", font= LARGE_FONT_STYLE)
		label.pack(pady=10)

	def create_put_link_msg_label(self):
		label= Label(self.window, text= "plz! Enter the video's link below", fg= "red", font= MSG_FONT_STYLE)
		label.pack(pady=10)

	def create_quality_msg(self):
		label= Label(self.window, text= "plz! Choose the quality", fg= "red", font= MSG_FONT_STYLE)
		label.pack(pady=10)


	def create_choose_folder_msg(self):
		label= Label(self.window, text= "plz! Choose your Download folder", fg= "red", font= MSG_FONT_STYLE)
		label.pack(pady=10)	

	def browse_fun(self):
		self.download_directory= filedialog.askdirectory()
		self.download_path.set(self.download_directory)
		self.label_current_downlod_folder_msg.config(text= f"your current Download directory is: \n {self.download_directory}")


	def create_browse_button(self):
		button= Button(self.window, text="Browse", font=BUTTON_FONT_STYLE, borderwidth=3, pady=2, padx=5, command= self.browse_fun)
		button.pack(pady=5)

	def progress_check(self, stream, chunk, bytes_remaining):
		self.file_size= stream.filesize
		self.downloaded_bytes = self.file_size - bytes_remaining
		self.percent= (self.downloaded_bytes/self.file_size) *100
		self.download_percent_label.config(text="Downloading Now... \n {:00.0f}% downloaded".format(self.percent))

	def download_fun(self):
		button1.config(state="disabled")
		self.download_folder= self.download_path.get()
		if self.quality_menu.get() in Quality_list:
			link= self.link_box.get()
			if len(link) >1:
				is_yt_link = re.search(r"(https)?(://)?(www)?\.?youtube.com/.*", link)
				if is_yt_link:
					yt= YouTube(link)
					yt.register_on_progress_callback(self.progress_check)
					yt1= yt.streams
					if (yt.streams.filter(res=self.quality_menu.get()).first()) in yt1:
						ys= yt.streams.filter(res=self.quality_menu.get()).first()
						if len(self.download_folder) > 1:
							try:
								ys.download(self.download_folder)
								messagebox.showinfo("Success!", "The video is successfully downlaoded!")
							except PytubeError:
								messagebox.showinfo("Error!", Error_msg)
						else:
							messagebox.showinfo("Error", "please choose a valid downlaod folder via Browse button!") 
					elif self.quality_menu.get() == 'only audio':
						ys= yt.streams.filter(only_audio=True).first()
						if len(self.download_folder) >1 :
							try:
								ys.download(self.download_folder)
								messagebox.showinfo("Success!", "The Audio is successfully downlaoded!")
							except PytubeError:
								messagebox.showinfo("Error!", Error_msg)
						else:
							messagebox.showinfo("Error", "please choose a valid downlaod folder via Browse button!")
					else:
						messagebox.showinfo("Error", "This quality does not exist try another quality!")
				else:
					messagebox.showinfo("Error", "This app workes only with youtube's links")
			else:
				messagebox.showinfo("Error", "please entre a link!")
		else:
			messagebox.showinfo("Error", "please choose a video quality")
		button1.config(state="normal")

	def threading_process(self):
		thread1= threading.Thread(target= self.download_fun)
		thread1.start()

	def create_download_button(self):
		global button1
		button1= Button(self.window, text="Download", font=BUTTON_FONT_STYLE, borderwidth=3, pady=2, padx=5, command= self.threading_process)
		button1.pack(pady=10)

	def show_menu(self, event):
		self.menu.tk_popup(event.x_root, event.y_root)

	def copy(self):
		self.link_box.event_generate("<<Copy>>")
	def cut(self):
		self.link_box.event_generate("<<Cut>>")
	def paste(self):
		self.link_box.event_generate("<<Paste>>")

	def create_mouse_menu(self):
		self.menu= Menu(self.link_box, tearoff=0)
		self.menu.add_command(label="Copy", command=self.copy)
		self.menu.add_command(label="Cut", command= self.cut)
		self.menu.add_command(label="Paste", command= self.paste)
		self.link_box.bind('<3>', self.show_menu)

	def run(self):
		self.window.mainloop()

if __name__ == '__main__':
	yt_prg= Yt_Structure()
	yt_prg.run()



