NO_OF_INSTRUCTIONS = 9
instruction_file = 	open("instruction.txt", "r") 
write_row_0 =	 	open("wr_add0.txt","w+")
write_row_1 =	 	open("wr_add1.txt","w+")
write_pre_0 =		open("wr_pre0.txt","w+")
write_pre_1 =		open("wr_pre1.txt","w+")
write_col_en0 =		open("write_col_en0","w+")
write_col_en1 =		open("write_col_en1","w+")
write_en=		open("write_en","w+")
Din_s =			open("Din_s","w+")
data1 =			open("data1.txt","w+")
data2 =			open("data2.txt","w+")
data3 =			open("data3.txt","w+")
data4 =			open("data4.txt","w+")

read_pre_0 =		open("read_pre0.txt","w+")
read_pre_1 =		open("read_pre1.txt","w+")
r_add0     =		open("r_add0.txt","w+")
r_add1     =		open("r_add1.txt","w+")
read_en	   = 		open("read_en","w+")
op_sel1	   =		open("op_sel1","w+")
op_sel2	   =		open("op_sel2","w+")
block_en1  =		open("block1_en","w+")
block_en2  =		open("block2_en","w+")
nor	   = 		open("nor","w+")

def write_defaults(bit):
	for i in range(bit):							#Row address
			write_row_1.write("0")
			write_row_0.write("0")
			write_pre_0.write("1")
			write_pre_1.write("1")	
			write_col_en0.write("0")
			write_col_en1.write("0")
			Din_s.write("0")					#Din mux select
			write_en.write("0")					#Row enable		
			data1.write("0")
			data2.write("0")
			data3.write("0")
			data4.write("0")	
	return
def read_defaults(bit):
	for i in range(bit):							
			r_add0.write("0")
			r_add1.write("0")
			read_pre_0.write("1")
			read_pre_1.write("1")	
			op_sel1.write("0")
			op_sel2.write("0")
			nor.write("0")						
			read_en.write("0")							
			block_en1.write("0")
			block_en2.write("0")
				
	return
	
for index in range(NO_OF_INSTRUCTIONS):
	inst=instruction_file.next().replace(" ", "")
	print "This is inst %d" %(index)
	print(inst[0:4])
	print(inst[4])  
	print(inst[4:7]) 
	print(inst[7:10])
	print(inst[10:13])
	print(inst[13:17])
	if(inst[0:4]=="0000"):									#Takes 23 cycles
		bits=23		
		print "Write"
		read_defaults(bits)
		Din_s.write("0000 0000 0000 0000 0000 000")					#Din mux select
		write_en.write("0000 0000 0000 0000 1111 110")					#Row enable		
		if(inst[4]=="0"):								#precharge
			write_pre_0.write("0000 0000 0000 1111 1111 111")
			write_pre_1.write("1111 1111 1111 1111 1111 111")	
			write_col_en0.write("0000 0000 0000 1111 1111 111")			#column_block_select
			write_col_en1.write("0000 0000 0000 0000 0000 000")
	
		if(inst[4]=="1"):	
			write_pre_1.write("0000 0000 0000 1111 1111 111")
			write_pre_0.write("1111 1111 1111 1111 1111 111")	
			write_col_en1.write("0000 0000 0000 1111 1111 111")
			write_col_en0.write("0000 0000 0000 0000 0000 000")	
		
		for i in range(bits):								#Row address
			write_row_1.write("%s" % inst[5])
			write_row_0.write("%s" % inst[6])
			data1.write("%s" % inst[13])						#data
			data2.write("%s" % inst[14])
			data3.write("%s" % inst[15])
			data4.write("%s" % inst[16])		
	if(inst[0:4]=="0001"):									#Takes 30 cycles
		bits=17		
		print "Read"
		write_defaults(50)
		read_en.write("0000 0000 0000 0000 1000 0000 0000 00")						#Row enable		
		op_sel1.write("0000 0000 0001 1111 1111 1111 1111 11")
		if(inst[4]=="0"):								#precharge
			read_pre_0.write("0000 0000 0001 1111 1111 1111 1111 11")
			read_pre_1.write("1111 1111 1111 1111 1111 1111 1111 11")	
			block_en1.write(" 0000 0000 0001 1111 1111 1111 1111 11")				#column_block_select
			block_en2.write(" 0000 0000 0000 0000 0000 0000 0000 00")	
	
		if(inst[4]=="1"):	
			read_pre_1.write("0000 0000 0001 1111 1111 1111 1111 11")
			read_pre_0.write("1111 1111 1111 1111 1111 1111 1111 11")	
			block_en2.write(" 0000 0000 0001 1111 1111 1111 1111 11")
			block_en1.write(" 0000 0000 0000 0000 0000 0000 0000 00")	
		
		for i in range(11):								
			nor.write("0")	
			op_sel2.write("0")			
			r_add1.write("0")
			r_add0.write("0")
		
		for i in range(19):								#Row address
			nor.write("0")	
			op_sel2.write("0")			
			r_add1.write("%s" % inst[5])
			r_add0.write("%s" % inst[6])
			
		read_defaults(20)		

		


instruction_file.close()
write_row_0.close()
write_row_1.close()
write_pre_0.close()
write_pre_1.close()
write_col_en0.close()
write_col_en1.close()
write_en.close()
Din_s.close()
data1.close()
data2.close()
data3.close()
data4.close()


read_pre_0.close()
read_pre_1.close()
r_add0.close()    
r_add1.close()    
read_en.close()	  
op_sel1.close()	  
op_sel2.close()	  
block_en1.close() 
block_en2.close() 
nor.close()	  
