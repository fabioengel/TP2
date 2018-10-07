#!/bin/bash
lista=('1' '2' '3' '4' '5' '6' '7' '8' '9' '10' '11' '12' '13' '14' '15' '16' '17' '18' '19' '20' '22' '24' '26' '28' '30' '40' '50' '60' '70' '80' '90' '100' '110' '120' '130' '140' '150' '160' '170' '180' '190' '200' '220' '240' '280' '300' '350') 
numtestes=5

for n in $(seq 1 $numtestes)
do
	for i in ${lista[@]}
do	
	echo Experimento com window size = $i
	sed -i 's/unsigned int the_window_size =.*/unsigned int the_window_size = '$i';/' controller.cc

	cd ..
	make
	cd datagrump
	
	./run-contest fabio &> 'result_exe'$n'/windowsize'$i'.txt'
	echo ok
	done
done
