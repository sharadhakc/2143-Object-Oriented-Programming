## Homework - Understanding Encapsulation
### Part A: Conceptual Questions
#### **Definition** 

Encapsulation means keeping the important data inside a class private so that it can’t be changed directly from outside. Instead, we control how the data is accessed and modified through specific methods. This helps keep the data safe and prevents accidental or incorrect changes. <br>

**Example:** In a university's student management system, a student’s GPA and personal details like their name, age, gpa, etc should be private. If these were public, anyone could change their GPA or access personal information. Instead, the system provides methods like getGPA() that only allow authorized users, like professors or administrators, to view the data. A method like updateGPA() would only allow changes under specific conditions, ensuring fairness and accuracy.

#### **Visibility Modifiers** 
- **Public:** Anyone can access it like the class itself, derived class, friends class and any external code or objects, making it easy to use and modify. This is less secure which means accidental changes and security risks are more likely.
- **Protected:** This is more secure than public but less secure than private. Allows derived classes to access certain data while keeping it hidden for the rest of the program.
- **Private:** Most secure as the data is only allowed access to the friend class. Can make the code less flexible since you always need getter and setter methods to access or modify data.

   
