age = 20
name = "Tom"
age_text = "30"

if 20 >= 18:
    print("成年人")
    print("name: " + name)
    print(type(name))
    print(name.upper())
    print(type(age))
    print(type(age_text))
    print(f"age_text: {age_text}, name {name}")
    print(int(age_text)+age)

text = "  Python,JavaScript,React  "

print(text)
print(text.strip())

users = ["Tom", "Jerry", "Alice"]
print(users[0])
print(users[2])
print(users[-1])
print(users[-2])

users.append("Bob")

print("===")
for user in users:
    print(user)

print("===")
for index, user in enumerate(users):
    print(index, user)

print("===")

user = {
    "name": "Tom",
    "age": 20,
    "email": "tom@example.com",
}

user["name"] = "Tom"
user["age"] = 21
user["is_active"] = True
print(user)
phone = user.get("phone")
print(f"user phone: {phone}")
print("======")
for key in user:
    print(f"{key}: {user.get(key)}")