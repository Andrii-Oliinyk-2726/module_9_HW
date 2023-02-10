replies = ["hello", ["good bye", "close", "exit"]]
answers = ['How can I help you?', 'Good bye!']
phonebook = {}

def input_error(func):
    def inner(*args):
        try:
            result = func(*args)
            return result
        except:
            return "Give me name and phone please"
    return inner

# hello-good_bye-others
@input_error
def reply(answer):
    if answer == replies[0]:
        return answers[0]
    elif answer in replies[1]:
        return answers[1]
    else:
        comand = answer.split()
        return add_change_shows(comand)

# phone_add-change-shows 
@input_error     
def add_change_shows(comand):
    if comand[0] == 'add' or comand[0] == 'change':
        phonebook[comand[1]] = comand[2]
        print(phonebook)
        return "Ok"
    elif comand[0] == 'phone':
        return phonebook[comand[1]]
    elif comand[0] == 'show' and comand[1] == 'all':
        return phonebook
    else:
        return "I don't understand you"    

def main():
    botloop = True
    while botloop:
        print('user:', end=' ')
        rep = input().lower()
        print(reply(rep))
        if rep in replies[1]:
            botloop = False
       

if __name__ == '__main__':
    main()
    