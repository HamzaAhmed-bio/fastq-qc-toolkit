output = open("sample.fastq", "w")

output.write("@read1\n")
output.write("GATTACAGATTACAGATTACA\n")
output.write("+\n")
output.write("IIIIIIIIIIIIIIIIIIIII\n")

output.write("@read2\n")
output.write("GATTACAGATTACAGATTNNN\n")
output.write("+\n")
output.write("IIIIIIIIIIIIIIII!!!!!\n")

output.close()

print("Made sample.fastq")
