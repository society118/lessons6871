a=" ";b=" ";c=" "
d=" ";e=" ";f=" "
g=" ";h=" ";i=" "
x=1
while x<=9:
  print("\n",a,"|",b,"|",c,"\n---------\n",d,"|",e,"|",f,"\n---------\n",g,"|",h,"|",i)
  if x%2==1:
    p=input("Ваш хід (X), виберіть позицію (a-i): ")
    if p=="a" and a==" ": a="X"
    elif p=="b" and b==" ": b="X"
    elif p=="c" and c==" ": c="X"
    elif p=="d" and d==" ": d="X"
    elif p=="e" and e==" ": e="X"
    elif p=="f" and f==" ": f="X"
    elif p=="g" and g==" ": g="X"
    elif p=="h" and h==" ": h="X"
    elif p=="i" and i==" ": i="X"
    else: print("Спробуйте ще раз"); continue
  else:
    print("Хід комп'ютера (O):")
    if a==" ": a="O"
    elif b==" ": b="O"
    elif c==" ": c="O"
    elif d==" ": d="O"
    elif e==" ": e="O"
    elif f==" ": f="O"
    elif g==" ": g="O"
    elif h==" ": h="O"
    elif i==" ": i="O"
  if (a==b==c!=" ")or(d==e==f!=" ")or(g==h==i!=" ")or(a==d==g!=" ")or(b==e==h!=" ")or(c==f==i!=" ")or(a==e==i!=" ")or(c==e==g!=" "):
    print("\n",a,"|",b,"|",c,"\n---------\n",d,"|",e,"|",f,"\n---------\n",g,"|",h,"|",i)
    if x%2==1: print("Ви перемогли!")
    else: print("Комп'ютер переміг!")
    break
  x=x+1
if x==10:
  print("\nНічия!")
