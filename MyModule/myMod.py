def spaceRemove(str):
    str1=''
    for i in range(len(str)):
        if(str[i]==" "):
            str1+="_"
        else:
            str1+=str[i]
    return str1