#!/bin/bash

#janelaInicial=13

#alfaLista=('11' )

#betaLista=('10') # fator de redução


#Escreve o tamanho de janela inicial escolhido no arquivo Controller.cc
#sed -i 's/unsigned int the_window_size =.*/unsigned int the_window_size = '$janelaInicial';/' controller.cc

for i in {1..30}
do
	./run-contest fabio &> 'result_exe1/'$i.'txt'
	mv /tmp/contest_uplink_log log/contest_uplink_log$i
done



	# for j in ${betaLista[@]}
	# do
	# 	sed -i 's/unsigned int alfa =.*/unsigned int alfa = '$i';/' controller.cc
	# 	sed -i 's/unsigned int beta =.*/unsigned int beta = '$j';/' controller.cc
	# 	echo Experimento com alfa = $i e beta = $j
	# 	cd ..
	# 	make
	# 	cd datagrump
	# 	./run-contest fabio &> 'result_exe1/alfa'$i'_beta'$j'.txt'
	# 	echo ok
	# done