# 5.4 Stack (14%)

Implementieren Sie einen Stack, welcher auf einem dynamischen Array operiert und Elemente mit beliebigen Datentypen beinhalten kann. Dieser Stack soll die Funktionen "push", "pop", "top", "is_empty" und "size" anbieten. Elemente sollen immer am Ende des Arrays hinzugefügt werden. Es ist erlaubt Elemente mit Hilfe der "append"-Funktion zu diesem Array hinzuzufügen.

```python
# Schreiben Sie Ihren Code in die untenstehenden Funktion. Verändern Sie dabei nichts am bereits vorhandenen Code.
# "stack" ist ein Array und "element" ist ein Element, welches hinzugefügt werden soll.
# Es ist nicht nötig einen Rückgabewert zu definieren.
def push(stack, element):
    stack.append(element)
# Schreiben Sie Ihren Code in die untenstehenden Funktion. Verändern Sie dabei nichts am bereits vorhandenen Code.
# "stack" ist ein Array. Falls "stack" keine Elemente besitzt, dann soll "None" zurückgegeben werden.
# Ansonsten soll das letzte Element, das zu "stack" hinzugefügt worden ist, zurückgegeben und aus "stack" entfernt werden.
def pop(stack):
    if not stack:
        return None
    return stack.pop()
# Schreiben Sie Ihren Code in die untenstehenden Funktion. Verändern Sie dabei nichts am bereits vorhandenen Code.
# "stack" ist ein Array. Falls "stack" keine Elemente besitzt, dann soll "None" zurückgegeben werden.
# Ansonsten soll das letzte Element, das zu "stack" hinzugefügt worden ist, zurückgegeben werden.
def top(stack):
    if not stack:
        return None
    return stack[-1]
# Schreiben Sie Ihren Code in die untenstehenden Funktion. Verändern Sie dabei nichts am bereits vorhandenen Code.
# "stack" ist ein Array. Falls "stack" keine Elemente besitzt, dann soll "True" zurückgegeben werden, andernfalls "False".
def is_empty(stack):
    return len(stack) == 0
# Schreiben Sie Ihren Code in die untenstehenden Funktion. Verändern Sie dabei nichts am bereits vorhandenen Code.
# "stack" ist ein Array. Die Anzahl der Elemente von "stack" soll als Integer zurückgegeben werden.
def size(stack):
    return len(stack)
# Weisen Sie der untenstehenden Variable den Wert True zu, sobald Sie die Aufgabe erfolgreich erledigt haben!
​
# Datentyp: bool
exercise_5_4_solved = True
​
# DEINE ANTWORT HIER
# Benutzen Sie diesen Funktionsaufruf um Ihr Ergebnis zu testen.
# Damit diese Zelle ausgeführt werden kann, führen Sie zuerst die Zellen mit den entsprechenden Funktionen aus.
​
#Create an empty stack
stack = []
​
#Print the stack - expected output: []
print("Stack: " + str(stack))
​
#Pushing an element onto the stack
print("Pushing element: \"Hello\"");
push(stack, "Hello")
​
#Print the stack - expected output: ['Hello']
print("Stack: " + str(stack))
​
#Check if the stack is empty
print("Empty?: " + str(is_empty(stack)))
​
#Pushing an element onto the stack
print("Pushing element: 5");
push(stack, 5)
​
#Print the stack - expected output: ['Hello', 5]
print("Stack: " + str(stack))
​
#Check the size of the stack
print("Size: " + str(size(stack)))
​
#Retrieve the top element of the stack
print("Top: " + str(top(stack)))
​
#Print the stack - expected output: ['Hello', 5]
print("Stack: " + str(stack))
​
#Retrieve the top element of the stack and delete it
print("Pop: " + str(pop(stack)))
​
#Print the stack - expected output: ['Hello']
print("Stack: " + str(stack))
​
#Check the size of the stack
print("Size: " + str(size(stack)))
​
#Retrieve the top element of the stack and delete it
print("Pop: " + str(pop(stack)))
​
#Check if the stack is empty
print("Empty?: " + str(is_empty(stack)))
​
#Print the stack - expected output: []
print("Stack: " + str(stack))
```
