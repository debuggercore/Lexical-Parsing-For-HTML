import re
tags=["html","head","title","body","table","form","frames","ol","li","ul","th","tr"
      ,"td","a","img","div" , "p" ,"tr" , "input","link" ,"script","h1"]
settags={}

for i in tags:
    settags[i]=set(i)
#print(settags)
attributes=["bgcolor","background","href","font"]

symbols=["<",">","/>"]
lineno=0
symboltable1=[]
symboltable2=[]
symboltable3=[]
symboltable4=[]
errortable=[]
f=open('main.html','r')

f1=open('output.txt' ,'w')

f2=open('Closingtag.txt' , 'w')
f3=open('ClosingOpeningtag.txt' , 'w')
f4=open('Openingtag.txt' , 'w')
f5=open('Attribute.txt' , 'w')
f6=open('Error.txt' , 'w')


#lines=f.readlines()
def tag(s):
    global symboltable
    ct=0
    
    #s=re.sub(r'\s+',r' ',s)
    
    match = re.findall(r'<.*?>', s,re.I)
    #i=re.sub(r'  ',r' ',s)
    for i in match:
        i=i[1:len(i)-1]
        if (i[len(i)-1]=='/'):
        	  ct=2	
        t=re.findall("\w+=['\"].*?['\"]",i)
        i=i.split(" ")
        tagname=i[0]
        if tagname[0]=='/':
            tagname=tagname[1:]
            ct=1
        if tagname in tags:
            #print(lineno,tagname)
            if(ct==1):
                symboltable1.append([tagname,"tag","ct",lineno])
                ct=0
            elif (ct==2):
            	 symboltable2.append([tagname,"tag","ct/ot",lineno])
            	 ct=0
            else:
                symboltable3.append([tagname,"tag","ot",lineno])
            #print(lineno,tagname)
           # print(i[1:])
            if t:
            	getattributes(tagname,t,lineno)
        else:
            settagname=set(tagname)
            findmax(tagname,settagname)
            
    #print(type(match))

    
   # value=re.findall(r'<.>)

    
def getattributes(tagname,l,lineno):
    
    global symboltable
    for i in l:
        i=i.split("=")
        #print(i)
        symboltable4.append([i[0],"att",i[1],tagname,lineno])
       # print("Att ",i[0],"value",i[1])

def findmax(tagname,settagname):
   # print("Inside error",tagname,settagname)
    global symboltable
    maxlen=0
    maxtag=""
    for k in settags.keys():
        a=settagname&settags[k]
        if len(a)>maxlen:
            maxlen=len(a)
            maxtag=k
    errortable.append([maxtag,"tag",lineno,"Error=",tagname])
    print("Error",maxtag)
    
    
  
#def
#print(type(lines))
#lines=re.sub(r'<!--.*?>',r'',lines)
#print("File\n",lines)

flag=0 
for line in f:
    #print("ori File\n",line)
    
    
    line=re.sub(r'<!--.*?-->',r'',line)
    match=re.match(r'\s*<!--.*?',line)
    if(match):
        flag=1
    
    match=re.match(r'.*?-->',line)
    if(match):
        flag=0
        line=re.sub(r'.*-->?',r'',line)
    if(flag):
        #flag=1
        line=re.sub(r'.*',r'',line)
    #print("File\n",line)
    #print(line)
    line=re.sub(r'\s+' , r' ',line)
    if(re.fullmatch(r'\s+',line)==None):
    	f1.write(line)
    	tag(line)
    lineno+=1


f2.write("---Closing tag Symbol table---\n")
for st in symboltable1:    
    f2.write(str(st)+"\n")   
    
f3.write("---Closing/Opening tag Symbol table---\n")
for st in symboltable2:    
    f3.write(str(st)+"\n")   
    
f4.write("---Opening tag Symbol table---\n")
for st in symboltable3:    
    f4.write(str(st)+"\n")   
    
    
f5.write("---Attribute Symbol table---\n")
for st in symboltable4:    
    f5.write(str(st)+"\n")   
    
f6.write("---Error table---\n")
for st in errortable:    
    f6.write(str(st)+"\n") 
f.close()
f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
f6.close()
