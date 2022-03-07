import tkinter as tk 
import tkinter.ttk as ttk
from wordfind import get_word

class GUI:
	def __init__(self, root, word):
		self.word = word
		self.root = root
		self.title_lbl = tk.Label(root, text = "Βρες τη σωστή λέξη", font = ("sans serif", 25), bg = "white")
		self.title_lbl.pack(fill = "both")
		
		self.st = ttk.Style(root)
		self.st.configure("W.TButton", background="#345", foreground="black", font=("sans serif", 25))
		self.enter_btn = ttk.Button(root, text = "Enter", style = "W.TButton", command = self.press_enter)
		self.enter_btn.place(x = 0, y = 500)
		self.del_btn = ttk.Button(root, text = "Del", style = "W.TButton", command = self.press_del)
		self.del_btn.place(x = 250, y = 500)

		self.r, self.c = 6,5
		self.lbls = [0 for temp in range(5)]
		self.ans = ['' for temp in range(5)]
		self.cur = 0
		self.create_frames()
		self.bind_keys()
		

	def press_enter(self):
		for i,c in enumerate(self.ans):
			if c.isalpha():
				if c == self.word[i]:
					self.lbls[i].configure(bg = "green")
				elif c in self.word:
					self.lbls[i].configure(bg = "yellow")
				else:
					self.lbls[i].configure(bg = "grey")
		if self.ans == list(self.word):
			self.title_lbl.configure(text = "Nίκησες")
			self.lbls[self.cur].unbind("<Key>")
		elif self.r:
			self.cur = 0
			self.ans = ['' for temp in range(5)]
			self.create_frames()
			self.bind_keys()
		else:
			self.title_lbl.configure(text = f"Έχασες η λέξη ήταν {self.word}...")
			self.lbls[self.cur].unbind("<Key>")

	def press_del(self):
		self.ans = ['' for temp in range(5)]
		self.lbls[self.cur].unbind("<Key>")
		for lbl in self.lbls:
			lbl.configure(text = "")
		self.cur = 0
		self.bind_keys()
	
	def bind_keys(self):
		self.lbls[self.cur].focus_set()
		self.lbls[self.cur].bind("<Key>", self.press_key)

	def create_frames(self):
		frame = tk.Frame(self.root, bg = "white", highlightbackground="blue", highlightthickness=3)
		frame.pack(fill = "both", expand = 0)
		for j in range(self.c):
			lbl = tk.Label(frame, text="", font=("sans serif",35), bg="white")
			lbl.grid(row = 5-self.r+1, column = j+1, ipadx = 30)
			self.lbls[j] = lbl
		self.r -= 1

	def press_key(self, event):
		sel = event.char.upper()
		if not sel.isalpha():
			return
		event.widget.configure(text = sel)
		self.ans[self.cur] = sel
		if self.cur < 4:
			self.cur += 1
			self.bind_keys()



if __name__ == "__main__":
	word = get_word()
	root = tk.Tk()
	root.title("Wordle")
	root.configure(bg = "white")
	root.geometry("489x600")
	root.maxsize(489, 600)

	GUI(root, word)
	root.mainloop()

