from cd import *



if __name__ == '__main__':
    conf = ["cdROM","1GB"]
    cdp = Audio(conf)
    files = ["cancion1","cancion2","cancion3"]
    cdp.guardar(files)
    cdp.search()
        




