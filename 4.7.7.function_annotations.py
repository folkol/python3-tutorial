def f(ham: str, eggs: str = 'eggs', amount: int = 666) -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + amount * eggs

print(f('spam'))

