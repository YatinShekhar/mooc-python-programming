def new_person(name, age):
    if not name or len(name.split()) < 2 or len(name) > 40:
        raise ValueError("Invalid name: Name must have at least two words and be between 1 and 40 characters.")

    if age < 0 or age > 150:
        raise ValueError("Invalid age: Age must be between 0 and 150.")

    return (name, age)


if __name__ == "__main__":
    try:
        person = new_person("John Doe", 25)
        print(person)
    except ValueError as e:
        print(e)