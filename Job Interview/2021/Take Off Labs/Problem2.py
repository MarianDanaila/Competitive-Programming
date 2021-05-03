"""
Idea: It's an iterative depth-first-search (I use stack) where hierarchy is a dictionary (HashMap).
I iterate through input string and whenever I find an employee name, I put him in the stack with the sub-hierarchy for
that employee (first an empty dictionary). Every time I find a closed parenthesis I pop from the stack and check
for 'Unavailable' employee to delete him from hierarchy.
In the end I transform the dictionary (HashMap) in a string and I apply a few 'replace' operations to look like the
expected output.
"""

string = input()
length = len(string)
hierarchy = {}
stack = [["", hierarchy]]
for i in range(length):
    if string[i] == "“":
        start_word = i+1
    elif string[i] == "”":
        end_word = i-1
        employee = '(' + string[start_word:end_word+1]
        manager = stack[-1][1]
        manager[employee] = {}
        stack.append([employee, manager[employee]])
    elif string[i] == ')':
        possible_removed = stack.pop()[0]
        if possible_removed == "(Unavailable":
            manager = stack[-1][1]
            manager.pop("(Unavailable")

string_hierarchy = str(hierarchy)
l = len(string_hierarchy)

final_hierarchy = string_hierarchy.replace(": {}", "}").replace("{", "").replace("}", ")").replace(":", ",").replace("'", "")[:-1]
print(final_hierarchy)
# Input:
# (“John”, (“Jasmine”, (“Jay”), (“Unavailable”)), (“Unavailable”, (“Jack”, (“Jeremy”))), (“Johanna”))
