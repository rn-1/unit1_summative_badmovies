# god has left us and this file this file killed him.
import requests as r
from bs4 import BeautifulSoup as BS
url = "https://www.rottentomatoes.com/browse/dvd-streaming-all?minTomato=0&maxTomato=9&services=amazon;hbo_go;itunes;netflix_iw;vudu;amazon_prime;fandango_now&genres=1;2;4;5;6;8;9;10;11;13;18;14&sortBy=release"
soup = r.get(url).content
data = BS(soup,"html.parser")
class movie(): #this is a class that pretty much does nothing other than hold all these functions. Which sucks, but oh well.
    def __init__(self): #get the data we want. Clean it up and prep it for the rest of the class to use. 
        mov = data.select(".body_main")
        parse = BS(str(mov),"html.parser")
        scripts = parse.find_all("script")
        check = "[{\"id\""
        thing = []
        for sc in scripts:
            if check in str(sc):
                #print(sc)
                thing.append(str(sc).strip())
        thing = thing[0].split('\n')
        for i in thing:
            if check in i:
                thing = [i]
        return thing
    def findGeneral(self,data,check): #A function used to find most of the information we want. This doesn't include actors, as this first split would mess with the script.
        data = data[0].split(',\"') # Separating it by commas, this makes it far easier to find the stuff.
        result = []
        for d in data:
            if check in d:
                result.append(d.strip(check))
        return result
    def actors(self,data): #Find the actors. This is similar to findGeneral, but somewhat different.
        data = data[0].split(',\"')
        result = []
        check = "actors\":"
        for d in data:
            if check in d:
                index = data.index(d)
                temp = data[index:index+1]
                temp = temp[0].split('},{')
                for n in temp:
                    if check in n:
                        temp = n.strip(check)
                result.append(temp)
        return result
    def summary(self,mn,r,a,s): #Compile this stuff into a dict.
        summ = {}
        elvisgone = False
        for i in range(len(mn)):
            if mn[i] == "Elvis from Outer Spac":
                summ[mn[i]] = r[i],"Unlisted",s[i]
                elvisgone = True
            elif elvisgone == True:
                summ[mn[i]] = r[i],a[i-1],s[i]
            else:
                summ[mn[i]] = r[i],a[i],s[i]
        return summ
        
#main. Doesn't really mean much, just a place where all the values are put in the right scope.
stuff = movie.__init__(movie) #Initialise the stuff, get the data.
movienames = movie.findGeneral(movie,stuff,"title\":") #Search the block of text for data pieces with the desired tag.
ratings = movie.findGeneral(movie,stuff,"tomatoScore\":") #Ditto
actors = movie.actors(movie,stuff) #Actors is different because of the website's format.
syn = movie.findGeneral(movie,stuff,"synopsis\":") #Finds the synopsis string, makes a list of them.
full = movie.summary(movie,movienames,ratings,actors,syn) #Takes all previous data and creates a dictionary with {names:ratings,actors,syn}.
#print commands, for debugging mainly.

#print(stuff)
#print(movienames)
#print(ratings)
#print(actors)
#print(syn)
#print(full)
print("""This is a discount rotten tomatoes.
Note that movie descriptions are ordered as follows:
Rating, Key actors, and Synopsis.
Inputs are sanitized, but avoid the '' around titles. Below are a list of available movies to look at:""")
print(movienames)
while True:
    inp = str(input("Which movie would you like to view?:"))
    inp = inp.strip('\"')
    inp = inp.strip()
    print(inp)
    try:
        print(full[inp])
        continue
    except:
        print("That movie is not listed, or there might be a typo:",inp)
        continue