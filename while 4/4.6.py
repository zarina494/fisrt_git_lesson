numbers = [1,3,5,4,6,2,8,9,7]
prime_numbers = []
non_prime_numbers = []

i = 0

while i < len(numbers):
    if numbers[i] % 2 == 0:
        prime_numbers.append(numbers[i])
    else:
        non_prime_numbers.append(numbers[i])
    i += 1
print(f'Obshii spisok {numbers}')
print(f'4etnye 4islami: {prime_numbers}')
print(f'Ne4etnye 4isla: {non_prime_numbers}')
