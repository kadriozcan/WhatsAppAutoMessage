import  pandas, pywhatkit


data = pandas.read_csv('list.csv')
data_dict = data.to_dict('list')
numbers = data_dict['Numbers']
message = "deneme"

for number in numbers:  
    pywhatkit.sendwhatmsg_instantly(f"+90{number}", message, 5, True, 3)