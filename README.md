# Minicurso Python

Arquivos fonte para a apresentação de um minicurso de Python ministrado para os membros do Ramo Estudantil IEEE CEFET/RJ durante os dias 30 e 31 de janeiro; e 01 de fevereiro de 2019.

## Visualização

Se deseja apenas vizualizar a apresentação:
- Baixe a versão mais recente na página de [releases](https://github.com/Lukff/minicurso-python/releases);
- Extraia o arquivo '.zip';
- Entre na pasta extraída;
- Abra o arquivo '.html' da apresentação utilizando um navegador recente (ex: Firefox, Google Chrome).

## Modificação

Se deseja modificar a apresentação, clone este repósitorio com o git:

> $ git clone https://github.com/Lukff/minicurso-python.git

As seções seguintes explicam o funcionamento do projeto.

### Estrutura

- markdown/

Arquivos fonte para a apresentação, escritos em markdown ([Pandoc's Markdown](https://pandoc.org/MANUAL.html#pandocs-markdown)).

- img/

Imagens utilizadas na apresentação.

- reveal.js/

Arquivos da biblioteca [reveal.js](https://revealjs.com/). Essa é a dependência principal do projeto, os arquivos foram incluídos no repositório por questão de praticidade.

- Makefile

Arquivo para automatizar a compilação dos fontes.

### Dependências para desenvolvimento

- [Reveal.js](https://revealjs.com/)
  - A biblioteca reveal.js é necessária para funcionamento da apresentação. O release utilizado para o desenvolvimento foi o 3.7 (já incluído no projeto).
- [Pandoc](https://pandoc.org/)
  - É necessário que o pandoc esteja instalado na máquina para  realizar a conversão dos arquivos markdown para html compatível com o reveal.js.
- [GNU make]
  - É necessário que o make estaja instalado na máquina para utilizar o 'Makefile'.

### Instruções

Após suprir as dependências do projeto, altere os arquivos '.md' contidos na pasta markdown conforme desejar.

Para gerar uma nova apresentação a partir dos arquivos alterados, execute o make sem argumentos a partir da pasta raíz do projeto.

> $ make
