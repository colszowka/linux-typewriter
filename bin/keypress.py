#!/usr/bin/env python 
## A tiny, nifty script for playing musical notes on each keypress. 
## 
##	Copyright Sayan "Riju" Chakrabarti (sayanriju) 2009 
##	me[at]sayanriju[dot]co[dot]cc ## 
##		Released under WTFPL Version 2 
## (DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE) 
##	Copy of license text can be found online at ##		http://sam.zoy.org/wtfpl/COPYING 
## http://rants.sayanriju.co.cc/script-to-make-tick-tick-sound-on-keypress
 
from Xlib.display import Display 
import os 
import time

notes=[440,494,523,587,659,698,784]	 
 
ZERO,SHIFT,ALT,CTL=[],[],[],[] 
for i in range(0,32): 
	ZERO.append(0) 
	if i==6: 
		SHIFT.append(4) 
	else: 
		SHIFT.append(0) 
	if i==4: 
		CTL.append(32) 
	else: 
		CTL.append(0) 
	if i==8: 
		ALT.append(1) 
	else: 
		ALT.append(0) 
		 
ignorelist=[ZERO,ALT,SHIFT,CTL] 

def main(): 
	disp = Display()	# connect to display	 

	while 1:	#event loop 
		keymap = disp.query_keymap() 
		if keymap not in ignorelist: 
			os.popen("curl http://localhost:4567/key")
			time.sleep(0.1)

 
if __name__ == '__main__': 
	main() 
