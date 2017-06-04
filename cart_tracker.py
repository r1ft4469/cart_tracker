from tkinter import *

def prob(left, total):
	left=''.join(left)
	left = int(left)
	total=''.join(total)
	total = int(total)
	cardprob = round((left / total) * 100, 2)
	cardprobstr = str(cardprob),'%'
	return cardprobstr

def cardneg(var):
	for key in range(len(AmmountArray)):
		if var == keytotal:
			valuestr = ''.join(AmmountArray[keytotal])
			valuestr = int(valuestr)
			valuestr -= 1
			valuestr = str(valuestr)
			AmmountArray[keytotal] = valuestr
			refreshdeck()
			return
		else:
			if key == var:
				valuestr=''.join(AmmountArray[var])
				valuestr = int(valuestr)
				valuestr -= 1
				valuestr = str(valuestr)
				AmmountArray[var] = valuestr
				valuestr = ''.join(AmmountArray[keytotal])
				valuestr = int(valuestr)
				valuestr -= 1
				valuestr = str(valuestr)
				AmmountArray[keytotal] = valuestr
				refreshdeck()
				return

def cardpos(var):
	for key in range(len(AmmountArray)):
		if var == keytotal:
			valuestr = ''.join(AmmountArray[keytotal])
			valuestr = int(valuestr)
			valuestr += 1
			valuestr = str(valuestr)
			AmmountArray[keytotal] = valuestr
			refreshdeck()
			return
		else:
			if key == var:
				valuestr=''.join(AmmountArray[var])
				valuestr = int(valuestr)
				valuestr += 1
				valuestr = str(valuestr)
				AmmountArray[var] = valuestr
				valuestr = ''.join(AmmountArray[keytotal])
				valuestr = int(valuestr)
				valuestr += 1
				valuestr = str(valuestr)
				AmmountArray[keytotal] = valuestr
				refreshdeck()
				return

def createdecklist():
	global CardArray
	global AmmountArray
	global keytotal
	deckvars = importentry.get("1.0",END)
	key = 1
	decksize = 0
	CardArray = {}
	AmmountArray = {}
	for line in deckvars.splitlines():
		if not line:
			continue
		ammount, card = line.split(" ", 1)
		CardArray.setdefault(key, [])
		CardArray[key].append(card)
		AmmountArray.setdefault(key, [])
		AmmountArray[key].append(ammount)
		decksize += int(ammount)
		key += 1
	CardArray.setdefault(key, [])
	CardArray[key].append('Cards Left in Deck')
	AmmountArray.setdefault(key, [])
	AmmountArray[key].append(str(decksize))
	keytotal = key
	refreshdeck()

def refreshdeck():
	for key in CardArray:
		n = Button(decklistwin, text='-')
		n.configure(command=lambda key=key: cardneg(key))
		n.grid(row=key, column=1)
		p = Button(decklistwin, text='+')
		p.configure(command=lambda key=key: cardpos(key))
		p.grid(row=key, column=3)
		a = Label(decklistwin, text=AmmountArray[key])
		a.grid(row=key, column=2)
		n = Label(decklistwin, text=CardArray[key])
		n.grid(row=key, column=4)
		c = Label(decklistwin, text=prob(AmmountArray[key], AmmountArray[keytotal]))
		c.grid(row=key, column=5)

importwin = Toplevel()
importwin.title("Cart Tracker")

importentry = Text(importwin)
importbutton = Button(importwin, text="Import")
importbutton.configure(command=createdecklist)

importbutton.pack()
importentry.pack()

decklistwin.mainloop()

