## Homework - Classes & Objects

### Part A: Conceptual Questions

#### **Definition of a Class and an Object**

**What is a class in object-oriented programming?**  
A class is a blueprint that defines attributes (data) and behaviors (methods) for objects. It provides structure and reusability in programming.

**What is an object, and how does it relate to a class?**  
An object is an instance of a class with its own attribute values and can perform class-defined actions. It represents real-world entities in a program.

#### **Constructors and Destructors**

**Define a constructor. What is its role in a class?**  
A constructor is a special function that initializes an object when it is created. It sets initial values for attributes and ensures proper object setup.

**Define a destructor. Why is it important in managing an object’s lifecycle?**  
A destructor is a function that gets called when an object is destroyed. It releases resources like memory or file handles to prevent memory leaks.

#### **Object Lifecycle**

**Briefly describe the lifecycle of an object from instantiation to destruction.**

- **Creation:** The constructor initializes the object, setting up its attributes.
- **Usage:** The object performs its tasks by calling methods and modifying attributes.
- **Destruction:** The destructor is called to clean up resources before the object is removed from memory.

**Why is it important for a class to manage its resources (e.g., memory) during its lifecycle?**  
Poor memory management can cause memory leaks, slow performance, crashes, and inefficient use of system resources.

---

### Part B: Minimal Coding Example

#### **C++ Code Implementation**

```cpp
#include <iostream>
using namespace std;

class Creature {
private:
    string name;
public:
    Creature(string creatureName) : name(creatureName) {
        cout << "Creature " << name << " has been created!\n";
    }
    
    void display() {
        cout << "Creature name: " << name << endl;
    }
    
    ~Creature() {
        cout << "Creature " << name << " is being destroyed!\n";
    }
};

int main() {
    Creature goblin("Goblin");
    goblin.display();
    return 0;
}
```

#### **Explanation**

- **The constructor initializes the creature’s name when an object is created.**
- **The `display` method prints the creature’s name.**
- **The destructor is called when the object goes out of scope, signaling its removal from memory.**
- **When `goblin` is created, the constructor runs automatically. Once `main()` ends, `goblin` is destroyed, and the destructor is triggered.**

---

### Part C: Reflection & Short-Answer

**Importance of Constructors:**  
They ensure objects start with valid data, preventing uninitialized variables and ensuring proper setup.

**Role of Destructors:**  
They free resources and prevent memory leaks, especially important in languages without automatic garbage collection.

**Lifecycle Management:**  
If a class does not properly manage its resources, it can lead to memory leaks, inefficient resource use, and system crashes.

---


