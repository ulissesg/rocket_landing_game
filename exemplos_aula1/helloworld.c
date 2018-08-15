#include <stdio.h>

/**
Compile com o gcc no linux para entender o que é um compilador.
No terminal:
cd /este/diretorio                   (substitua pelo caminho do diretório (pasta) em que se encontra este arquivo)
gcc helloworld.c                    (gera executável de nome a.out)
./a.out                             (executa programa)
gcc helloworld.c -o helloworld      (gera executável de nome 'helloworld')
./helloworld                        (executa programa)

OBS: Uma IDE NÃO é um compilador: apenas chama um compilador.

IDE = Integrated Development Environment
*/

int main(){
    int x = 1 + 1;
    printf("Ola mundo. %d \n", x);

    return 0;
}