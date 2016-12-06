from lxml import html
import requests

class PB():
    
    def __init__(self, busca):
        self.busca = 'https://thepiratebay.org/search/'+busca+'/0/99/0'
        self.itens = []
        self.links = []

    def get_links(self):
        pagina = requests.get(self.busca)
        tree = html.fromstring(pagina.content)

        self.itens += tree.xpath("//tr//div[@class='detName']//a/text()")
        self.links += tree.xpath("//tr//a[@title='Download this torrent using magnet']/@href")
