# py-oops
Object Oriented Concepts in Python

The style of programming where the focus is on the objects is known as OBJECT ORIENTED PROGRAMMING..

An object is any real-world entity which has some attributes and behavior.

A class is a logical concept not a real-world entity. The class provides the attributes and behavior which an object should possess to belong to the class.

Here the `__init__(self)`: is a magical function. It is called automatically whenever an object is created for the class. Such functions are also called as "Constructors"!

The value for self is automatically taken based on the object. We don't have to explicitly pass value for self.

All the objects belonging to this class would posses the attributes. Hence these attributes are also known as instance variables.

The attributes of an object are accesses using the dot(.) operator.

The data needed by an object stays in the object. It cannot be accessed without the object. This is an Object Oriented principle called as ENCAPSULATION.

Methods are functions written inside a class. Methods represent the behavior.

Always remember that in a method since 'self' is not a keyword, no matter what variable is used, the first parameter is always considered as the implicit reference to the object used.

We need not know how a method works internally to invoke it on an object. This is an object oriented principle called as ABSTRACTION.
For example, we need not know that inside the eat_banana() method there is a check happening for monkey breed. We can invoke it on a baboon also and a chimpanzee also.

OOP is never short of magic! You can create attributes and methods in a common class and inherit them in other classes!