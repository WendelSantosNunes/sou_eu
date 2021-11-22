import pyqrcode
import png
import urllib.request
import json
from fpdf import FPDF


class Dados():

    __slots__ = ['_nome']

    def __init__(self, nome):
        self._nome = nome

    @property
    def nome(self):
        return self._nome

    def github(self):

        with urllib.request.urlopen("https://api.github.com/users/{}".format(self.nome)) as url:
            dados = json.loads(url.read().decode())
        dados = 0

        return dados


class Cracha():

    def __init__(self,  endereco, usuario_github, url_facebook=None, url_instagram=None):
        self._endereco = endereco
        self._github = usuario_github
        self._url_facebook = url_facebook
        self._url_instagram = url_instagram

    @property
    def endereco(self):
        return self._endereco

    @property
    def url_facebook(self):
        return self._url_facebook

    @property
    def url_instagram(self):
        return self._url_instagram

    @property
    def github(self):
        return self._github

    # badge
    def cracha(self):
        if self.url_facebook != None:
            Qrcode(self.url_facebook).qrcode().png(
                "Facebook.png", scale=6, module_color=[228, 87, 118], background=[248, 197, 33])
        if self.url_instagram != None:
            Qrcode(self.url_instagram).qrcode().png("Instagram.png", scale=6,
                                                    module_color=[228, 87, 118], background=[248, 197, 33])
        if self.url_facebook == None and self.url_instagram == None:
            Qrcode('https://github.com/' +
                   self.github).qrcode().png("Github.png", scale=6, module_color=[228, 87, 118], background=[248, 197, 33])

        dados = Dados(self.github).github()
        if dados != 0:
            pdf.header(self.endereco, dados,
                       self.url_facebook, self.url_instagram)


class Qrcode:

    def __init__(self, url_social):
        self._url_social = url_social

    @property
    def url_social(self):
        return self._url_social

    def qrcode(self):
        qr = pyqrcode.create(self.url_social)
        return qr


class Dados():

    __slots__ = ['_nome']

    def __init__(self, nome):
        self._nome = nome

    @property
    def nome(self):
        return self._nome

    def github(self):
        with urllib.request.urlopen("https://api.github.com/users/{}".format(self.nome)) as url:
            dados = json.loads(url.read().decode())

        return dados


class pdf:
    def header(endereco, dados, url_facebook, url_instagram):

        fpdf = FPDF('L', 'mm', (100, 150))
        fpdf.add_page()

        Fundo = 'https://github.com/WendelSantosNunes/thatsme/blob/main/src/thatsme/Rectangle%201.png?raw=true'
        Desktop = 'https://github.com/WendelSantosNunes/thatsme/blob/main/src/thatsme/Desktop.png?raw=true'

        fpdf.image(Fundo, 0, 0, 180)
        fpdf.image(Desktop, -30, -10, 210)

        # fonte
        fpdf.set_font('helvetica', '', 10)
        fpdf.set_text_color(255, 255, 255)

        # qrcode
        if url_facebook != None and url_instagram != None:
            fpdf.image('Facebook.png', 95, 30, 25)
            fpdf.image('Instagram.png', 95, 60, 25)
        elif url_instagram != None:
            fpdf.image('Instagram.png', 95, 30, 25)
        elif url_facebook != None:
            fpdf.image('Facebook.png', 95, 30, 25)
        else:
            fpdf.image('Github.png', 95, 30, 25)

        # dados do github

        fpdf.image(dados['avatar_url'], 30, 30, 25)
        fpdf.ln(50)
        fpdf.text(30, 60, dados['login'])
        fpdf.ln(3)
        effective_page_width = (fpdf.w - 9*fpdf.l_margin) + 10
        if dados['bio']:
            fpdf.multi_cell(effective_page_width, 5,
                            dados['bio'], border=0, align='C')
        fpdf.output(endereco + '/Crachá.pdf')
