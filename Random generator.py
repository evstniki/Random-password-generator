import random
import string

password_length = random.randint(8, 25)
characters = string.ascii_letters + string.digits
password = "".join(random.choice(characters) for i in range(password_length))
print(password)