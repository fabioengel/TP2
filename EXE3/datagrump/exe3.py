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

	throughput_list = []
	queueingDelay_list = []
	signalDelay_list = []
	for i in range(size):
		with open(directory + '/'+ arquivosDiretorio[i], 'r') as f:
			try:
				lines = f.read().splitlines()

				throughput_line = lines[-5].split()
				throughput = throughput_line[2]
				throughput_list.append(throughput)

				queueingDelay_line = lines[-4].split()
				queueingDelay = queueingDelay_line[5]
				queueingDelay_list.append(queueingDelay)

				signalDelay_line = lines[-3].split()
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


	x_ = range(1,size+1)

	fig1 = plt.figure()
	ax1 = fig1.add_subplot(211)
	ax1.scatter(x,y, color='b', label='Taxa de transmissao x Atraso do sinal')
	# for i in range(size):
	# 	ax1.text(x[i]+0.05,y[i], x_[i], ha ='left',color="k", fontsize=8,wrap=True)
	ax1.set_xlabel('Atraso do sinal com percentil de 95% (ms)')
	ax1.set_ylabel('Taxa de transmissao (Mbps)')

	ax2 = plt.subplot(212)
	
	ax2.bar(x_, w,color='r')
	for i in range(size):
		#ax2.text(x_[i] - 0.15, w[i] - 0.5, "{:.2f}".format(w[i]) ,ha ='left',color="w", wrap=True)
		#ax2.text(x_[i] - 0.35, w[i] - 1, "{:.2f}".format(w[i]) ,ha ='left',color="w", fontsize=8,wrap=True)
		ax2.text(x_[i] - 0.35, w[i] - 2, "{:.2f}".format(w[i]) ,ha ='left',color="w", fontsize=8,wrap=True)

	#for i in range(size):
		#ax1.text(x[i] - 0.4, y[i] - 2, "{:.2f}".format(w[i]) ,ha ='left',color="w", wrap=True)
		#ax1.text(x[i], y[i], str(i) + ' ' + w_str[i] ,ha ='left',color="r", wrap=True)
	ax2.set_xticks(range(1,size+1))
	ax2.set_ylabel('Taxa de transmissao x Atraso do sinal')
	ax2.set_xlabel('Execucao')
	plt.show()

if __name__ == "__main__":
	start()
