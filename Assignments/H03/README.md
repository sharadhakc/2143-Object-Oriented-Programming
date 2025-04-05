## Homework - Inheritance in OOP
### Part A: Conceptual Questions
#### Definition:
Inheritance in OOP refers to the ability of a class to have a derived class which has its own unique properties and behavior but can also use the property of the base class. This allows for code reuseablity.
While inheritance uses a “is-a” relationship where a derived class is a specialized version of the base class, composition or aggregation uses a “has-a” relationship where one class contains another, but without necessarily extending it.
#### Types of Inheritance:
- Single Inheritance: when the derived class derives from only one base class. For example, lets say we have a class `Animal` that has a derived class `Dog`. The `Dog` inherits characteristics like eating and sleeping from `Animal` but also has it's own attributes like barking.
- Multiple Inheritance: when one derived class has serveral base classes. For example, `child` class inheriting from `parent1` and `parent2`. The `child` will have it's own properties but will also inherit from `parent1` and `parent2`.
 #### Overriding Methods
 Method overriding allows a derived class to provide its own implementation of a method that is already defined in the base class. This is useful when the base class method is not specific enough for the derived class, and you want to change or extend its behavior. For example, if a base class Vehicle has a method drive(), and a derived class Car wants to customize how it drives, it can override drive() to include details specific to a car.

You might override a method instead of adding a new one because it maintains the same method signature, ensuring consistency across the class hierarchy. This way, any code using the base class method can also work with the derived class method, without needing to change how the method is called.
#### Real World Analogy
A real-life analogy of inheritance can be seen in how children inherit traits from their parents. For example, children might inherit their parents' eye color, hair type, or height. While the parents have these traits, the child may inherit a mix of them or display something unique that reflects the combination of both parents' characteristics.

In terms of OOP, this is like a `Child` class inheriting attributes and behaviors (methods) from a `Parent` class. The child gets the properties and methods of the parent but can also have its own unique attributes or methods. The parent provides the basic structure (like eye color or height in the real-world example), and the child can customize or extend these characteristics. The concept of inheritance lets the child class reuse the functionality of the parent class without having to rewrite it from scratch.

### Part B: Minimal Coding
``` cpp
#include <iostream>
using namespace std;

class Vehicle {
private:
    string brand;

public:
    Vehicle(string b) : brand(b) {} // Constructor initializes the brand

    void drive() { 
        cout << "Driving a " << brand << endl;
    }
};

class Car : public Vehicle {
private:
    int doors;

public:
    Car(string b, int d) : Vehicle(b), doors(d) {} // Calls Vehicle constructor

    void drive() override { // Overrides the drive method
        cout << "Car is driving with " << doors << " doors." << endl;
    }
};

int main() {
    Vehicle v("Generic Brand"); // Creating a Vehicle object
    Car c("Toyota", 4);         // Creating a Car object

    v.drive();                  // Calls the drive method of Vehicle
    c.drive();                  // Calls the overridden drive method of Car

    return 0;
}

```
### Part C: Short Reflection & Discussion
#### When to use Inheritance
Inheritance allows the user to reuse the same code. So, if we have a class which has common attributes to a different class, we can use inheritance in that situation. It is easier as the we don't have to create the same methods for derived class from scratch and can just reuse the ones from the base class. Using inheritance where classes don’t share meaningful common behavior can lead to messy code. . For example, forcing a `User` class to inherit from `Vehicle` doesn’t make sense. Instead, composition would be a better fit in such cases.

### Method Overriding Vs Method Overloading
Overriding means redefining a parent class method in the child class with the same name and parameters. It happens at runtime and lets the child class change how things work.
Overloading means having multiple methods with the same name but different parameters in the same class. It happens at compile time.
Inheritance relies heavily on overriding for flexibility because overriding lets the child change or upgrade the behavior without starting over. That’s what gives control and makes inheritance useful—not just copying, but customizing.
### Inheritance vs. Interfaces/Abstract Classes
Inheritance gives a class the ability to inherit behavior and properties from a parent class. It defines an "is-a" relationship and enables code reuse.. You can reuse and override behavior directly.
Interfaces or abstract classes, on the other hand, don’t give full behavior. They just set rules or structure. You implement those rules in your own way.
So, inheritance gives you something ready to use and modify, while interfaces force you to build your own version following a blueprint.
### Pitfalls of Multiple Inheritance
One common problem with multiple inheritance is the diamond problem. If two parent classes have the same method, and a child class inherits from both, the compiler doesn’t know which version to use.
We fix the diamond problem with virtual inheritance. This means when a class inherits from two others, it only gets one copy of the shared features from the parent class. This removes the confusion because there’s no duplication.
