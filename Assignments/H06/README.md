## Homework - Understanding Composition and Aggregation in OOP
### Part A: Conceptual Questions

 **Composition vs. Aggregation**

Composition and aggregation both describe relationships between objects, but they differ in how tightly the objects are linked. Composition means one object "owns" another, and if the parent is destroyed, so is the child. For example , lets take a car and its engine. The engine can’t exist without the car, so the car is responsible for the engine’s lifecycle. Aggregation is a more flexible relationship. A Library and Books is a good example as books can exist outside of the library, and the library doesn’t control the books’ lifespans.

**When to Use It**

Composition is best when one object depends entirely on the other, and its lifecycle is tied to it. For example, in a video game, a `Character` and its `Avatar` are in a composition relationship, because the avatar can’t exist without the character. Aggregation is better when one object can exist independently of the other. In a banking system, a `Customer` and their `Account` would have an aggregation relationship. The account can exist even if the customer is no longer involved with it, like when an account is closed.

**Differences from Inheritance**

Composition and aggregation are different from inheritance because they express "has-a" relationships, rather than "is-a" relationships. Inheritance creates a hierarchical structure, like a `Dog` being an `Animal`. Composition allows for more flexible designs because objects can change and adapt without relying on rigid class hierarchies. It’s often preferred because it lets you modify individual components without impacting the whole class structure, whereas inheritance can lead to tighter coupling and less flexibility.

**Real-World Analogy**

We could use the example of a room and a house. The rooms are part of the house, and without the house, the rooms wouldn't exist. That’s composition. A Driver and a Car is more like aggregation. The driver isn’t bound to a single car, and a car can have different drivers. These distinctions are important because they affect how objects are created, linked, and destroyed in code. Composition leads to tighter relationships and dependencies, while aggregation gives more flexibility for objects to exist independently.
#### Part 2: Minimal Coding Example

```cpp
// Composition: Address belongs to Person, doesn't exist alone.
class Address {
private:
    string street;
    string city;

public:
     Address(string str, string c) {
        street = str;
        city = c;
    }
};

class Person {
private:
    string name;
    Address address;  // Strong "has-a" relationship

public:
   public:
    Person(string n, string str, string c) : address("", "") {
        name = n;
        address = Address(str, c); 
    // When Person is destroyed, Address is too
};
```
## Part C: Reflection & Short Discussion

### Ownership & Lifecycle

In a composition relationship, the child object’s existence fully depends on the parent. If the parent is destroyed, the child gets deleted with it. For example, if a house is demolished, all the rooms inside it disappear too. The child can't exist on its own because it was never meant to live outside that context.

In contrast, with aggregation, the child object is more independent. Even if the parent is gone, the child can still exist. Like, a student might be part of a class, but even if the class ends, the student still exists somewhere else. The child object just happened to be referenced.

### Advantages & Pitfalls

One big advantage of using composition is that you have more control over how objects are created and destroyed. You know that when the parent object goes away, its components will too, which makes memory and lifecycle management easier.

If you use composition in a place where aggregation would be better, you might overcomplicate things. You could end up tightly coupling two objects that don’t need to be that connected, which makes your code harder to reuse and maintain later on.

### Contrast with Inheritance

“Has-a” relationships like composition or aggregation describe what something *contains*, while “is-a” relationships through inheritance describe what something *is*. For example, a car *has an* engine, but a car *is a* vehicle.

The problem with relying too much on inheritance is that it forces a rigid structure. You’re stuck following the parent class, even when you don’t need everything it gives you. That’s why people often prefer composition or aggregation. They’re more flexible and let you build around behavior instead of being locked into a family tree.
