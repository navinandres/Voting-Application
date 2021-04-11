
"""********************KONGU ENGINEERING COLLEGE-CSE C**************************"""

nominee_1=input("Enter the Nominee 1 Name:")
nominee_2=input("Enter the Nominee 2 Name:")

nominee_1_votes=0
nominee_2_votes=0

voters_id=[]
for i in range(121,180):
    voters_id.append(i)


num_of_votors=len(voters_id)

while True:
    
    if voters_id==[]:
        print("***************Voting has been Completed!!!*****************")
        if nominee_1_votes>nominee_2_votes:
            print("{} has WON".format(nominee_1))
            percent=(nominee_1_votes/num_of_votors)*100
            print("Votes WON by",percent,"%")
            
        elif nominee_1_votes<nominee_2_votes:
            print("{} has WON".format(nominee_2))
            percent=(nominee_2_votes/num_of_votors)*100
            print("Votes WON by",percent,"%")
        break    
    
    
    else:
        
      votor=int(input("Enter your Roll No:"))
      if votor in voters_id:
        print("You are Eligible to Vote!!!")
        voters_id.remove(votor)
        vote=int(input("Enter your Vote 1 {} or 2 {}:".format(nominee_1,nominee_2)))
        if vote==1:
            nominee_1_votes+=1 
        elif vote==2:
            nominee_1_votes+=1 
        print("Thank You for Casting your Valuable Vote!!!")
      else:
        print("You are not in the Votor List Currently//You have already Voted")

