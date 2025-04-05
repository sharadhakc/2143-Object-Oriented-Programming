# Part A: Conceptual Questions

### Definition

**What is abstraction in OOP?**
Abstraction in OOP is the concept of hiding complex details and only exposing the necessary parts of an object to the user. It's like providing a simple interface to interact with an object while keeping the internal workings hidden.

**Real-world analogy:**
Think of a car's dashboard. You interact with the steering wheel, pedals, and buttons to drive. You don't need to know about the engine or how the transmission works. The dashboard abstracts those complex details and gives you only what you need to operate the car.

### Abstraction vs. Encapsulation

**Comparison:**
Abstraction hides the complexity of an object by exposing only the essential features, while encapsulation is about bundling the data (attributes) and methods (functions) that operate on the data into a single unit, and restricting access to some of the object’s components.

**Why might someone confuse the two?**
Both deal with hiding details, but abstraction focuses on *what* an object can do and encapsulation deals with *how* the object does it. So, both can seem like they're about hiding information, but they tackle different aspects.

### Designing with Abstraction

**Smart Thermostat Attributes:**
1. **Current Temperature**
2. **Target Temperature**
3. **Mode (Heating or Cooling)**

**Smart Thermostat Methods:**
1. **Set Temperature**
2. **Turn On/Off**

**Why omit certain details?**
You would omit internal details like circuit design and firmware because they aren’t relevant to the user’s interaction with the thermostat. The user only needs to control the temperature settings, not the underlying hardware or software.

### Benefits of Abstraction

**Two benefits:**
1. **Simplifies the system interface** by providing a clear way to interact with objects.
2. **Improves maintainability** because changes in internal implementation don’t affect how the user interacts with the object.

**How does abstraction reduce code complexity?**
Abstraction reduces complexity by allowing you to focus on essential features and hiding unnecessary details, making code easier to understand and maintain.

---

# Part B: Minimal Class Example (Pseudo-code)

**Scenario:** Model a Banking System where you only want certain core operations exposed (like deposit and withdraw), hiding internal complexities (like encryption, logging, or ledger balancing).

```cpp
// Abstract class defining the interface
class BankAccount {
public:
    virtual void deposit(double amount) = 0;
    virtual void withdraw(double amount) = 0;
    virtual double getBalance() const = 0;
    virtual ~BankAccount() = default;
};

// Derived class implementing the abstract methods
class SavingsAccount : public BankAccount {
private:
    double balance;
public:
    SavingsAccount(double initial_balance) : balance(initial_balance) {}
    
    void deposit(double amount) override {
        balance += amount;
    }

    void withdraw(double amount) override {
        if (amount <= balance) {
            balance -= amount;
        }
    }

    double getBalance() const override {
        return balance;
    }
};

