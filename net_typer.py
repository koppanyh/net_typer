import pyautogui as pag
import socket

pag.FAILSAFE = False

def readLine(socket):
	buf = b""
	while True:
		b = socket.recv(1)
		if b == b'\n':
			break
		buf += b
	return buf.decode("utf-8") #.rstrip("\r\n")

def writeLine(socket, text):
	socket.sendall((text.rstrip("\r\n") + "\r\n").encode("utf-8"))

def processHotKey(line):
	line = line[1:] #strip the [
	line = line.split(']', maxsplit=1)
	cmds = line.pop(0).split()
	line = line[0] if line else ""
	if cmds[0] == "exit":
		exit()
	pag.hotkey(*cmds)
	process(line)

def process(line):
	if not line:
		return
	bracket = line.find("[")
	if bracket >= 0: #if there's a bracket
		isEscaped = bracket >= 1 and line[bracket - 1] == '\\'
		if isEscaped:
			pre = line[:bracket - 1]
			if pre:
				pag.typewrite(pre)
			pag.typewrite('[')
			process(line[bracket + 1:])
		else:
			pag.typewrite(line[:bracket])
			processHotKey(line[bracket:])
	else: #otherwise print normally
		pag.typewrite(line)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind(("0.0.0.0", 20052)) #setup the socket server
	s.listen()
	
	conn, addr = s.accept()
	print(f"Connected on {addr}")
	writeLine(conn, "N3T TYP3R (c)22 v0.9")
	
	while True:
		#writeLine(conn, readLine(conn))
		process(readLine(conn))
