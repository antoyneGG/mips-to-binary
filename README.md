# MipsToBinary

MipsToBinary es un programa que ejecuta una interfaz grafica simple, la cual cuenta con un un boton de Open (para cargar archivos .txt o .s), otro boton de Translate, el cual da inicio al proceso de traduccion, y un espacio de Frecuency, para agregar con la frecuencia de maquina que se quiera calcular el programa. Y finalmente tanto el texto que se ingresa para la traduccion como el texto traducido aparecera en un recuadro blanco de texto que se encuentra a la derecha.

## Instrucciones

Este es un ejemplo de como lee la sintaxis el programa:
lui $s0,0x1000
ori $s0,$s0,0x0400
lw $s3,12($s0)
lw $s4,16($s0)
lw $s5,0($s0)
ciclo:
beq $s3,$s4,salir
sub $s5,$s5,$s3
sw $s5,0($s0)
j ciclo 
salir:
lw $s1,4($s0)
lw $s2,8($s0)
add $s5,$s1,$s2
jr $ra
Notese que los labels deben ir siempre en una linea separada y finalizados con el caracter ':'. Tambien cabe resaltar que no se deben dejar lineas en blanco en medio del programa. Cada instruccion ocupa una linea, y estas deben venir tal cual como se encuentran en este ejemplo, separando con un espacio en blanco la instruccion de sus parametros y los parametros separados por comas.
Y por ultimo debe siempre revisarse que se haya colocado una frecuencia de reloj, pues en caso contrario el programa no correria.
Una vez la sintaxis este bien escrita se podra correr el programa con el boton Translate. Hay que añadir que si por algun descuido se comete algun error basico de sintaxis de instrucciones (como cantidad incorrecta de parametros, inmediato con tamaño muy grande, etc.) el programa se encargara de detener todo el proceso de traduccion y avisar de dicho error, esto con el fin de que se sepa donde o cual es el error y poder corregirlo.
