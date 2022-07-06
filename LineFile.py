# Write A Program To Count  The Number Of Line In The File.

f = open("E:\\info.txt","r")
count=0

for i in f:
    count=count+1

print("The No. Of Lines In Files Is:",count)

f.close()
