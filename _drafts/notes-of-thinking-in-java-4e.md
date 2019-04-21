---
layout: post
title: "Notes of Thinking in Java, 4th Edition"
categories: "Notes"
tags: java
---

[*Thinking in Java*, 4th Edition](https://www.amazon.com/dp/0131872486) was written by [Bruce Eckel](https://www.bruceeckel.com/) and published in 2005. So the version of Java is limited to Java SE 6 and below. In the days (2019) I am reading this book, [Java 12](https://www.oracle.com/technetwork/java/javase/12-relnote-issues-5211422.html) has been published.

{% include toc.html %}

## The Style of This Book

Each chapter in this book tries to teach a single feature, or a small group of associated features, without relying on concepts that haven't been introduced yet. Because the author thought that if you teach a lot of new features to the audience would make them confused. Though, I don't think that bottom-up is not a perfect even possible way to introduce a programming language.

Anyway, these features are:

- Everything Is an Object
- Operators
- Controlling Execution
- Initiallization & Cleanup
- Access Control
- Reusing Classes
- Polymorphism
- Interfaces
- Inner Classes
- Holding Your Objects
- Error Handling with Exceptions
- Strings
- Type Information
- Generics
- Arrays
- Containers in Depth
- I/O
- Enumerated Types
- Annotations
- Concurrency
- GUI

### Examples

This book uses examples that are simple and short as possible ("toy examples"), and they are not "real world" problems.

> I’ve found that beginners are usually happier when they can understand every detail of an example rather than being impressed by the scope of the problem it solves. Also, there’s a severe limit to the amount of code that can be absorbed in a classroom situation.

However, I still prefer the real world examples. K&R C was written in that way.

## What is OOP

### The Progress of Abstraction

Two ways of abstraction:

- From the solution world. Assembly language is a small abstraction of the underlying machine. FORTRAN, BASIC, and C are abstractions of assembly language. They are high level programming languages, but they still requires you to think in terms of the structure of the computer.
- From the problem world. In LISP, all problems are lists. In APL, all problems are algorithmic. Prolog casts all problems into chains of decisions. However, they are all too narrow, so that each of them can only solve a particuar class of problems.

OOP builds a connection between the solution world and the problem world. Every element in the problem space has a representation in the solution space as "object". So you can describe your problems based on the language of solution space, and every object is like a little computer -- it has a state, and it has operations.

[Alan Kay](https://en.wikipedia.org/wiki/Alan_Kay) summarized five basic characteristic of OOP:

1. **Everything is an object.**
2. **A program is a bunch of objects telling each other what to do by sending messages.**
3. **Each object has its own memory made up of other objects.**
4. **Every object has a type.**
5. **All objects of a particular type can receive the same messages.**