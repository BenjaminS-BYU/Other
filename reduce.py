def numberOfSteps(num, total_steps = 0):
        if num == 0:
            return total_steps
        # If the num is even
        if num % 2 == 0:
            num = num // 2
            total_steps += 1
        # If num is not even
        if num % 2 != 0:
            num -= 1
            total_steps += 1
        return numberOfSteps(num, total_steps)
        

print(numberOfSteps(14))