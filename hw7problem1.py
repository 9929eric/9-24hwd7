class Person:

    def __init__(self, name):
        self.name = name
        self.age = 0
        self.friend_list = []

    def get_older(self):
        self.age += 1

    def about_me(self):
        return "Hello! I'm " + self.name + " and I'm " + str(self.age) + " years old."

    def make_friend(self, friend_name):
        self.friend_list.append(friend_name)


    def talk_about_friends(self):
        print(self.name,"'s friends: --------")

        if self.friend_list == []:
          print("I don't have any friends yet.")

        else:
          for friend in self.friend_list:
           print(friend,"is a friend of mine.")



# LEAVE THIS CODE AS IS ---------
person1 = Person('Dale')
person2 = Person('Stacey')


print(person1.about_me())
print(person2.about_me())
print()

person1.get_older()
print(person1.about_me())
person1.talk_about_friends()
person1.make_friend('Rita')
person1.make_friend('Sen')
person1.talk_about_friends()
person1.get_older()
print(person1.about_me())
print()


for i in range(10):
    person2.get_older()
print(person2.about_me())
person2.make_friend('Johanis')
person2.talk_about_friends()
print()
