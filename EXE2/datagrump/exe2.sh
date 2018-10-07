#!/bin/bash
#lista=('1' '2' '3' '4' '5' '6' '7' '8' '9' '10' '11' '12' '13' '14' '15' '16' '17' '18' '19' '20' '30' '40' '50' '60' '70' '80' '90' '100' '110' '120' '130' '140' '150' '160' '170' '180' '190' '200' '220' '240' '280' '300' '350') 
#for i in $(seq 3)
janelaInicial=13
#alfaLista=('1' '2' '3') # valor aumentado
#alfaLista=('3' '4' '5' '6' '7' '8' '9' '10' '11' '12' '13' '14' '15' '16' '20') # valor aumentado
alfaLista=( '9' '10' '11' '12' '13' '14' '15' '16' '20')
#betaLista=('1' '2' '3' '4' '5' '6' '7' '8') # fator de redução
betaLista=('1' '2' '3' '4' '5' '6' '7' '8' '9' '10' '11' '12' '13' '14' '15' '16' '17' '18' '19' '20') # fator de redução
#betaLista=('1' '2' '3' '4' '5' '6' '7' '8' '9' '10') # fator de redução

#Escreve o tamanho de janela inicial escolhido no arquivo Controller.cc
sed -i 's/unsigned int the_window_size =.*/unsigned int the_window_size = '$janelaInicial';/' controller.cc

for i in ${alfaLista[@]}
do
	for j in ${betaLista[@]}
	do
		sed -i 's/unsigned int alfa =.*/unsigned int alfa = '$i';/' controller.cc
		sed -i 's/unsigned int beta =.*/unsigned int beta = '$j';/' controller.cc
		echo Experimento com alfa = $i e beta = $j
		cd ..
		make
		cd datagrump
		./run-contest fabio &> 'result_exe1/alfa'$i'_beta'$j'.txt'
		echo ok
	done
done



