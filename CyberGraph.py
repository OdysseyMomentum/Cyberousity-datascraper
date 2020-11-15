import tkinter
import random
import time
import winsound
    

width = 1400
height = 700
p = tkinter.Canvas(width=width, height=height)
p.pack()
p.configure(background="#374850")

red = "#FF5722"
red = "#FFEB3B"

xm = 0
ym = 0
V = 0
E = 0
R = "INFINITY"

pole = []

file = open("C:/Users/danko/Desktop/Currency Exchange/cmake-build-debug/test.txt", 'r')
for i, line in enumerate(file):
    if i == 0:
        V = int(line)
    if i == 1:
        E = int(line)
    if i == 3:
        if  '99999'in line:
            R = "INFINITY"
        else:
            R = float(line)
            print(line)
file.close()

p.create_text(700,50, text="Currency exchange problem", font="Corbel 30", fill="white")
p.create_line(100,50,380,50, fill="#879196")
p.create_line(1020,50,1300,50, fill="#879196")
p.update()
p.after(500)

p.create_line(250,100,250,height-70, width=2, dash=(8,5), fill="white")
p.create_text(120,135, text="Optimal path:", font="Corbel 17", fill="white")

p.create_text(120,540, text="Vertices: "+str(V), font="Corbel 13", fill="white")
p.create_text(120,570, text="Edges: "+str(E), font="Corbel 13", fill="white")
p.create_text(120,600, text="Rate: "+str(R), font="Corbel 13", fill="white")

p.create_line(40,510,200,510, width=2, dash=(8,5), fill="white")
#p.create_text(120,570, text="1 -> 3 -> 5 -> 7 -> 8", font="Calibri 14", fill=red)

toPrint = [(2,1,0.827341),(3,1,0.849146),(1,4,2.121445),(2,6,0.273184),(5,3,0.059532),(4,5,0.125820),(6,3,-0.138932),(5,6,0.896635),(7,5,1.775592),(8,7,2.061406),(5,8,-0.076542),(6,7,1.975613),(3,4,1.428037)]

isNegative = 0

def possible(x, y, x2, y2):
    dist = (pow(abs(x-x2),2)+pow(abs(y-y2),2))**(1/2)
    if (dist <= 150):
        return False
    else:
        return True

kolko = 0
temp = 0
file = open("C:/Users/danko/Desktop/Currency Exchange/cmake-build-debug/test.txt", 'r')
for i, line in enumerate(file):
    if i == 0:
        kolko = int(line)
        temp = int(line)
    if i == 2:
        if int(line) == 1:
            isNegative = 1

file.close()

array = []

z = 0
while (kolko != 0):
    x = random.randint(300,width-50)
    y = random.randint(120,height-100)
    if kolko > 10:
        z = random.randint(5, 13)
    else:
        z = random.randint(13, 23)
    ispossible = len(array)
    for i in array:
        if (possible(x, y, i[0], i[1])):
            ispossible -= 1
    if (ispossible == 0):
        kolko -= 1
        z = z+1.3
        array.append((x, y, temp-kolko, z))
        p.create_oval(x-15-z, y-15-z,x+15+z,y+15+z, fill="white", outline="#455A64", tag='a')
        p.create_text(x, y, text=temp-kolko, fill="black", font="Cursiva 15", tag='a')
        #winsound.Beep(random.randint(500,3000),100)
        p.after(30)
        p.update()

        

