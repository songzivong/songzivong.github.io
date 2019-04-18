---
title: "Annotations to Pro Git, 2nd Edition"
filename: annotations-to-pro-git-2e
layout: post
categories: Annotations
tags: git 
---

[*Pro Git*, 2nd Edition](https://git-scm.com/book/en/v2) was written by Scott Chacon and Ben Straub and published in 2014.

## 3. Git Branching

### 3.1. Branches in a Nutshell

> Git doesn’t store data as a series of changesets or differences, but instead as a series of **snapshots**.

A snapshot :camera: is a [checksum](https://en.wikipedia.org/wiki/Checksum) of all files in the repository. The Git checksum uses [SHA-1](https://en.wikipedia.org/wiki/SHA-1). The hash value of SHA-1 is a hexadecimal number, 40 digits long.

> When you make a commit, Git stores a commit object that contains a pointer to the snapshot of the content you staged. This object also contains the author’s name and email address, the message that you typed, and pointers to the commit or commits that directly came before this commit (its parent or parents): zero parents for the initial commit, one parent for a normal commit, and multiple parents for a commit that results from a merge of two or more branches.

{% include image.html name="commit-and-parents.png" %}
{% include image.html name="commit-and-tree.png" %}

All commit objects live in `.git/objects/`, in a binary file format. Suppose the checksum of a commit object is `0a012dd29c6129a4347622e3748869fcab6c6e48`, then all information is stored in a file with a path `.git/objects/0a/012dd29c6129a4347622e3748869fcab6c6e48`.
