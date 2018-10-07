# encoding: utf-8
import matplotlib as mpl
import matplotlib.pyplot as plt
import os
from natsort import natsorted, ns
import numpy
import re
import xlsxwriter

def start():
	directory = 'result_exe1/'
	arq = os.listdir(directory)
	arquivosDiretorio = natsorted(arq, alg=ns.IGNORECASE) #ordena arquivos para plot
	size = len(arquivosDiretorio)

	cenarios = []
	for i in range(size):
		cenarios.append(re.findall('\d+',arquivosDiretorio[i]))

	alfa, beta = zip(*cenarios)

	throughput_list = []
	queueingDelay_list = []
	signalDelay_list = []
	for i in range(size):
		with open(directory + '/'+ arquivosDiretorio[i], 'r') as f:
			try:
				lines = f.read().splitlines()

				throughput_line = lines[4].split()
				throughput = throughput_line[2]
				throughput_list.append(throughput)

				queueingDelay_line = lines[5].split()
				queueingDelay = queueingDelay_line[5]
				queueingDelay_list.append(queueingDelay)

				signalDelay_line = lines[6].split()
				signalDelay = signalDelay_line[4]
				signalDelay_list.append(signalDelay)

			except:
				print('Erro na leitura dos arquivos')

	x = [float(i) for i in signalDelay_list]
	y = [float(i) for i in throughput_list]
	w = [] #Throughput/Delay ou Potencia
	for i in range(len(x)):
		w.append(y[i]/(x[i]*0.001))

	x_str = []
	for i in range(size):
		x_str.append("{:.2f}".format(x[i]))

	y_str = []
	for i in range(size):
		y_str.append("{:.2f}".format(y[i]))

	w_str = []
	for i in range(size):
		w_str.append("{:.2f}".format(w[i])) #{:.2e}


	dados = zip(alfa,beta, y_str,x_str,w_str)

	#dados = {"alfa": alfa, "beta": beta}
	
	workbook = xlsxwriter.Workbook('tabela.xls')
	worksheet = workbook.add_worksheet('tab')

	head = ('Alfa', 'Beta', 'Throughput (Mbps)', 'Atraso (ms)', 'Potencia')

	dados.insert(0, head)
	#worksheet.write_row(0,0, head)
	for row, item in enumerate(dados):
		worksheet.write_row(row,0,item)

	workbook.close()



	# f = open('tabela.csv','w')
	# for i in range(size):
	# 	row = alfa[i] + " " + beta[i] + " " + y_str[i] + " " + x_str[i] + " " + w_str[i]		
	# 	f.write(row)


	#y_str = ":.2f"
	#w_str = ''.join(w)


	# dados = zip(alfa,beta, y,x,w)
	# print(dados)

	# f = open('tabela.csv','w')
	# for i in range(size):
	# 	f.write(dados[i]) 

	# f.close()




	#print(dados)
	#fieldnames = ('Alfa', 'Beta', 'Throughput (Mbps)', 'Atraso (ms)', 'Potência')



		# writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		# writer.writeheader()
    	# for i in range(size):
    	#  	print(dados[i])
    	#  	writer.writerow()
    	#  	writer.writerow(dados[i])
    	 	

	# fig, ax = plt.subplots()
	# dados = zip(alfa,beta, y,x,w)
	
	# collabel=('Alfa', 'Beta', 'Throughput (Mbps)', 'Atraso (ms)', 'Potencia')
	# table = ax.table(cellText=dados,colLabels=collabel,loc='center')
	# table.auto_set_font_size(False)
	# table.set_fontsize(22)	
	# plt.show()



if __name__ == "__main__":
	start()
