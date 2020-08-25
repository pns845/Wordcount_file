import sys
f=open(sys.argv[1],'r').readlines()
l=0
m={}
for i in f:
   d=i.strip()
   e=d.split(" ")
   for word in e:
      if word in m:
         m[word]=m[word]+1
      else:
         m[word]=0

  # l=l+len(e)
  # print("total no of words is:"+str(l))
for e in m:
   print("the word count in dict"+":"+str(e)+"-"+str(m[e]))
