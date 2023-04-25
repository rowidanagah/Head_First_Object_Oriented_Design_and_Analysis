__UML till pg 230__

![](https://github.com/Rowida46/Head_First_Object_Oriented_Design_and_Analysis/blob/main/ch5/UML.png)

# To sum up ::

## Abstract Classes

It work as a placehoulder for actaul implementation class tok define behavior, *However*
__subclasses__ implement that behavior.

## Encapsulation

The main objective of it is to protect your classes from unnecessary changes.
- Just try your hardest to encapsulate what varies.

### Generalization

Used to show that a class extends or inhierts form another class or a more generalized one.


### Association 

Association is a semantically weak relationship between unrelated objects. It's *"using"* relation between objects in which the objects have their own lifetime and there is no owner.

__ex__ :: A relationship between a doctor and a patient.

 An association relationship between two or more objects denotes a path of communication betwen them.


### Aggregation

 It's a special form of association to show that our thhing or class is made up of another class.

 Aggregation is a specialized form of association between two or more objects in which each object has its own life cycle but there exists an ownership as well.


### Composition 

Composition is most powerful when you want to use behavior to be defined in an interfance.

- It allowyou to use behavior from a family of other classes, and to chane that behavior at the runtime.

- When an objectis composed of other objects and that owing object is destroyed, the obj that are pert of the composition go away too.

- *Composition* is about ownership. _the main obj *owns* the composed bevavior_. 


> Notes
- Treat your subclasses as a placeholders for actual implementation. The abs class  *defines* the behavior and subclass *implement* that behavior.


- Diff properties, Use hash map....!

#### What is interface ?

A class that lotsof classees can inheriet common behaviors 
- Coding to an interface rather than an implementation make your code easyto be extended.


 - Classes about the behavior, and the reason that we create subclasses is the diff properties.
