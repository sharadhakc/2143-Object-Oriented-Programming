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
