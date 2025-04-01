## Homework - Understanding Encapsulation
### Part A: Conceptual Questions
#### **Definition** 

Encapsulation means keeping the important data inside a class private so that it can’t be changed directly from outside. Instead, we control how the data is accessed and modified through specific methods. This helps keep the data safe and prevents accidental or incorrect changes. <br>

**Example:** In a university's student management system, a student’s GPA and personal details like their name, age, gpa, etc should be private. If these were public, anyone could change their GPA or access personal information. Instead, the system provides methods like `getGPA()` that only allow authorized users, like professors or administrators, to view the data. A method like `updateGPA()` would only allow changes under specific conditions, ensuring fairness and accuracy.

#### **Visibility Modifiers** 
- **Public:** Anyone can access it like the class itself, derived class, friends class and any external code or objects, making it easy to use and modify. This is less secure which means accidental changes and security risks are more likely.
- **Protected:** This is more secure than public but less secure than private. Allows derived classes to access certain data while keeping it hidden for the rest of the program.
- **Private:** Most secure as the data is only allowed access to the friend class. Can make the code less flexible since you always need getter and setter methods to access or modify data.

**When to use protected instead of private:** 

If there’s a `UniversityMember` class with a `universityID`, making it **private** means only that class can use it, so `Student` or `Professor` wouldn’t have access. But if it’s **protected**, those subclasses can still use it when needed like if a `Student` needs to check their enrollment or a `Professor` needs it for faculty records. This keeps the data hidden from the outside but still usable by related classes.

#### **Impact on Maintenance** 
Encapsulation makes debugging easier because it organizes code and keeps things neat. It hides the inner details of a class and only shows what other parts of the program actually need. This makes it simpler to track down problems since you can focus on the specific part of the code where the issue might be. It also prevents accidental changes to how things work inside the class, which helps avoid unexpected bugs. Overall, it keeps the code consistent and easier to fix when something goes wrong.

#### **Real World Analogy**
A university’s grading system is a good example of encapsulation. Students can log into their portal to see their grades, schedules, and tuition balance—this is the **public interface**. But the actual system that stores grades, calculates GPAs, and manages payments is hidden in the **private implementation**. Students can’t change their grades themselves because that data is protected. If the backend was open to everyone, people could edit their own records, which would mess up the system. Keeping the private side hidden makes sure everything stays accurate and secure.


### Part B:  Small-Class Design (Minimal Coding)
```cpp
class BankAccount {
private:
    double balance;
    int accountNumber;

public:
    BankAccount(int accNum, double initialBalance) {
        accountNumber = accNum;
        balance = initialBalance;
        }

    void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
        }
    }

    double getBalance() const {
        return balance;
    }
};
```
The `balance` and `accountNumber` are private because they are personal information and should not be accessed outside the class. The `deposit()` method makes sure only positive amounts are added, and the `withdraw()` method checks if there’s enough money before letting you take any out. These methods keep the account info legit and error-free.

The `balance` variable is private, while public methods handle modifications. This setup makes it clear that balance shouldn't be changed directly. I’d also add comments, but just placing the variable in the private section already signals to other developers that it must be modified through the provided methods.

### **Part C: Reflection & Short-Answer**
#### Pros and Cons
Pros
- Prevents accidental changes by allwoing access to limited data and having controlled methods to modify them, reducing risks
- Makes debugging easier as the code is neat making it easier to track down errors
Cons
- Extra coding as we have to create various mathods to access and modify the data 

#### Encapsulation vs. Other Concepts
Encapsulation is about keeping data safe by making sure it can only be changed in controlled ways. Abstraction is more about keeping things simple and not showing unnecessary details. Both are forms of information hiding because they limit what people can see and mess with. Encapsulation locks data behind methods so no one can change it directly, and abstraction hides all the extra stuff so users only see what they need.

#### Testing Encapsulated Classes
We can ensure valid testing using methods. We can create methods to access the private data, modify it or check if the data is correct.





