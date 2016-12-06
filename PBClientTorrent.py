#! /usr/bin/env python
# -*- coding: utf-8 -*-
from torrent import Torrent
from scrap import PB
from lxml import html
import requests, sys

def main():
    print("Pirate Bay Terminal Client")
    busca = raw_input("\nPesquisar: ")
    num = int(raw_input("Número máximo de arquivos: "))
    
    pb = PB(busca)
    pb.get_links()
    
    if pb.links:
        for i in range(num):
            print(str(i+1) + " - " + pb.itens[i])
        escolha = int(raw_input("\nEscolha: ")) - 1

        magnet = pb.links[escolha]
        caminho = pb.itens[escolha]
        torrent = Torrent(caminho, magnet)
        
        torrent.connect()

    else:
        sys.exit("Não foram encontrados torrents com sua busca.")

if __name__ == '__main__':
    main()
