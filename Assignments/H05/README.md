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



