
# **Polymorphism in C++: Homework**

### **Part A: Conceptual Questions**

#### **Definition**
Polymorphism in C++ means that one function or method can behave differently depending on the type of object calling it. It’s a core feature of OOP because it makes our code flexible—allowing us to work with different objects in the same way, but still allowing them to do different things.  

Polymorphism is considered one of the pillars of OOP because it promotes code reuse and makes code easier to maintain and extend. Instead of writing specific code for every type of object, we can rely on polymorphism to handle the differences.

#### **Compile-Time vs. Runtime**

- **Compile-time polymorphism (method overloading)**: This happens when the method is resolved at compile time, based on the arguments passed in (like using different parameter types).
  
- **Runtime polymorphism (method overriding)**: This happens when the method is resolved at runtime, based on the object type, not the reference type.

**Which type requires inheritance?**  
- **Runtime polymorphism** requires inheritance because it involves a base class and derived classes where methods in derived classes can override base class methods.

#### **Method Overloading**

We overload methods when we want the same method name to handle different kinds of input. For example, `calculate()` could accept different types like `(int, int)` or `(double, double)`. This lets the user use the same method name without confusion.

**Example**:  
Imagine a `Calculator` class with a `calculate()` method. One version accepts integers, another accepts floating-point numbers. This allows you to call `calculate()` regardless of the type of data, simplifying user interactions with the class.

#### **Method Overriding**

Overriding happens when a derived class provides a specific implementation for a method defined in its base class. In C++, we use the `virtual` keyword in the base class to allow the method to be overridden.

The reason we use `virtual` is that we want the C++ runtime to choose which version of the method to call based on the object type, not the reference type.

### **Part B: Minimal Demonstration (Pseudo-code or UML)**

**Option**
