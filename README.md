# Automated Test-Cases Generation

There are many free symbolic execution tools available. However, since symbolic execution generates
a large number of test cases, it is impractical to run all the generated test cases in practice. Number of
test-cases should be lower so that they can be veried manually. But, these test-cases also needs to cover
atomic conditions in the solution.

## Quick start

```
$ ./Run.sh model.c "test/*" "xml"
```
