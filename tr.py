import random
hanga = [ '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


w=['apple','banana','grapes']
a=random.choice(w)
print(a)
display=[]
m=6
k=len(a)
end="f"

for s in range(0,k):

    display+="_"

while end=="f":
    b=input("guess a letter").lower()







    for s in range(0,k):
        if b==a[s]:
            display[s]=b
    if b not in a:
        m-=1
        print(hanga[m])
    if m==0:
        end="t"
        print("you lose")
    print(display)
    if '_' not in display:
        
        end="t"
        print("you win")
    
        

         
print(display)




        

        
    

    
        
        
        







       
    
    