class_a = ["Jan", "Nick", "Maria", "Peter"]
class_b = ["Klara", "Jonas", "Hans", "Vladimir"]

#to print out all objects in both lists do not:
#for student in class_a:
#    print(student)    
#for student in class_b:
#    print(student)     
#but:
   
for student in class_b:
    class_a.append(student)

print(class_a)
    
