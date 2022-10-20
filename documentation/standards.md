# Dawn of the Abyss | Programming Standards

## Variable, Class and Function Naming

**Variables**
```python
# When naming variables, use standard camelCase

# Good variables (all standard camelCase)
playerHealth = 100
testingString = "Test"
anotherTestingString = "Another Test"

# Bad variables
player_health = 100 # Uses underscore
Testing_String = "Test" # Capitalization and underscore
AnotherTestingString = "Another Test" # camelCase, but uses caps at beginning (reserved for classes)

```

**Functions**
```python
# When naming functions, also use standard camelCase

# Good function name
def eventHandler():
    pass

# Bad function name
def event_handler(): # No underscores
    pass

def Event_Handler(): # What even
    pass

def EventHandler(): # CamelCase is reserved for classes
    pass
```

**Classes**
```python
# When naming classes use CamelCase (with all words first letter capped)

# Good class names
class Player(): # Only one word, gets capped
    pass

class ParticleSystem(): # Two words, both capped!
    pass

# Bad class names
class player(): # Why would you leave this lowercase?
    pass

class Particle_System(): # No underscores! (que Edna Mode - No Capes!)
    pass
```

## Docstrings
**Classes**

I really want to push for all classes to use docstrings.

```python
# One line docstrings
class ExampleClass():
    def __init__(self): # Single line docstring for classes with no args
        """This class is a one line example"""

class ExampleClass():
    def __init__(self, a, b, c, d=0.0): # If you have any argument, use a multi-line docstring and explain the arguments. Even if they make sense as written
        """This is a quick descriptor of what the class does

        Keyword arguments:
        a -- explain what this does
        b -- see above
        c -- see above
        d -- same thing, but give the default (default 0.0)
        """
```
**Functions**

Same as classes, unless the function has a return statement, in which case that should be detailed at the end of the multi-line docstring

```python
def getSomeValue(a, b): # Multi-line funciton example with return
    """This gets some value?

    Keyword arguments:
    a -- the first thing this needs
    b -- the second thing this needs

    Returns:
    varName -- what the returned thing is
    """
```