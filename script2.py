import  pandas, pywhatkit

message = "Deneme mesaji"

data = pandas.read_csv('list.csv')
data_dict = data.to_dict('list')
numbers = data_dict['Numbers']
message = data_dict['Message']

for number in numbers:  
    pywhatkit.sendwhatmsg_instantly(f"+90{number}", "Deneme Mesaji", 5, True, 3)