def addEdge(src, dest, w):
    w = round(w, 3)
    x=y=x2=y2=0
    print(array)
    for i in array:
        if (i[2] == src):
            x = i[0]
            y = i[1]
        if (i[2] == dest):
            x2 = i[0]
            y2 = i[1]
    farby = ["#879196","#9ba3a7","#afb5b9", "#FFFFFF", "#577273"]
    color = random.choice(farby)
    p.create_line(x, y, x2, y2, width=1, fill=color, tag='a')
    dist = (pow(abs(x-x2),2)+pow(abs(y-y2),2))**(1/2)
    if (x < x2 and y < y2):
        p.create_oval(x+(abs(x-x2)/2)-3, y+(abs(y-y2)/2)-3,x+(abs(x-x2)/2)+3, y+(abs(y-y2)/2)+3, fill=red, outline=red, tag='a')
        p.create_text(x+(abs(x-x2)/2), y+(abs(y-y2)/2)+15, text=w, fill="white", tag='a')

        #for i in range(2,10):
        #    p.create_oval(x+(abs(x-x2)/(dist/(65-(i*5))))-i, y+(abs(y-y2)/(dist/(65-(i*5))))-i,x+(abs(x-x2)/(dist/(65-(i*5))))+i, y+(abs(y-y2)/(dist/(65-(i*5))))+i, fill="white")

        p.create_oval(x+(abs(x-x2)/(dist/25))-8, y+(abs(y-y2)/(dist/25))-8,x+(abs(x-x2)/(dist/25))+8, y+(abs(y-y2)/(dist/25))+8, fill="white", outline="white", tag='a')
        p.create_oval(x+(abs(x-x2)/(dist/42))-6, y+(abs(y-y2)/(dist/42))-6,x+(abs(x-x2)/(dist/42))+6, y+(abs(y-y2)/(dist/42))+6, fill="#d7dadc", outline="#d7dadc", tag='a')
        p.create_oval(x+(abs(x-x2)/(dist/55))-3, y+(abs(y-y2)/(dist/55))-3,x+(abs(x-x2)/(dist/55))+3, y+(abs(y-y2)/(dist/55))+3, fill="#879196", outline="#879196", tag='a')
        p.create_oval(x+(abs(x-x2)/(dist/65))-2, y+(abs(y-y2)/(dist/65))-2,x+(abs(x-x2)/(dist/65))+2, y+(abs(y-y2)/(dist/65))+2, fill="#5e6c72", outline="#5e6c72", tag='a')

    if (x > x2 and y < y2):
        p.create_oval(x-(abs(x-x2)/2)-3, y+(abs(y-y2)/2)-3,x-(abs(x-x2)/2)+3, y+(abs(y-y2)/2)+3, fill=red, outline=red, tag='a')
        p.create_text(x-(abs(x-x2)/2), y+(abs(y-y2)/2)+15, text=w, fill="white", tag='a')

        #for i in range(2,10):
        #    p.create_oval(x-(abs(x-x2)/(dist/(65-(i*5))))-i, y+(abs(y-y2)/(dist/(65-(i*5))))-i,x-(abs(x-x2)/(dist/(65-(i*5))))+i, y+(abs(y-y2)/(dist/(65-(i*5))))+i, fill="white")

        p.create_oval(x-(abs(x-x2)/(dist/25))-8, y+(abs(y-y2)/(dist/25))-8,x-(abs(x-x2)/(dist/25))+8, y+(abs(y-y2)/(dist/25))+8, fill="white", outline="white", tag='a')
        p.create_oval(x-(abs(x-x2)/(dist/42))-6, y+(abs(y-y2)/(dist/42))-6,x-(abs(x-x2)/(dist/42))+6, y+(abs(y-y2)/(dist/42))+6, fill="#d7dadc", outline="#d7dadc", tag='a')
        p.create_oval(x-(abs(x-x2)/(dist/55))-3, y+(abs(y-y2)/(dist/55))-3,x-(abs(x-x2)/(dist/55))+3, y+(abs(y-y2)/(dist/55))+3, fill="#879196", outline="#879196", tag='a')
        p.create_oval(x-(abs(x-x2)/(dist/65))-2, y+(abs(y-y2)/(dist/65))-2,x-(abs(x-x2)/(dist/65))+2, y+(abs(y-y2)/(dist/65))+2, fill="#5e6c72", outline="#5e6c72", tag='a')
        
    if (x > x2 and y > y2):
        p.create_oval(x-(abs(x-x2)/2)-3, y-(abs(y-y2)/2)-3,x-(abs(x-x2)/2)+3, y-(abs(y-y2)/2)+3, fill=red, outline=red, tag='a')
        p.create_text(x-(abs(x-x2)/2), y-(abs(y-y2)/2)+15, text=w, fill="white", tag='a')

        #for i in range(2,10):
        #    p.create_oval(x-(abs(x-x2)/(dist/(65-(i*5))))-i, y-(abs(y-y2)/(dist/(65-(i*5))))-i,x-(abs(x-x2)/(dist/(65-(i*5))))+i, y-(abs(y-y2)/(dist/(65-(i*5))))+i, fill="white")

        p.create_oval(x-(abs(x-x2)/(dist/25))-8, y-(abs(y-y2)/(dist/25))-8,x-(abs(x-x2)/(dist/25))+8, y-(abs(y-y2)/(dist/25))+8, fill="white", outline="white", tag='a')
        p.create_oval(x-(abs(x-x2)/(dist/42))-6, y-(abs(y-y2)/(dist/42))-6,x-(abs(x-x2)/(dist/42))+6, y-(abs(y-y2)/(dist/42))+6, fill="#d7dadc", outline="#d7dadc", tag='a')
        p.create_oval(x-(abs(x-x2)/(dist/55))-3, y-(abs(y-y2)/(dist/55))-3,x-(abs(x-x2)/(dist/55))+3, y-(abs(y-y2)/(dist/55))+3, fill="#879196", outline="#879196", tag='a')
        p.create_oval(x-(abs(x-x2)/(dist/65))-2, y-(abs(y-y2)/(dist/65))-2,x-(abs(x-x2)/(dist/65))+2, y-(abs(y-y2)/(dist/65))+2, fill="#5e6c72", outline="#5e6c72", tag='a')
        
    if (x < x2 and y > y2):
        p.create_oval(x+(abs(x-x2)/2)-3, y-(abs(y-y2)/2)-3,x+(abs(x-x2)/2)+3, y-(abs(y-y2)/2)+3, fill=red, outline=red, tag='a')
        p.create_text(x+(abs(x-x2)/2), y-(abs(y-y2)/2)+15, text=w, fill="white", tag='a')

        #for i in range(2,10):
        #    p.create_oval(x+(abs(x-x2)/(dist/(65-(i*5))))-i, y-(abs(y-y2)/(dist/(65-(i*5))))-i,x+(abs(x-x2)/(dist/(65-(i*5))))+i, y-(abs(y-y2)/(dist/(65-(i*5))))+i, fill="white")

        p.create_oval(x+(abs(x-x2)/(dist/25))-8, y-(abs(y-y2)/(dist/25))-8,x+(abs(x-x2)/(dist/25))+8, y-(abs(y-y2)/(dist/25))+8, fill="white", outline="white", tag='a')
        p.create_oval(x+(abs(x-x2)/(dist/42))-6, y-(abs(y-y2)/(dist/42))-6,x+(abs(x-x2)/(dist/42))+6, y-(abs(y-y2)/(dist/42))+6, fill="#d7dadc", outline="#d7dadc", tag='a')
        p.create_oval(x+(abs(x-x2)/(dist/55))-3, y-(abs(y-y2)/(dist/55))-3,x+(abs(x-x2)/(dist/55))+3, y-(abs(y-y2)/(dist/55))+3, fill="#879196", outline="#879196", tag='a')
        p.create_oval(x+(abs(x-x2)/(dist/65))-2, y-(abs(y-y2)/(dist/65))-2,x+(abs(x-x2)/(dist/65))+2, y-(abs(y-y2)/(dist/65))+2, fill="#5e6c72", outline="#5e6c72", tag='a')

    #winsound.Beep(random.randint(400,3500),50)
    p.after(0)
    p.update()

