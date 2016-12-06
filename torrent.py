# -*- coding: utf-8 -*-
import libtorrent, time, os

class Torrent():
    def __init__(self, caminho, magnet):
        self.caminho = caminho
        self.params = { 
                'save_path' : '/home/'+os.getlogin()+'/Downloads/'+self.caminho,
                'storage_mode' : libtorrent.storage_mode_t(2),
                'paused' : False,
                'auto_managed' : True,
                'duplicate_is_error' : True 
                }
        self.magnet = magnet

    def connect(self):
        
        session = libtorrent.session()
        session.listen_on(6881, 6891)
        print("Salvando o arquivo .torrent em: " + self.caminho + "...")

        handle = libtorrent.add_magnet_uri(session, self.magnet, self.params)
        session.start_dht()
        while(not handle.has_metadata()):
            time.sleep(.1)

        info = handle.get_torrent_info()

        store = libtorrent.file_storage()

        for arquivo in info.files():
            store.add_file(arquivo)

        torarquivo = libtorrent.create_torrent(store)
        torarquivo.set_comment(info.comment())
        torarquivo.set_creator(info.creator())

        f = open(self.caminho, "wb")

        f.write(libtorrent.bencode(torarquivo.generate()))
        f.close()

        print("Começando o download...")

        s = handle.status()

        while(s.state != libtorrent.torrent_status.seeding):
            time.sleep(10)
            print("\nBaixando...")
            print("%.2f COMPLETOS\n%.1f kbps DOWNLOAD" % (s.progress * 100, s.download_rate/1000)) 
            s = handle.status()
