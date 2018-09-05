O arquivo universe.py contido nesta pasta é apenas para testes isolados, e não está atualizado.

Para utilizar a biblioteca, agora você deve instalá-la via PIP:

> pip3 install htdp-pt-br

ou, no Windows:

> py -m pip install htdp-pt-br

Isto já instalará também as bibliotecas necessárias, como o Pygame, caso ainda não estejam instaladas.

Para atualizar para a versão mais nova, rode o comando da seguinte forma:

> pip3 install htdp-pt-br --upgrade

Para utilizar a biblioteca, você deve importá-la da seguinte forma no início do seu código:

> from htdp_pt_br.universe import *

Caso você for trabalhar apenas com imagens (sem animações), poderá importar apenas o módulo ``image``:

> from htdp_pt_br.image import *