path = []
file = open("C:/Users/danko/Desktop/Currency Exchange/cmake-build-debug/test.txt", 'r')
for i, line in enumerate(file):
    if i == 4:
        for i in range(len(line.split())):
            path.append(int(line.split()[i]))
    if i > 4:
        pole = line.split()
        addEdge(int(pole[0]), int(pole[1]), float(pole[2]))
file.close()

path = [1,5,3,13,15,6,10,16,14,18,18]
print(path)
count = -1
counter = 0
it = 0
if (isNegative == 0):
    for i in range(0, len(path)-1):
        src = path[i]
        dest = path[i+1]
        for i in array:
            if (i[2] == src):
                x = i[0]
                y = i[1]
            if (i[2] == dest):
                x2 = i[0]
                y2 = i[1]
        p.create_line(x, y, x2, y2, fill=red, width=1, tag='a')
        
        count += 1
        it += 32
        counter += 1
        p.create_text(120,150+it, text=path[count], font="Colbel 15", fill=red)
        dist = (pow(abs(x-x2),2)+pow(abs(y-y2),2))**(1/2)
        if (x < x2 and y < y2):
            p.create_text(x+(abs(x-x2)/2), y+(abs(y-y2)/2)-15, text=counter, font="Cursiva 15", fill=red, tag='a')


        if (x > x2 and y < y2):
            p.create_text(x-(abs(x-x2)/2), y+(abs(y-y2)/2)-15, text=counter, font="Cursiva 15", fill=red, tag='a')


        if (x > x2 and y > y2):
            p.create_text(x-(abs(x-x2)/2), y-(abs(y-y2)/2)-15, text=counter, font="Cursiva 15", fill=red, tag='a')

            
        if (x < x2 and y > y2):
            p.create_text(x+(abs(x-x2)/2), y-(abs(y-y2)/2)-15, text=counter, font="Cursiva 15", fill=red, tag='a')
        p.update()
        p.after(30)
