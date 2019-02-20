import PIL.ImageDraw as ID, PIL.Image as Image, PIL.ImageShow as IS
from math import *
im = Image.new("RGB", (640,480))
draw = ID.Draw(im)
d=int(input("Distance from screen:"))
f=[[1,0,0,0],[0,1,0,0],[0,0,0,0],[0,0,0,1/d]]
def ref(f,x,y,z,d):
   temp=[]
   xref=f[0][0]*x + f[0][1]*y + f[0][2]*z + f[0][3]*1
   yref=f[1][0]*x + f[1][1]*y + f[1][2]*z + f[1][3]*1
   a=xref/(1+(z/d))
   b=yref/(1+(z/d))
   temp.append((int(a),int(b)))
   return temp
p=[(200,200,100),(300,200,100),(300,300,100),(200,300,100),(250,150,0),(350,150,0),(350,250,0),(250,250,0)]
new=[]
for i in p:
   b=ref(f,i[0],i[1],i[2],d)
   new.append(b)
print(new)   
draw.polygon((new[0][0],new[1][0],new[2][0],new[3][0]),outline=(255,255,255))
draw.polygon((new[1][0],new[5][0],new[6][0],new[2][0]),outline=(255,255,255))
draw.polygon((new[0][0],new[4][0],new[7][0],new[3][0]),outline=(255,255,255))
draw.polygon((new[4][0],new[5][0],new[6][0],new[7][0]),outline=(255,255,255))
im.show()
