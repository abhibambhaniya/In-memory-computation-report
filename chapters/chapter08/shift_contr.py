NO_OF_INSTRUCTIONS = 9
instruction_file = 	open("instruction_S.txt", "r") 
out =	 		open("out.txt","w+")
enW =	 		open("enW.txt","w+")
en1 =			open("en1.txt","w+")
en =			open("en.txt","w+")
readP =			open("readP.txt","w+")
enb =			open("enb.txt","w+")
writeP=			open("writeP.txt","w+")
RL =			open("RL.txt","w+")
readP2 =		open("readP2.txt","w+")
S =			open("S.txt","w+")
Sb =			open("Sb.txt","w+")

def write_defaults(f):
	for i in range(f):							#Row address
		out.write("1")
		enW.write("0")
		en1.write("1")
		en.write("0")
		readP.write("0")
		enb.write("1")
		RL.write("1")
		writeP.write("0")
		readP2.write("0")
			
	return

def signal_gen(s,bit,f):
	
	for i in range(0,f):
		s = s + str(bit)	
	
	return s
	

#write defaults
#write_defaults(150)

#write_controls

#out
out_str = ""
out_str = signal_gen(out_str,1,43)
out_str = signal_gen(out_str,0,2)
out_str = signal_gen(out_str,1,43)
out.write(out_str)
#write_controls(out,out_str)

#enW
enW_str = ""
enW_str = signal_gen(enW_str,0,5)
enW_str = signal_gen(enW_str,1,9)
enW_str = signal_gen(enW_str,0,61)
enW.write(enW_str)
#write_controls(enW,enW_str)

#en1
en1_str = ""
en1_str = signal_gen(en1_str,0,1)
en1_str = signal_gen(en1_str,1,21)
en1.write(en1_str)
#write_controls(en1,en1_str)

#en
en_str = ""
en_str = signal_gen(en_str,0,7)
en_str = signal_gen(en_str,1,74)
en_str = signal_gen(en_str,0,70)
en.write(en_str)
#write_controls(en,en_str)

#enb
enb_str = ""
enb_str = signal_gen(enb_str,1,7)
enb_str = signal_gen(enb_str,0,74)
enb_str = signal_gen(enb_str,1,70)
enb.write(enb_str)
#write_controls(enb,enb_str)

#readP
readP_str = ""
readP_str = signal_gen(readP_str,0,13)
readP_str = signal_gen(readP_str,1,11)
readP_str = signal_gen(readP_str,0,70)
readP_str = signal_gen(readP_str,1,7)
readP_str = signal_gen(readP_str,0,50)
readP.write(readP_str)
#write_controls(readP,readP_str)

#RL
RL_str = ""
RL_str = signal_gen(RL_str,1,1)
RL_str = signal_gen(RL_str,0,21)
RL.write(RL_str)
#write_controls(RL,RL_str)

#writeP
writeP_str = ""
writeP_str = signal_gen(writeP_str,0,30)
writeP_str = signal_gen(writeP_str,1,11)
writeP_str = signal_gen(writeP_str,0,109)
writeP.write(writeP_str)
#write_controls(writeP,writeP_str)

#readP2
readP2_str = ""
readP2_str = signal_gen(readP2_str,0,13)
readP2_str = signal_gen(readP2_str,1,11)
readP2_str = signal_gen(readP2_str,0,126)
readP2.write(readP2_str)
#write_controls(readP2,readP2_str)

#S
S_str = ""
S_str = signal_gen(S_str,1,75)
S.write(S_str)
#write_controls(S,S_str)

#Sb
Sb_str = ""
Sb_str = signal_gen(Sb_str,1,75)
Sb.write(Sb_str)
#write_controls(Sb,Sb_str)

instruction_file.close()
out.close()
enW.close()    
en1.close()    
en.close()	  
enb.close()	  
readP.close()	  
RL.close() 
writeP.close() 
readP2.close()	  
S.close()
Sb.close()
