
# Polymorphism in C++: Homework

### Part A: Conceptual Questions

#### Definition
Polymorphism in C++ means that one function or method can behave differently depending on the type of object calling it. It’s a core feature of OOP because it makes our code flexible—allowing us to work with different objects in the same way, but still allowing them to do different things.  

Polymorphism is considered one of the pillars of OOP because it promotes code reuse and makes code easier to maintain and extend. Instead of writing specific code for every type of object, we can rely on polymorphism to handle the differences.

#### Compile-Time vs. Runtime

- **Compile-time polymorphism (method overloading)**: This happens when the method is resolved at compile time, based on the arguments passed in (like using different parameter types).
  
- **Runtime polymorphism (method overriding)**: This happens when the method is resolved at runtime, based on the object type, not the reference type.

**Which type requires inheritance?**  
- Runtime polymorphism requires inheritance because it involves a base class and derived classes where methods in derived classes can override base class methods.

#### Method Overloading

We overload methods when we want the same method name to handle different kinds of input. For example, `calculate()` could accept different types like `(int, int)` or `(double, double)`. This lets the user use the same method name without confusion.

**Example**:  
Imagine a `Calculator` class with a `calculate()` method. One version accepts integers, another accepts floating-point numbers. This allows you to call `calculate()` regardless of the type of data, simplifying user interactions with the class.

#### Method Overriding

Overriding happens when a derived class provides a specific implementation for a method defined in its base class. In C++, we use the `virtual` keyword in the base class to allow the method to be overridden.

The reason we use `virtual` is that we want the C++ runtime to choose which version of the method to call based on the object type, not the reference type.

#### Method Overriding

Overriding happens when a derived class provides a specific implementation for a method defined in its base class. In C++, we use the `virtual` keyword in the base class to allow the method to be overridden.

The reason we use `virtual` is that we want the C++ runtime to choose which version of the method to call based on the object type, not the reference type.

### Part B: Minimal Demonstration

**Option 1: Minimal Code (No More Than 20 Lines)**

```cpp
#include <iostream>
using namespace std;

class Shape {
public:
    virtual void draw() = 0;  // Pure virtual function
};

class Circle : public Shape {
public:
    void draw() override {
        cout << "Drawing Circle" << endl;
    }
};

class Rectangle : public Shape {
public:
    void draw() override {
        cout << "Drawing Rectangle" << endl;
    }
};

int main() {
    Shape* shapes[2];  // Array of Shape pointers
    shapes[0] = new Circle();
    shapes[1] = new Rectangle();

    for (int i = 0; i < 2; ++i) {
        shapes[i]->draw();  // Calls the correct draw method at runtime
    }

    return 0;
}
```
**Explanation:**
Here, we have an abstract class Shape with a pure virtual method draw(). The derived classes Circle and Rectangle each override the draw() method. We create an array of Shape* references and point them to a Circle and a Rectangle. When we call draw(), the correct method is chosen based on the actual object type, not the reference type. This decision happens at runtime.
### Part C: Overloading vs. Overriding Distinctions

#### Overloaded Methods

In method overloading, C++ uses compile-time resolution to decide which method to call. This happens based on the number and types of parameters passed to the method. For example:

```cpp
class Calculator {
public:
    int calculate(int a, int b) {
        return a + b;
    }

    double calculate(double a, double b) {
        return a + b;
    }
};
```
In the above example, the calculate() method is overloaded. If you pass integers, the first method is called; if you pass doubles, the second method is called. The C++ compiler resolves this at compile time based on the argument types you provide.
#### Overridden Methods
In method overriding, C++ resolves which method to call at runtime based on the type of the object. For example:

```cpp
class Shape {
public:
    virtual void draw() {
        std::cout << "Drawing Shape" << std::endl;
    }
};

class Circle : public Shape {
public:
    void draw() override {
        std::cout << "Drawing Circle" << std::endl;
    }
};

int main() {
    Shape* shape = new Circle();
    shape->draw();  // Calls Circle's draw() at runtime
}
```
Here, although shape is a pointer of type 8Shape*, the correct draw() method for Circle is called, because the actual object type is Circle. This is determined at runtime and is a key part of runtime polymorphism.

### Part D: Reflection & Real-World Applications
#### Practical Example
Imagine you’re developing a simulation game where different types of vehicles (e.g., Car, Truck, Motorcycle) need to have a `move()` function. You can define a Vehicle base class with a virtual `move()` function, and then have each derived class (Car, Truck, Motorcycle) implement its own version of `move()`. This reduces code duplication, makes it easier to add new vehicle types, and keeps the code scalable and maintainable. The correct move() method is called at runtime based on the actual object type, simplifying the game logic.

#### Potential Pitfalls
**Method Overloading:** One potential pitfall is that if method overloads aren't carefully designed, it can lead to ambiguity or confusion about which method gets called. For example, if you have two overloaded methods where the parameter types are too similar (e.g., int and float), it could cause issues where it's unclear which method should be invoked.

**Runtime Polymorphism:** A potential pitfall of runtime polymorphism is performance issues. The method that is called is decided at runtime, which can add overhead. Additionally, debugging can become more difficult because it might not be obvious which method is being called, especially in complex hierarchies or with pointers.

#### Checking Understanding
Polymorphism allows you to add a new Triangle class without touching the existing code that uses Shape* references. Since draw() is a virtual method, C++ will automatically call the correct draw() method based on the actual object type, whether it's a Circle, Rectangle, or Triangle. So, the code remains flexible and doesn’t need to change whenever you add a new shape—polymorphism handles the method call at runtime.
