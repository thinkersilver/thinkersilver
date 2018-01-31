project: distributedsystems
date: 2017-08-02
doc-name: consensus-intro
doc-title: FLP
package: consensus_intro
---

## Consensus

`The consensus problem involves an asynchronous system of processes, some of which may be
unreliable. The problem is for the reliable processes to agree on a binary value. In this paper, it is shown
that every protocol for this problem has the possibility of nontermination, even with only one faulty
process. By way of contrast, solutions are known for the synchronous case, the “Byzantine Generals”
problem. `



Imagine a system of reliable and unreliable processes communicating asynchronously. You are presented with a problem of reaching an aggreement on a binary value.

`The __FLP impossibility result__ states that the existance of at least one faulty process is enough to loose the guarantee of termination.`
If a node in a distributed cache suddenly dies or becomes unresponsive, the cluster can find itself in a situation where it can not reach aggreement on the value of an object. Assuming that there are no synchronized clocks available to the cluster it has to rely on time-outs to determine the death of a process.

![](/images/replicas_exchange.png)