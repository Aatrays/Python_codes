number = int(input("Enter the number you want to check: "))
is_prime = True
def prime_number(value):
  for i in range(2, value):
    if value % i == 0:
      is_prime = False
  if is_prime:
    print("It's is a prime number")
  else:
    print("It's not a prime number")

prime_number(value = number)
