#=====global variables===========
user_credentials = {}
all_users_tasks = {}
user_tasks = {}
username = ""
password = ""

#=====lamda functions===========
# def lambda_handler(event,context):
#      data = client.scan(TableName = "Tasks")
#      return {
#           'statusCode' : 200,
#           'body' : json.dumps(data)
#      }

# def lambda_handler(event,context):
#      data = client.scan(TableName = "Credentials")
#      return {
#           'statusCode' : 200,
#           'body' : json.dumps(data)
#      }

def get_credentials():
    user_credentials = {
        "claudia" : "passwd1",
        "felippe" : "passwd2"
    }

def get_all_tasks():
    all_users_tasks = {
        {
            "assigned_username" : "felippe",
            "task_title" : "",
            "task_description" : "",
            "task_due_date" : "",
            "assigned_date" : ""
        },
        {
            "assigned_username" : "claudia",
            "task_title" : "",
            "task_description" : "",
            "task_due_date" : "",
            "assigned_date" : ""
        },
    }

def get_user_tasks():
        my_tasks = {
            "assigned_username" : "",
            "task_title" : "",
            "task_description" : "",
            "task_due_date" : "",
            "assigned_date" : ""        
        }

def authenticate():
    username = input("Username: ")
    password = input("Password: ")

    if username in user_credentials and user_credentials[username] == password:
        print("Login válido!")
    else:
        print("Credenciais inválidas.")

    print("You have successfully logged in!")

def register_user():
    pass

def add_task():
    user_tasks["assigned_username"] = input("You can now assign tasks, please enter the username of the person you would like to assign tasks to: ")
    user_tasks["task_title"] = input("Please enter the title of the task: ")
    user_tasks["task_description"] = input("Please enter the task description: ")
    user_tasks["task_due_date"] = input("Please enter the due date of the task in the format dd/mm/yyyy:")
    user_tasks["assigned_date"] = input("Please enter the date today in the format dd/mm/yyyy:")


def view_all_tasks():
    all_tasks = get_all_tasks()
    # all_tasks = line.strip().split(", ")
    for task in all_tasks:        
        print(f"Assigned to: {task[0]}")
        print(f"Title: {task[1]}")
        print(f"Description: {task[2]}")
        print(f"Due Date: {task[3]}")
        print(f"Assigned Date: {task[4]}")
        print(f"Status: {task[5]}")
        print()


def view_my_tasks():
    tasks = get_user_tasks()
    # my_tasks = line.strip().split(", ")
    for task in tasks:    
        if task[0] == username:
            print(f"Title: {task[1]}")
            print(f"Description: {task[2]}")
            print(f"Due Date: {task[3]}")
            print(f"Assigned Date: {task[4]}")
            print(f"Status: {task[5]}")
            print()
            
def store_to_dynamodb():
     pass

def main():
    while True:
        menu = input('''Select one of the following options:
    r - register a user
    a - add task
    va - view all tasks
    vm - view my tasks
    e - exit
    : ''').lower()
        if menu == 'r':
                new_username = input("To register a user, please enter the username of the new user: ").lower()
                new_password = input("Please enter the password for the new user: ").lower()
                confirmed_password = input("Please confirm the password for the new user: ").lower()
                while new_password != confirmed_password:
                        confirmed_password_retry = input("This does not match the previous password, please try again: ").lower()
                        if confirmed_password_retry == new_password:
                            # store_to_dynamodb()
                            print("New user successfully registered!")
                            break
        elif menu == 'a':
            add_task()
        elif menu == 'va':
            view_all_tasks()
        elif menu == 'vm':
            view_my_tasks()
        elif menu == 'e':
            exit()
        else:
            print("You have entered an invalid input. Please try again")

main()