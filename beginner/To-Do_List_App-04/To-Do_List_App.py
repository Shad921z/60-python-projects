import sqlite3

# Connect to the database
conn = sqlite3.connect('todo.db')
cursor = conn.cursor()

# Create the table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS todo (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL,
        completed INTEGER DEFAULT 0
    )
''')

# Function to add a task
def add_task(task, completed=False):
    cursor.execute("insert or ignore into todo (task) values (?)", (task,))
    conn.commit()

# Function to mark a task as completed
def mark_completed(task_id):
    cursor.execute('UPDATE todo SET completed = 1 WHERE id = ?', (task_id,))
    conn.commit()

# Function to delete a task
def delete_task(task_id):
    cursor.execute('DELETE FROM todo WHERE id = ?', (task_id,))
    conn.commit()

# Function to list all tasks
def list_tasks():
    cursor.execute('SELECT * FROM todo')
    return cursor.fetchall()

# INPUT TASK FROM THE USER
while True:
    inputopt = input("Enter 1 to add a task \n Enter 2 to mark a task as completed \n Enter 3 to delete a task \n Enter 4 to list all tasks \n Enter 0 to exit: \n\n>>> ")

    if inputopt == "1":
        add_task(input("Enter a task: "))
        print("Task added successfully!")

    elif inputopt == "2":
        tasks = list_tasks()
        for task in tasks:
            print(f"ID: {task[0]}, Task: {task[1]}, Completed: {task[2]}")
        task_id = int(input("\n Enter the task ID to mark as completed \n 0=Not Completed and 1=Completed : "))
        mark_completed(task_id)
        print("Task marked as completed!")

    elif inputopt == "3":
        tasks = list_tasks()
        for task in tasks:
            print(f"ID: {task[0]}, Task: {task[1]}, Completed: {task[2]}")
        task_id = int(input("\n 0=Not Completed and 1=Completed \n Enter the task ID: "))
        delete_task(task_id)
        print("Task deleted successfully! \n \n")

    elif inputopt == "4":
        tasks = list_tasks()
        for task in tasks:
            print(f"ID: {task[0]}, Task: {task[1]}, Completed: {task[2]} \n 0=Not Completed and 1=Completed")

    elif inputopt == "0":
        print("Goodbye!")
        break

    else:
        print("Invalid input. Please enter a valid option.")


conn.close()


