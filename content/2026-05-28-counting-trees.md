Title: Notes on Counting Tree Structures
Date: 2026-05-28
Tags: combinatorics; notes

A few months ago, I gave a talk at our chair's seminar on counting tree-like structures. Here, I am sharing my [notes](notes/kalinke26-counting-trees-notes.pdf) and the accompanying [slides](notes/kalinke26-counting-trees-slides.pdf).

## Introduction

The idea of these notes is to introduce tree counting to computer scientists
by combining extraordinary existing expositions, each focusing on a particular
subtopic needed, in a consistent fashion. To do so, we let ourselves be guided by
the following classical problems in combinatorics.


- Given three distinct dice, what is the probability that their eyes sum to
ten?
- How many ways are there of making change for $1?
- What is the number of necklaces that can be constructed from five beads
available in three distinct colors?
- In how many ways can the corners of a square be colored?
- How many trees with a given number of nodes are there?


Indeed, by addressing these questions one by one, we build up to the Pólya
enumeration theorem [Pólya, 1937][^polya37counting], one of the most powerful results in enumerative combinatorics, and used here to enumerate the number of trees with given
node degree. Along the way, we recall generating functions, some group theory,
Burnside’s lemma, and Otter’s dissimilarity characteristic theorem.


The exposition of Pólya’s enumeration theorem follows Tucker [1974][^tucker74polya]. For
counting trees, we rely on Harary and Palmer [1973][^harary73graphicalenumeration]. Additional helpful resources,
besides the ones stated in the main text below, include Riordan [1958][^riordan58combinatorialanalysis], Harary
[1969][^harary69graphtheory], Shapiro [1973][^shapiro73finitegroups], Judson [2022][^judson22abstractalgebra].

... continued in the pdf linked above.


## References

[^polya37counting]: G. Pólya. Kombinatorische Anzahlbestimmungen für Gruppen, Graphen und chemische Verbindungen. Acta Mathematica, 68(1):145–254, 1937.
[^tucker74polya]: Alan Tucker. Polya’s enumeration formula by example. Mathematics Magazine, 47:248–256, 1974.
[^harary73graphicalenumeration]: Frank Harary and Edgar M. Palmer. Graphical Enumeration. Academic Press, 1973.
[^riordan58combinatorialanalysis]: John Riordan. An Introduction to Combinatorial Analysis. John Wiley & Sons, 1958.
[^harary69graphtheory]: Frank Harary. Graph Theory. Addison-Wesley, 1969.
[^shapiro73finitegroups]: Louis W. Shapiro. Finite groups acting on sets with applications. Mathematics Magazine, 46(3):136–147, 1973.
[^judson22abstractalgebra]: Thomas W. Judson. Abstract Algebra. orthogonal publishing l3c, 2022.