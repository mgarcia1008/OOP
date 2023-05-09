class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    
    def display_info(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Reward Member: {self.is_rewards_member}")
        print(f"Gold Card Points: {self.gold_card_points}")
        print("================================")
    
    def enroll(self):
        if not self.is_rewards_member:
            self.is_rewards_member = True 
            self.gold_card_points = 200
            print(f"Congratulations {self.first_name} you are now enrolled")
        else:
            print(f"{self.first_name} is already enrolled in our Gold Card program")
            print("======================")
        
    def spend_points(self,amount):
        if amount < self.gold_card_points:
            self.gold_card_points -= amount
        else:
            print(f"{self.first_name} Sorry you tried to redeem more Gold Card points than you have")
        print("========================")
        

patient1 = User("Mindi", "Garcia", "mgarcia@gmail.com", 37)
patient2 = User("Peter", "Smith", "psmit@yahoo.com", 42)
patient3 = User("Tim", "Burton", "imakeweirdstuff.com",64)
patient4 = User("Jenna", "Ortega", "imthenewBurtonmuse.com",20)

patient1.display_info() #prints out all user details on separate lines via method on line 9
patient2.display_info()
patient3.display_info()
patient4.display_info()

patient2.enroll()
patient2.display_info()

patient2.enroll() #bonus on second user of trying to re-enroll instead of first user
patient1.enroll() #enroll for spend points method
patient3.enroll() #enroll for bonus 
patient4.enroll()#enroll for bonus

patient1.spend_points(50)
patient2.spend_points(80)
patient3.spend_points(40)
patient4.spend_points(201)
print(patient1.gold_card_points)
print(patient2.gold_card_points)
print(patient3.gold_card_points)
print(patient4.gold_card_points)