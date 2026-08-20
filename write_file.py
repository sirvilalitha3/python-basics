

#with open('data.txt',"w") as file:

   # file.write("Name:S.lalitha","\nCourse:Datascience")
    #file.write("koi job dilado[crying emoji]")
f=open("sample.txt","w")
lines=["hello everyone\n","writing multiple strings\n","this is third line"]
f.writelines(lines)
f.close()
