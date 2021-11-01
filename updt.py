import subprocess as sp

def update(data):
	if ":" in data:
		data = list(set([x.split(":")[1].strip() for x in data.splitlines() if x != ""]))
	else:
		data = [data.strip()]
	f = list(set([i.strip() for i in open("mydev.txt","r").readlines()]))
	n = 0
	if len(data) < 2:
		d = data[0]
		if d in f:
			print(d,"data sudah ada, skip")
		else:
			f.append(d)
			n += 1
			print(d,"data baru ditambahkan")

	else:
		print(data)
		for d in data:
			if d in f:
				print(d,"data sudah ada, skip")
			else:
				f.append(d)
				n += 1
				print(d,"data ditambahkan")
	print(n, "data berhasil ditambahkan")
	print("menulis file..")
	with open("mydev.txt","w") as file:
		for x in f:
			file.write(x+"\n")
		file.close()
	print("done.")
	print("update repository..")
	sp.call(f"git add *;git commit -am 'nambahin {data}';git push -u https://github.com/karjok/karjok.git",shell=True,stdout=sp.PIPE)
	print("done.")

data = """
[1/11 6.23 PM] Bg Ardi Customer: 20999926e3c698ccf02e1b1941d2f5a4
[1/11 6.29 PM] Bg Ardi Customer: 38260461ce089c9d938b393f03748f0b
[1/11 6.31 PM] Bg Ardi Customer: 38260461ce089c9d938b393f03748f0b
[1/11 7.01 PM] Bg Ardi Customer: cdba7ccbe8897dd79f2fd4952cb5c8a1
"""
update(data)
