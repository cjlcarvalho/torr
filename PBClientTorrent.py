#! /usr/bin/env python
# -*- coding: utf-8 -*-
from torrent import Torrent
from lxml import html
import requests

def main():
    print("Pirate Bay Terminal Client")
    busca = raw_input("\nPesquisar: ")
    num = int(raw_input("Número máximo de arquivos: "))
    url = 'https://thepiratebay.org/search/'+busca+'/0/99/0'
    
    pagina = requests.get(url)
    tree = html.fromstring(pagina.content)

    itens = tree.xpath("//tr//div[@class='detName']//a/text()")
    links = tree.xpath("//tr//a[@title='Download this torrent using magnet']/@href")

    if links:
        for i in range(num):
            print(str(i+1) + " - " + itens[i])
        escolha = int(raw_input("\nEscolha: ")) - 1

        magnet = links[escolha]
        caminho = itens[escolha]
        torrent = Torrent(caminho, magnet)
        
        torrent.connect()

    else:
        sys.exit("Não foram encontrados torrents com sua busca.")

if __name__ == '__main__':
    main()