else:
    # --------- NEGATIVE CYCLES --------- #    
    #cycle = [8,2,9,8] #cycles
    counter = 0
    for i in range(0, len(path)-1):
        src = path[i]
        dest = path[i+1]
        for i in array:
            if (i[2] == src):
                x = i[0]
                y = i[1]
            if (i[2] == dest):
                x2 = i[0]
                y2 = i[1]
        count += 1
        it += 32
        p.create_text(120,150+it, text=path[count], font="Colbel 15", fill="red2")
        p.create_line(x, y, x2, y2, fill="red", width=1, tag='a')
        p.update()
        p.after(30)
    # --------- NEGATIVE CYCLES --------- #  

z = 0
for i in array:
    x = i[0]
    y = i[1]
    t = i[2]
    z = i[3]
    p.create_oval(x-15-z, y-15-z, x+15+z, y+15+z, fill="white", outline="white", tag='a', activefill="#d7dadc", activeoutline="#d7dadc")
    if (t in path): # path of cycle
        p.create_text(x, y, text=t, font="Cursiva 15", fill="red2", tag='a') #8BC34A
    else:
        p.create_text(x, y, text=t, fill="black", font="Cursiva 15", tag='a') 

def up(sur):
    xm = sur.x
    ym = sur.y
    y = x = 5
    p.move('a', 0, -y)
    p.update()

def down(sur):
    xm = sur.x
    ym = sur.y
    y = x = 5
    p.move('a', 0, y)
    p.update()

def left(sur):
    xm = sur.x
    ym = sur.y
    y = x = 5
    p.move('a', -x, 0)
    p.update()

def right(sur):
    xm = sur.x
    ym = sur.y
    y = x = 5
    p.move('a', x, 0)
    p.update()

p.bind_all('<Left>', left)
p.bind_all('<Right>', right)
p.bind_all('<Up>', up)
p.bind_all('<Down>', down)

