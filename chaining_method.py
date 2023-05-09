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
        return self
        
    
    def enroll(self):
        if not self.is_rewards_member:
            self.is_rewards_member = True 
            self.gold_card_points = 200
            print(f"Congratulations {self.first_name} you are now enrolled")
        else:
            print(f"{self.first_name} is already enrolled in our Gold Card program")
        return self
        
    def spend_points(self,amount):
        if amount < self.gold_card_points:
            self.gold_card_points -= amount
        else:
            print(f"{self.first_name} Sorry you tried to redeem more Gold Card points than you have")
        return self
        
        

patient1 = User("Mindi", "Garcia", "mgarcia@gmail.com", 37)
patient2 = User("Peter", "Smith", "psmit@yahoo.com", 42)
patient3 = User("Tim", "Burton", "imakeweirdstuff.com",64)
patient4 = User("Jenna", "Ortega", "imthenewBurtonmuse.com",20)

patient1.display_info().enroll().spend_points(50).display_info()
patient2.display_info().enroll().spend_points(80).display_info()
patient3.display_info().enroll().spend_points(40).display_info()
patient4.display_info().enroll().spend_points(201).display_info()
