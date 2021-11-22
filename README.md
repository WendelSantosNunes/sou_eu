# sou_eu

## Crachá personalizado com dados do github e/ou QRcodes dos perfis do Facebook e Instagram

<p> Usuário completo </p>

![Usuário + QRcode do Facebook + QRcod do Instagram](https://raw.githubusercontent.com/WendelSantosNunes/thatsme/main/demo/UC.png)

<p> Usuário básico </p>

![Usuário + QRcode do Github](https://raw.githubusercontent.com/WendelSantosNunes/thatsme/main/demo/UB.png)

O sou_eu foi criado em python3.8. O sistema pode ser usado em Windows, Linux e Mac.

Colaboradores: <br />

1. [Wendel Nunes](https://github.com/WendelSantosNunes) <br />
2. [Eva Luana](https://github.com/evalasilva) <br />

### Descrição:

> O sou_eu é um pacote criado durante a disciplina de Programação Orientada a Objetos 2 (POO2), ministrada no curso de Sistema de Informação na Universidade Federal do Piauí-CSHNB.
> Não há intuito comercial, ou governamental.
> O sou_eu foi produzido para fins de aprendizado e experiência em desenvolvimento de pacotes, contudo pode ser utilizado por qualquer usuário do Github que tenha interesse. O projeto possui a Licença do MIT disponibilizada pelo próprio Github.
> O sou_eu pode ser utilizado como cartão virtual, em formato PDF, para qualquer pessoa física/jurídica que queira compartilhar suas informações de contato de forma padronizada, elegante e eficiente.

## Requisitos:

1. [python3](https://www.python.org/downloads/)
2. [pip](https://pip.pypa.io/en/stable/installation/)

## Instalação:

### Python3

1. Windows: [Download](https://www.python.org/downloads/)

2. Linux Debian e derivados.

   ```
       $ sudo apt-get install python3
   ```

### PIP

1. Instalação do PIP - LINUX

   ```Debian
   	$ sudo  apt-get install python-pip
   ```

   ```Red Hat/ OpenSUSe
   	$ sudo  yum install python-pip
   ```

### thatsme

1. Instalação do thatsme

   pip install thatsme

## Execução:

1.  Instale o pacote;
2.  Importe a classe Cracha:
    (from cracha import Cracha);
3.  Crie um objeto da classe:

    3.1. O objeto deve enviar como parâmetro("endereco_local_armazenar_pdf","nome_usuario_github","url_perfil_facebook", "url_perfil_instagram");

        from sou_eu import thatsme

        usuario = thatsme.Cracha('endereco','usuario_github', 'url_perfil_facebook', 'url_perfil_instagram')

        usuario.cracha()

    3.2. O parâmetro "nome_usuario_github" é obrigatório;
    3.3. Caso não hajam as URLs dos perfins do Facebook e/ou Instagram, deve ser inserido "None" no local devido;

        from sou_eu import thatsme

        usuario = thatsme.Cracha('endereco','usuario_github', None, 'url_perfil_instagram')

        usuario.cracha()

    3.4. Para o caso de não haver URL do Facebook nem do Instagram será adicionado o QRcode do perfil do usuário no Github;

    3.5. Se o usuário do Github não for encontrado será apresentado o ERROR 404.
