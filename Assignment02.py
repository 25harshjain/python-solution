#problem 1
with open("f1.txt", "r+") as f:
    str = f.read()
    str1 = str.split(",") 
    ans = str1[::-1]       
    an1 = ",".join(ans)

with open("f1.txt","w+") as of:
    of.write(an1)   
    of.close()        

#problem 2
def numtoword(num):
    if num == 0:
        return " zero "
    
    arr = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    result = ""
    while num != 0:
        small_ans = arr[num % 10]
        result = small_ans + result
        num = int(num / 10)
    return result


def convert_numbers_to_words(input_text):
    result = ""
    is_inside_number = False

    for char in input_text:
        if char.isdigit():
            if not is_inside_number:
                result += numtoword(int(char))
                is_inside_number = True
            else:
                result += numtoword(int(char)).rstrip()
        else:
            result += char
            is_inside_number = False

    return result

with open("f2.txt", "r") as f:
    content = f.read()

converted_content = convert_numbers_to_words(content)

with open("new_f2.txt", "w") as of:
    of.write(converted_content)

print("Conversion complete. Check 'new_f2.txt' for the result.")


#problem 3
def create_student_dictionary(file_path):
    student_dict = {}
    current_key = None

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith("Roll:"):
                current_key = line.split(":")[1].strip()
                student_dict[current_key] = {}
            elif current_key and line:
                key, value = map(str.strip, line.split(":", 1))
                student_dict[current_key][key] = value

    return student_dict

file_path = "f3.txt"
student_dictionary = create_student_dictionary(file_path)

print("Student Dictionary:")
print(student_dictionary)