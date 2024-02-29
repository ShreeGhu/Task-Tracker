from tabulate import tabulate
from colorama import init, Fore
init(autoreset=True)
from rich.console import Console

console =Console()

def add_tasks(task_list, task_description):
    task_list.append({'description': task_description, 'completed': False})

def update_task(task_list, task_index,new_description):
    task_index = int(task_index)
    if 0 <= task_index <  len(task_list):
        task_list[task_index]['description'] = new_description
        print(Fore.GREEN + 'Task updated successfully')
    else:
        print(Fore.RED + 'Invalid task index')

def complete_task(task_list, task_index):
    if 0 <= task_index <  len(task_list):
        task_list[task_index]['completed'] = True
        print(Fore.GREEN + 'Task completed successfully')
    else:
        print(Fore.RED + 'Invalid task index')

def delete_task(task_list, task_index):
    if 0 <= task_index <  len(task_list):
        del task_list[task_index]
        print(Fore.GREEN + 'Task deleted successfully')
    else:
        print(Fore.RED + 'Invalid task index')

def list_task(task_list):
    if not task_list:
        print(Fore.MAGENTA + 'No task has been added')
    else:
        headers = ['index', 'Description', 'Status']
        task_data = [[index, task['description'], f'{Fore.GREEN}Completed{Fore.RESET}'if task['completed'] else f'{Fore.YELLOW}Pending{Fore.RESET}'] for index, task in enumerate(task_list)]
        print(tabulate(task_data, headers=headers,tablefmt='grid'))

def main():
    tasks = []

    while True:
        print('Task Tracker Menu')
        print('1. Add Task')
        print('2. Update Task')
        print('3. Complete Task')
        print('4. Delete Task')
        print('5. List Task')
        print('6. Exit')

        choice = input('Enter your choice: ')

        if choice =='1':
            task_description = input('Enter task description: ')
            add_tasks(tasks,task_description)
            print(Fore.GREEN + 'Task has been added successfully')
        elif choice =='2':
            task_index = int(input('Enter the index of task you want to update: '))
            if task_index > len(tasks):
                print(Fore.RED + 'Invalid task index')
                continue
            new_description = input('Enter new description: ')
            update_task(tasks,task_index, new_description)

        elif choice =='3':
            task_index = int(input('Enter the index of task you want to complete: '))
            if task_index > len(tasks):
                print(Fore.RED + 'Invalid task index')
                continue
            complete_task(tasks, task_index)
        
        elif choice =='4':
            task_index = int(input('Enter the index of task you want to delete: '))
            if task_index > len(tasks):
                print(Fore.RED + 'Invalid task index')
                continue
            delete_task(tasks, task_index)
        
        elif choice=='5':
            list_task(tasks)
        
        elif choice =='6':
            print(Fore.BLUE +'Thank you for using Task Tracker')
        else:
            print(Fore.RED +'Invalid Choice')
            continue

if __name__ =="__main__":
    main()


