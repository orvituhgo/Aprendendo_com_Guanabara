import urllib.request

def verificarSite(linkcomhttp):
    while True:
        try:
            site = urllib.request.urlopen(linkcomhttp)
        except:
            print('O site não está disponível')
        else:
            print('O site está disponível')
            print(site.read())
            break

verificarSite('http://www.pudim.com.br/')
