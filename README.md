
# learning_type_checking_python
Doing type checking statically (mypy) and in runtime (pytypes and typical)


## Runtime checking
Pytypes @typechecked and typical @typic.al decorators assure type checking when building an object for a class and when calling a method.

## Static type checking
Mypy can be executed to type check code before executing it.
```commandline
mypy . --explicit-package-bases --namespace-packages --strict 
```