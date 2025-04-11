from connection import get_connetion
def delete_lessons(lesson_id):
     connection = get_connection()
     cursor = conncetion.cursor()
     sql = "DELETE FROM lessons WHERE id = %s"
     cursor.execute(sql, (lesson_id))
     connection.commit

if cursor.rowcount > 0:
    print("Diagraphike")
else:
     print("Den vrethike")

cursor.close()
connection.close()

try:
    lesson_id = int(input("eisagetai to id: "))
    delete_lesson(lesson_id)
except ValueError:
    print("Den valate egkuro id")
