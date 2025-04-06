# Part A: Conceptual Questions

### Definition

Abstraction in OOP is the concept of hiding complex details and only exposing the necessary parts of an object to the user. It's like providing a simple interface to interact with an object while keeping the internal workings hidden.

**Real-world analogy:**
Abstraction is like using a smartphone: you know pressing the screen to open an app or making a call, but you don’t need to understand how the phone’s operating system, hardware, or network works behind the scenes. You only interact with the essential features, and the complex details are hidden from you.

### Abstraction vs. Encapsulation

Abstraction is about hiding the complexity of the system by exposing only the necessary features. It allows you to focus on what an object can do, rather than how it does it. For example, when using a phone, you interact with the screen to open apps, but you don’t need to understand the software, hardware, or network process behind it.

Encapsulation, on the other hand, is about bundling the data and methods that operate on that data within a class and restricting access to some of the object’s internal state. You can’t directly access or modify the data inside a class unless through specific methods. It's like having a phone’s internal workings (battery, processor, etc.) hidden away so you can’t directly mess with them, but you can use buttons and touch gestures to control the phone.

While abstraction hides complexity, encapsulation protects data and limits how it's accessed. That's why people sometimes confuse them—they both simplify how we interact with things, but they do it in different ways.

#### Designing with Abstraction
For a smart thermostat, three essential attributes would be the `current temperature`, `target temperature`, and `mode`. For methods, I'd include `SetTemperature()`, allowing users to set their desired temperature, and `AdjustMode()`, which switches between heating, cooling, and off. These methods are what users would actually use to control the thermostat.
The user doesn’t need to know how the sensor measures the temperature, how the data is processed, or how the system switches between modes. They just care about the user-friendly methods, like adjusting the temperature or changing the mode, which keeps the interface simple and focused on the tasks at hand.. The user only needs to control the temperature settings, not the underlying hardware or software that is why you would **omit certain internal detail**.

#### Benefits of Abstraction 
- Abstraction makes it easier to add new features or make changes to the system.  When you modify the internals of a system, you don’t have to touch the code that interacts with the system at a higher level. This reduces the chances of breaking existing functionality.
- It also helps avoid code duplication because the abstracted parts of the system are reused instead of being rewritten in multiple places. This increases reusability because once you define a general behavior or interface, it can be applied across different parts of the system or in other projects, saving time and effort.

#### Minimal Class Example (Pseudo-code)
```cpp
class BankAccount {
public:
    virtual void deposit(double amount) = 0;  // Abstract method for deposit
    virtual void withdraw(double amount) = 0; // Abstract method for withdraw
    virtual double getBalance() const = 0;    // Abstract method to get balance
    virtual ~BankAccount() {}  // Virtual destructor for polymorphism
};

// Derived class SavingsAccount
class SavingsAccount : public BankAccount {
private:
    double balance;  // Hidden internal state

public:
    SavingsAccount(double initialBalance) : balance(initialBalance) {}

    void deposit(double amount) override {
        balance += amount;
        // Internal logic like logging can be hidden here
    }

```
### Part C: Reflection & Comparison
### Additional Exploration:
**Interfaces vs. Abstract Classes**

An interface defines a contract of methods that a class must implement but doesn’t provide any implementation itself, while an abstract class can provide both abstract methods (without implementation) and concrete methods (with implementation). In short, an interface is for defining "what" a class should do, while an abstract class can define "how" part of it should be done, along with leaving room for further implementation.

An interface would be more suitable than an abstract class when you need to define a common set of behaviors that multiple, unrelated classes must implement. For example, in a system where different types of objects (like a Bird, Car, and Robot) need to implement a Move() function, using an interface ensures that all these objects can be treated similarly while maintaining flexibility in their individual implementations.

**Testing Abstraction** 

To unit test abstract methods or classes, you can create a concrete subclass that provides basic implementations of the abstract methods. This allows you to instantiate the abstract class for testing purposes, making it easier to verify that the abstract methods behave as expected in a controlled, testable way. 

