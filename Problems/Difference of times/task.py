# put your python code here

first_hour = int(input())
first_minute = int(input())
first_second = int(input())

first_result = first_hour * 3600 + first_minute * 60 + first_second

second_hour = int(input())
second_minute = int(input())
second_second = int(input())

second_result = second_hour * 3600 + second_minute * 60 + second_second

result = second_result - first_result
print(result)
