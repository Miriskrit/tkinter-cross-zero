from tkinter import *
from PIL import Image, ImageTk
from random import randint
root = Tk()
root.resizable(width=False, height=False)
root.title('GAME')
root["bg"] = 'lightblue'
player = 0
full = 0
def reset():
	for i in range(9):
		global full
		Button_list[i]['text'] = ''
		Button_list[i]['image'] = default
		full = 0

def winLine(b1,b2,b3,image):
	Button_list[b1]['image'] = image
	Button_list[b2]['image'] = image
	Button_list[b3]['image'] = image
	curent_player['text'] = 'WIN /n press : "reset" '

def win():
	global full
	for i in range(8):
		win_list = ( (0,1,2,img_win_X_w,img_win_0_w),
			  (0,3,6,img_win_X_h,img_win_0_h),
			  (0,4,8,img_win_X_r, img_win_0_r),
			  (1,4,7,img_win_X_h, img_win_0_h),
			  (2,5,8,img_win_X_h, img_win_0_h),
			  (2,4,6,img_win_X_l, img_win_0_l),
			  (3,4,5,img_win_X_w, img_win_0_w),
			  (6,7,8,img_win_X_w, img_win_0_w) )
		b = win_list[i]
		if Button_list[b[0]]['text'] == Button_list[b[1]]['text'] == Button_list[b[2]]['text'] == 'X':
			winLine(b[0],b[1],b[2],b[3])
			full = 0
		elif Button_list[b[0]]['text'] == Button_list[b[1]]['text'] == Button_list[b[2]]['text'] == 'O':
			winLine(b[0],b[1],b[2],b[4])
			full = 0
	#event.widget['bg']
def changeBtn(event):
	global player, full
	if player % 2 == 0:
		if event.widget['text'] == '':
			event.widget['text'] = 'X'
			event.widget['image'] = image_X
			curent_player['text'] = 'O'
			player += 1
			full += 1

	if player % 2 == 1:
		def auto():
			r = randint(0,8)
			if Button_list[r]['text'] == '':
				Button_list[r]['text'] = 'O'
				Button_list[r]['image'] = image_O
				curent_player['text'] = 'X'	
			else:
				auto()
			
		player += 1
		full += 1
		if full < 9:
			auto()
		win()

# 121 x 131
default = ImageTk.PhotoImage(Image.open('sources/tk_D.png'))
image_X = ImageTk.PhotoImage(Image.open('sources/tk_X.png'))
image_O = ImageTk.PhotoImage(Image.open('sources/tk_O.png'))
image_button = ImageTk.PhotoImage(Image.open('sources/button_img.png'))
image_button2 = ImageTk.PhotoImage(Image.open('sources/button_img2.png'))

img_win_X_h = ImageTk.PhotoImage(Image.open('sources/tk_X_win_h.png'))
img_win_X_w = ImageTk.PhotoImage(Image.open('sources/tk_X_win_w.png'))
img_win_X_r = ImageTk.PhotoImage(Image.open('sources/tk_X_win_r.png'))
img_win_X_l = ImageTk.PhotoImage(Image.open('sources/tk_X_win_l.png'))
img_win_0_h = ImageTk.PhotoImage(Image.open('sources/tk_O_win_h.png'))
img_win_0_w = ImageTk.PhotoImage(Image.open('sources/tk_O_win_w.png'))
img_win_0_r = ImageTk.PhotoImage(Image.open('sources/tk_O_win_r.png'))
img_win_0_l = ImageTk.PhotoImage(Image.open('sources/tk_O_win_l.png'))

Button_list = []
row_s = 0; column_s = 0
for i in range(9):
	b = Button(root, text='', image=default, bd=7,bg='lightblue')
	b.bind('<Button-1>',changeBtn)
	b.grid(row = row_s, column = column_s)
	if row_s < 2:
		row_s += 1
	else:
		row_s = 0
		column_s +=1
	Button_list.append(b)

text_lable = Label(root, image = image_button2)
curent_player = Label(root, text='',bd=7, bg='lightblue', width=15, height=3)
text_lable.grid(row=4, column=0)
curent_player.grid(row=4, column=1)
res = Button(root, text='reset', image = image_button, command=reset).grid(row=4, column=2)

root.mainloop()


