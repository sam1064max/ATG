# Automated Test-Cases Generation

There are many free symbolic execution tools available. However, since symbolic execution generates
a large number of test cases, it is impractical to run all the generated test cases in practice. Number of
test-cases should be lower so that they can be verified manually. But, these test-cases also needs to cover
atomic conditions in the solution.

###Prerequisites
[Klee](http://klee.github.io/getting-started/), [gcovr] (http://gcovr.com/guide.html)

Scared of Klee ? Use the docker images of ATG.

```
$ docker pull sam1064max/atg
```

## Quick start

```
$ ./Run.sh <klee-compatible-c-code-file> <gcc-compatible-c-code-file>
```
