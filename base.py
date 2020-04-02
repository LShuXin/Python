class Animal:
    def run(self):
        print("animal is running");
class Dog(Animal):
    def run(self):
        print("dog is runing");
class Cat(Animal):
    def run(self):
        print("cat is running");
dog=Dog();
cat=Cat();
print(Dog.__base__);
print(Cat.__base__);





