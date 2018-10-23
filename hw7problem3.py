import random
class Person:


    def __init__(self, name):
        self.name = name
        self.age = 0
        self.friend_list = []
        self.height = random.randint(175,215)/10

    def get_older(self):
        self.age += 1
        self.height += 6


    def about_me(self):
        return "Hello! I'm " + self.name + " and I'm " + str(self.age) + " years old and " + str(self.height) + " inches tall. I can walk " + str(int(self.height*self.height)) + " yards at a time!"

    def make_friend(self, friend_name):
        self.friend_list.append(friend_name)


    def talk_about_friends(self):
        print(self.name,"'s friends: --------")
        for friend in self.friend_list:
           print(friend,"is a friend of mine.")



# LEAVE THIS CODE AS IS ---------
person1 = Person('Dale')
person2 = Person('Stacey')
person3 = Person('Louis')
people_list = [person1, person2, person3]

print(person1.about_me())
print(person2.about_me())
print(person3.about_me())
print()



for person in people_list:
  for i in range(10):
    person.get_older()


print(person1.about_me())
person1.make_friend('Rita')
person1.make_friend('Sen')
person1.talk_about_friends()
print()

print(person2.about_me())
person2.make_friend('Johanis')
person2.talk_about_friends()
print()

print(person3.about_me())
person3.make_friend('Marco')
person3.talk_about_friends()
print()
