project: distributedsystems
date: 2017-08-06
doc-name: consensus-problems
doc-title: FLP
package: consensus_problems
---

## Problem Instantiations

Aggreeing on a value in a distributed system is fundamental to algorithms which drive
* distributed file management
* distributed operations on data
* tolerating fault in distributed operations
### The *transaction commit problem*

Several things can go wrong when multiple processes are executing a transaction and have to agree on the commit to the backing store. These problems fall into the following categoires

* request loss
* response loss
* corrupt responses - an incorrect or malicious response is recieved

*** Message loss ***
Messages can be lost if the network goes down ( network partition), the process crashes, the operating system crashes. All these type of failures can be seen as a network partition.

** Message Distortion ***
The request or response messages can be distorted. Some messages may be duplicated and finally messages may be tampered with by an adverserial actor.

## Consensus Algorithms
[checkout out: dolev](http://www.cse.huji.ac.il/~dolev/pubs/p401-dolev.pdf)

Consensus Algorithms are evaluated by the number of faults they can tolerate. There are 3 properties which are interesting when looking at a consensus algorithm

* termination - a decision or agreement is reached
* agreement - all processes decide on the same value
* validity - a process is used to determine the value to be agreed upon



### Types of Byzantine Failure