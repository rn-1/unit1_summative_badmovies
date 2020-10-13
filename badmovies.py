# god has left us and this file this file killed him.
import requests as r
from bs4 import BeautifulSoup as BS
url = "https://www.rottentomatoes.com/browse/dvd-streaming-all?minTomato=0&maxTomato=10&services=amazon;hbo_go;itunes;netflix_iw;vudu;amazon_prime;fandango_now&genres=1;2;4;5;6;8;9;10;11;13;18;14&sortBy=release"
soup = r.get(url).content
data = BS(soup,"html.parser")
class movie():
    def __init__(self):
        mov = data.select(".body_main")
        return mov
    def rating(self,data):
        ratings = []
        souped = BS(str(data),"html.parser")
        r = souped.find_all("span",class_="tMeterScore")
        for i in r:
            hell = BS(str(i),"html.parser")
            s = hell.span.contents
            #print(s[0].replace('%',""))
            x = s[0].replace('%',"")
            ratings.append(int(x))
        return ratings
    def movienames(self,data):
        souped = BS(str(data),"html.parser")
        mn = souped.find_all("h3",class_="movieTitle")
        names = []
        for n in mn:
            pain = BS(str(n),"html.parser")
            b = pain.h3.contents
            names.append(b)
        return names
    def actors(self,data):
        souped = BS(str(data),"html.parser")
        aa = souped.find_all("p",class_="actors")
        names = []
        for n in aa:
            pain = BS(str(n),"html.parser")
            b = pain.p.contents
            names.append(b)
        return names
    def synopsis(self,data):
        souped = BS(str(data),"html.parser")
        aa = souped.find_all("span",class_="consensus-text")
        names = []
        for n in aa:
            pain = BS(str(n),"html.parser")
            b = pain.span.contents
            names.append(b)
        return names
    def summary(self,mn,r,a,s):
        summ = {}
        for i in names:
            pass
        return None
        pass
        
#main
stuff = movie.__init__(movie)
names = movie.movienames(movie,stuff)
ratings = movie.rating(movie,stuff)
actors = movie.actors(movie,stuff)
syn = movie.synopsis(movie,stuff)
full = movie.summary(movie,names,ratings,actors,syn)
#print(stuff)
print(names)
print(ratings)
print(actors)
print(syn)