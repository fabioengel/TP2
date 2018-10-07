# encoding: utf-8
import matplotlib as mpl
import matplotlib.pyplot as plt
import os
from natsort import natsorted, ns
import numpy


windowsSize = []

def leituraDados(n):
	directory = 'result_exe'+str(n)+'/'
	arq = os.listdir(directory)
	arquivosDiretorio = natsorted(arq, alg=ns.IGNORECASE) #ordena arquivos para plot
	size = len(arquivosDiretorio)

	global windowsSize
	windowsSize = []
	for i in range(size):
		valor =  ''.join(i for i in arquivosDiretorio[i] if i.isdigit())
		windowsSize.append(valor)



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
	z = [int(i) for i in windowsSize]
	w = [] #Throughput/Delay
	for i in range(len(x)):
		w.append(y[i]/(x[i] * 0.001))

	return x,y,z,w


def start():
	x1,y1,z1,w1 = leituraDados(1)
	x2,y2,z2,w2 = leituraDados(2)
	x3,y3,z3,w3 = leituraDados(3)
	x4,y4,z4,w4 = leituraDados(4)
	x5,y5,z5,w5 = leituraDados(5)

	x = calculamedia(x1,x2,x3,x4,x5)
	y = calculamedia(y1,y2,y4,y4,y5)
	z = calculamedia(z1,z2,z3,z4,z5)
	w = calculamedia(w1,w2,w3,w4,w5)
	print(w)


	tam = len(y1)
	plotgrafico(x, y, z, w, tam)


def calculamedia(a1, a2, a3, a4, a5):
	a = []
	tam = len(a1)

	for i in range(tam):
		media = (a1[i] + a2[i] + a3[i] + a4[i] + a5[i])/5
		a.append(media)

	return a



def plotgrafico(x, y, z, w, tam):
	fig1 = plt.figure()
	ax1 = fig1.add_subplot(111)
	ax1.scatter(x,y, color='b', label='Taxa de transmissao x Atraso do sinal')
	ax1.set_xlabel('Atraso do sinal com percentil de 95%')
	ax1.set_ylabel('Taxa de transmissao')


	for i in range(tam):
		ax1.text(x[i]+20, y[i],windowsSize[i],ha ='left',rotation=10, wrap=True)

	plt.autoscale(enable=True, axis='both', tight=None)


	
	fig2 = plt.figure()
	ax2 = fig2.add_subplot(211)
	

	ax2.bar(z,w,color='r',label='Tamanho da janela de transmissao x Taxa de transferencia/Atraso')
	ax2.set_xlabel('Tamanho da janela de transmissao')
	ax2.set_ylabel('Taxa de transferencia/Atraso')
	plt.xticks(z, windowsSize,rotation='horizontal')
	ax2.axis([min(z), max(z), min(w), max(w)])

	ax3 = plt.subplot(212)
	ax3.bar(z,w,color='r',label='Tamanho da janela de transmissao x Taxa de transferencia/Atraso (Zoom)')
	ax3.set_xlabel('Tamanho da janela de transmissao')
	ax3.set_ylabel('Taxa de transferencia/Atraso')
	plt.xticks(z, windowsSize,rotation='horizontal')
	ax3.axis([min(z), 30, min(w), max(w)])
	for i in range(tam):
		ax3.text(z[i] - 0.4, w[i] - 2, "{:.2f}".format(w[i]) ,ha ='left',color="w", wrap=True)


	plt.show()
	
	#plt.savefig('Fig1.png')



if __name__ == "__main__":
	start()
