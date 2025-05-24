# Write a function hours to seconds(hours) that converts hours to seconds (1 hour = 3600 seconds)
def convert(hours):
    sec=hours*3600
    return sec

num=int(input("Enter the number: "))
print(convert(num), "Secomd")