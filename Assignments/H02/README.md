## Homework - Understanding Encapsulation
### Part A: Conceptual Questions
#### **Definition** 

Encapsulation means keeping the important data inside a class private so that it can’t be changed directly from outside. Instead, we control how the data is accessed and modified through specific methods. This helps keep the data safe and prevents accidental or incorrect changes. <br>

**Example:** In a university's student management system, a student’s GPA and personal details like their name, age, gpa, etc should be private. If these were public, anyone could change their GPA or access personal information. Instead, the system provides methods like getGPA() that only allow authorized users, like professors or administrators, to view the data. A method like updateGPA() would only allow changes under specific conditions, ensuring fairness and accuracy.

#### **Visibility Modifiers** 
- **Public:** Anyone can access it like the class itself, derived class, friends class and any external code or objects, making it easy to use and modify. This is less secure which means accidental changes and security risks are more likely.
- **Protected:** This is more secure than public but less secure than private. Allows derived classes to access certain data while keeping it hidden for the rest of the program.
- **Private:** Most secure as the data is only allowed access to the friend class. Can make the code less flexible since you always need getter and setter methods to access or modify data.

**When to use protected instead of private:** 

If there’s a `UniversityMember` class with a `universityID`, making it **private** means only that class can use it, so `Student` or `Professor` wouldn’t have access. But if it’s **protected**, those subclasses can still use it when needed like if a `Student` needs to check their enrollment or a `Professor` needs it for faculty records. This keeps the data hidden from the outside but still usable by related classes.

#### **Impact on Maintenance** 
Encapsulation makes debugging easier because it organizes code and keeps things neat. It hides the inner details of a class and only shows what other parts of the program actually need. This makes it simpler to track down problems since you can focus on the specific part of the code where the issue might be. It also prevents accidental changes to how things work inside the class, which helps avoid unexpected bugs. Overall, it keeps the code consistent and easier to fix when something goes wrong.
