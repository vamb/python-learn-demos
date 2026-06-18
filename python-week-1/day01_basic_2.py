age = 20

if age >= 18:
    print("成年人")
else:
    print("未成年人")
print("======")
score = 85
if score >= 90:
    level = "优秀"
elif score >= 60:
    level = "及格"
else:
    level = "不及格"
print(level)
print("======")

is_active = True

if age >= 18 and is_active:
    print("有效的成年用户")
print("======")

name = ""
if not name:
    print("名字为空")

print("======")
def greet(name):
    return f"你好， {name}"
message = greet("Tom")
print(message)

print("======")
name = "外部变量"
def test():
    name = "局部变量"
    print(name)
test()
print(name)
print("======")

def is_valid_user(user: dict) -> bool:
    name = user.get("name")
    age = user.get("age")

    if not name:
        return False

    if not isinstance(age, int):
        return False

    return True


def is_adult_user(user: dict) -> bool:
    return user.get("age", 0) >= 18

users = [
    {"name": "Tom", "age": 20},
    {"name": "", "age": 18},
    {"name": "Jerry", "age": "16"},
]

for user in users:
    if not is_valid_user(user):
        continue

    if is_adult_user(user):
        print(user)

print("===")
with open("message.txt", "r", encoding="utf-8") as file:
    content = file.read()
print(content)

print("===")
with open("output.txt", "w", encoding="utf-8") as file:
    file.write("Hello porter greeting")