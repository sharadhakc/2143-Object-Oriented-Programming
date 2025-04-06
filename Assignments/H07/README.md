## Homework - Basic Design Principles in Software Development

### Part A: Conceptual Questions

#### DRY (Don’t Repeat Yourself)

DRY emphasizes the idea that every piece of knowledge should only be represented once within a system. If you find yourself duplicating code, you're violating this principle. For example, if you have two functions, `calculateSalary()` and `calculateBonus()`, which both contain logic for calculating an employee's pay based on the same data, you’re repeating yourself unnecessarily.

To adhere to DRY, you would refactor the code to extract the common logic into a shared method, say `calculatePay()`, which could be used by both `calculateSalary()` and `calculateBonus()`. This reduces duplication and makes your code cleaner and easier to maintain.

#### KISS (Keep It Simple, Stupid)

KISS is a reminder to avoid unnecessary complexity in your code. The goal is to keep your logic straightforward and easy to understand so that future changes or debugging can be done quickly and efficiently. For example, if you’re writing a method that checks for user eligibility for a discount, instead of using a complex chain of conditional checks, you could simplify the logic by breaking it down into smaller, clearer pieces.

However, oversimplifying can sometimes be problematic. For instance, if you strip away too much complexity in an effort to follow KISS, you might end up with code that lacks flexibility or doesn't handle edge cases, making it harder to scale or adapt to new requirements.

#### Introduction to SOLID (High-Level)

The SOLID principles help make software more maintainable, scalable, and adaptable. Here’s a quick breakdown:

1. **Single Responsibility Principle (SRP)**: A class should only have one reason to change, meaning it should only be responsible for one thing.
2. **Open-Closed Principle (OCP)**: Software entities (like classes or modules) should be open for extension but closed for modification.

The SOLID principles are important because they promote a clean, modular design that makes it easier to manage and extend large codebases. By adhering to these principles, you can avoid messy, tightly-coupled code, which becomes hard to maintain and test as the system grows.

### Part B: Minimal Examples or Scenarios

#### DRY Violation & Fix
## Part B: Minimal Examples or Scenarios

### DRY Violation & Fix


**Original Code (Violation of DRY)**:

```cpp
void printEmployeeDetails(Employee emp) {
    cout << "Employee Name: " << emp.name << endl;
    cout << "Employee Department: " << emp.department << endl;
}

void printCustomerDetails(Customer cust) {
    cout << "Customer Name: " << cust.name << endl;
    cout << "Customer Account Type: " << cust.accountType << endl;
}
```
**Rewritten**
```cpp
void printDetails(string name, string info) {
    cout << "Name: " << name << endl;
    cout << "Info: " << info << endl;
}

void printEmployeeDetails(Employee emp) {
    printDetails(emp.name, emp.department);
}

void printCustomerDetails(Customer cust) {
    printDetails(cust.name, cust.accountType);
}
```



