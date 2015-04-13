import urllib.request
import xml


x = urllib.request.urlopen("http://ht.wikipedia.org/w/api.php?action=query&titles=Mango,_Granma&prop=revisions&rvprop=content&format=xml")
print(x.read())#, file=open('output.xml', "w"))
print(x.getcode())


