# WAP to generate the given sequence of alphabets using for loop.
# A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,
# z,y,x,w,v,u,t,s,r,q,p,o,n,m,l,k,j,i,h,g,f,e,d,c,b,a,


for i in range(65, 91):
    print(chr(i), end=",")

print()

for i in range(122, 96, -1):
    print(chr(i), end=",")
