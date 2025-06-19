text = []
with open("textforadventofcode1.txt") as file:
    line = file.readlines()
    text = [string[:len(string)-1] for string in line]
#print(line)
#print(text)
total = 0
#text = ["two1nine",
#"eightwothree",
#"abcone2threexyz",
#"xtwone3four",
#"4nineeightseven2",
#"zoneight234",
#"7pqrstsixteen"]
for part in text:
    firstindex = 500000000
    lastindex = 0
    counter = 0
    #above variables are for part 2
    calibrationvalue = ""
    realval = 0
    for char in part:
        if char.isdigit():
            if calibrationvalue == "":
                firstindex = counter
            calibrationvalue += char
            lastindex = counter
        counter += 1
    numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in range(len(numbers)):
        if part.find(numbers[i]) < firstindex and part.find(numbers[i]) > -1:
            calibrationvalue = calibrationvalue[::-1] + str(i)
            calibrationvalue = calibrationvalue[::-1]
            firstindex = part.find(numbers[i])
            #print("f", firstindex, part[firstindex])
            if i == 0:
                print("!!!!!!!!!!!!!!!!!!!\n"*10)
        #print(i, end = '')
    for j in range(len(numbers)):
        if part.rfind(numbers[j]) > lastindex:
            calibrationvalue += str(j)
            lastindex = part.rfind(numbers[j])
            #print("l", lastindex, part[lastindex])
            if j == 0:
                print("!!!!!!!!!!!!!!!!!!!\n"*10)
    
    realval = int(calibrationvalue[0]+calibrationvalue[-1])
    print(realval)
    total += realval
print(total)
