'''
Build on the previous exercise.

Create subclasses of two of the existing classes. Create a subclass of
one of those so that the hierarchy is at least three levels.

Build these classes out like we did in the previous exercise.

If you cannot think of a way to build on your previous exercise,
you can start from scratch here.

We encourage you to be creative and try to think of an example of
your own for this exercise but if you are stuck, some ideas include:

- A Vehicle superclass, with Truck and Motorcycle subclasses.
- A Restaurant superclass, with Gourmet and FastFood subclasses.

'''

class Employee(object):
    raise_amt = 1.04
    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = self.first_name + '.' + self.last_name + '@company.com'
    def full_name(self):
        return self.first_name + ' ' + self.last_name

    def emp_raise(self):
        self.pay = int(self.raise_amt * self.pay)

class Developer(Employee):
    def __init__(self, first_name, last_name, pay, prog_lang):
        super().__init__(first_name, last_name, pay)
        self.prog_lang = prog_lang

class SME(Developer):
    raise_amt = 2
    def __init__(self, first_name, last_name, pay, prog_lang):
        super().__init__(first_name, last_name, pay, prog_lang)



dev_1 = Developer('kaushik', 'pal', 100000, 'python')
sme_1 = SME('Laura', 'Svechenko', 160000, ['java', 'c++', 'Go'])

print(vars(sme_1))
print(dir(sme_1))
# print(dev_1.email)
# print(dev_1.pay)
# dev_1.emp_raise()
# print(dev_1.pay)
#
# print(sme_1.full_name())
# print(sme_1.pay)
# sme_1.emp_raise()
# print(sme_1.pay)
# print(sme_1.prog_lang)
print(help(sme_1))
