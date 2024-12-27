## strings are immutable
# orignal string change nahi ho sakta hai  like capital se small, small se capital
# replace method bhi only print karega new string ko but ol wala string remail same rahega.

string = "string"
string.replace("t", "T")
print(string)

# yaha pe hamne old string ko replace karke new variable me store kar diya hai
new_string = string.replace("t", "T")
print(new_string)

