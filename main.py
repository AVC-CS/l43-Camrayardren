def main():
    
    total = 0
    inputs = []


    while len(inputs) < 5:
        number = int(input(f"Enter number #{len(inputs) + 1}: "))
        total += number
        inputs.append(number)

    print("The running total is:", total)
    ########################################
    # Do not delete the return statement
    ########################################
    return total


if __name__ == '__main__':
    main()