flying = "(1) AFN - Afghanistan Afghani   |   (2) ALL - Albania Lek   |   (3) BBD - Barbados Dollar   |  (4) BTN - Bhutan Ngultrum   |   (1) AFN - Afghanistan Afghani   |   (2) ALL - Albania Lek   |   (3) BBD - Barbados Dollar   |  (4) BTN - Bhutan Ngultrum   |   (1) AFN - Afghanistan Afghani   |   (2) ALL - Albania Lek   |   (3) BBD - Barbados Dollar   |  (4) BTN - Bhutan Ngultrum"
flying2 = "( 2 , 1 , 0.331824 )    ( 3 , 1 , 0.093751 )    ( 1 , 4 , -0.077711 )   ( 2 , 1 , 0.331824 )    ( 3 , 1 , 0.093751 )    ( 1 , 4 , -0.077711 )   ( 2 , 1 , 0.331824 )    ( 3 , 1 , 0.093751 )    ( 1 , 4 , -0.077711 )   ( 2 , 1 , 0.331824 )    ( 3 , 1 , 0.093751 )    ( 1 , 4 , -0.077711 )   ( 2 , 1 , 0.331824 )    ( 3 , 1 , 0.093751 )    ( 1 , 4 , -0.077711 )   ( 2 , 1 , 0.331824 )    ( 3 , 1 , 0.093751 )    ( 1 , 4 , -0.077711 )   ( 2 , 1 , 0.331824 )    ( 3 , 1 , 0.093751 )    ( 1 , 4 , -0.077711 )   ( 2 , 1 , 0.331824 )    ( 3 , 1 , 0.093751 )    ( 1 , 4 , -0.077711 )   ( 2 , 1 , 0.331824 )    ( 3 , 1 , 0.093751 )    ( 1 , 4 , -0.077711 )   ( 2 , 1 , 0.331824 )    ( 3 , 1 , 0.093751 )    ( 1 , 4 , -0.077711 )   ( 2 , 6 , 1.517350 )    ( 5 , 3 , -0.215516 )    ( 4 , 5 , 2.157920 )    ( 6 , 3 , 1.730333 )    ( 5 , 6 , 1.037656 )    ( 7 , 5 , 0.921438 )    ( 8 , 7 , 0.841551 )    ( 5 , 8 , 0.578654 )    ( 6 , 7 , 1.995139 )    ( 3 , 4 , 0.522299 )"
flying2 = "( 3 , 18 , -0.204531 )      ( 5 , 9 , 0.929389 )      ( 1 , 3 , 0.663992 )      ( 12 , 10 , -0.130614 )      ( 17 , 11 , -0.232718 )      ( 2 , 15 , 1.364882 )      ( 13 , 16 , 1.191162 )      ( 3 , 6 , -0.248395 )      ( 13 , 11 , 1.214079 )      ( 13 , 14 , 0.028495 )      ( 2 , 7 , 0.601971 )      ( 17 , 4 , -0.081446 )      ( 17 , 15 , -0.010924 )      ( 7 , 15 , 1.328527 )      ( 14 , 2 , 0.841278 )      ( 12 , 2 , -0.088522 )      ( 4 , 18 , -0.151249 )      ( 9 , 14 , 2.245525 )      ( 17 , 2 , 0.358598 )      ( 3 , 4 , 0.221123 )      ( 14 , 8 , 1.709502 )      ( 8 , 3 , 1.646786 )      ( 11 , 18 , 1.496541 )      ( 17 , 12 , -0.108880 )      ( 17 , 18 , 0.009228 )      ( 11 , 5 , -0.070808 )      ( 7 , 6 , -0.063645 )      ( 1 , 8 , 0.694335 )      ( 7 , 18 , 1.517144 )      ( 13 , 7 , 0.426663 )      ( 16 , 6 , 0.125757 )      ( 18 , 9 , 1.728869 )      ( 17 , 16 , -0.096345 )      ( 11 , 2 , 1.524283 )      ( 4 , 6 , -0.258758 )      ( 12 , 15 , -0.062272 )      ( 12 , 14 , 0.899914 )      ( 1 , 15 , 1.202911 )      ( 13 , 8 , -0.045434 )      ( 15 , 13 , 0.382764 )      ( 12 , 6 , 2.218663 )      ( 8 , 18 , 1.026656 )      ( 1 , 4 , 0.677969 )      ( 17 , 8 , -0.032018 )      ( 1 , 9 , 0.537380 )      ( 6 , 15 , 0.024453 )      ( 9 , 8 , 0.175075 )      ( 10 , 13 , 0.738043 )      ( 9 , 2 , 0.008579 )      ( 18 , 1 , 1.102703 )      ( 9 , 13 , 1.957641 )      ( 6 , 2 , -0.137289 )      ( 6 , 13 , 0.773506 )      ( 6 , 17 , 1.279805 )      ( 9 , 15 , 0.031758 )      ( 1 , 2 , 1.401184 )      ( 4 , 12 , 1.931505 )      ( 3 , 15 , 0.280457 )      ( 12 , 9 , 0.328050 )      ( 4 , 16 , 1.280922 )      ( 10 , 18 , 1.444925 )      ( 1 , 17 , 0.962589 )      ( 1 , 12 , 0.962348 )      ( 15 , 8 , 2.080863 )      ( 1 , 11 , 0.597741 )      ( 16 , 11 , 0.972368 )      ( 16 , 10 , -0.111675 )      ( 5 , 1 , 0.004760 )      ( 12 , 16 , 0.426496 )      ( 1 , 14 , 0.132143 )      ( 12 , 18 , 0.827070 )      ( 5 , 15 , 0.398004 )      ( 9 , 16 , 2.298162 )      ( 12 , 13 , 0.016370 )      ( 2 , 5 , 0.782525 )      ( 14 , 17 , 0.530441 )      ( 4 , 13 , 0.373493 )      ( 11 , 6 , 1.904711 )      ( 18 , 2 , -0.126834 )      ( 8 , 11 , 0.821172 )      ( 15 , 11 , 0.908569 )      ( 14 , 16 , -0.200811 )      ( 17 , 13 , 1.102160 )      ( 6 , 8 , 0.123894 )      ( 5 , 10 , 1.469149 )      ( 10 , 2 , 2.034777 )      ( 3 , 10 , -0.132676 )      ( 10 , 9 , 1.240074 )      ( 1 , 10 , 0.205271 )      ( 7 , 8 , 0.529201 )      ( 9 , 11 , 0.655436 )      ( 10 , 6 , -0.049195 )      ( 4 , 7 , -0.008736 )      ( 15 , 18 , 0.076882 )      ( 13 , 3 , -0.099040 )      ( 4 , 11 , 1.098934 )      ( 15 , 16 , 1.955825 )      ( 3 , 5 , 0.071661 )      ( 16 , 18 , 1.923756 )      ( 18 , 14 , 0.318613 )      ( 0 , 0 , 0.590708 )      ( 0 , 0 , 0.672910 )      ( 0 , 0 , 1.470938 )      ( 0 , 0 , 0.583508 )      ( 0 , 0 , 1.265491 )      ( 0 , 0 , 0.430322 )      ( 0 , 0 , -0.213730 )      ( 0 , 0 , 0.017609 )      ( 0 , 0 , 0.305492 )      ( 0 , 0 , -0.072555 )      ( 0 , 0 , 1.498787 )      ( 0 , 0 , -0.191410 )      ( 0 , 0 , -0.001329 )"

xsur = 0
f = p.create_text(xsur, 670, text=flying2, fill="white", font="Corbel 12")
while (1):
    if (xsur == 5000):
        xsur = 0
    xsur += 1
    p.delete(f)
    f = p.create_text(xsur, 670, text=flying2, fill="white", font="Corbel 12")
    p.after(1)
    p.update()



tkinter.mainloop()




