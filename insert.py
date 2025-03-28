from connection import get_connection

def insert lessons(title,author,description):
    connection = get_connection()
    cursor = connection.cursor()
    sql = "INSERT INTO lessons (title,author,description) VALUES (%s, %s, %s)"
    values = (title,author,description)
    cursor.execute(sql,values)
    connector.commit()
    print("Το μάθημα προστεθήκε")
    cursor.close()
    connection.close()

insert_lesson("mathimatika","tasos","propedia")    
insert_lesson("istoria","tasos","odyseia")
