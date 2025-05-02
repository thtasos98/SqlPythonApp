from connection import get_connection

def update_lesson(id,title,author,description):

          connection = get_connection()
          cursor = connection.cursor()

          updates = []
          values = []

          if title:
              updates.append("title = %s")
              values.append(title)

           if author:
              updates.append("author = %s")
              values.append(author)

           if description:
              updates.append("description = %s")
              values.append(description)

            if updates:
                 sql = f"UPDATE lessons SET {', '.join(updates)} WHERE id = %s"
                 values.append(id)
                 cursor.execute(sql,tuple(values))
                 connection.commit()

                if  cursor.rowcount > 0:
                     print("To update egine")
                else:
                     print("den vrethike
                     
            cursor.close()
            connection.close()

try:
   id = int(input("Eisagetai to id pou thelete na allaxete: "))
   title = int(input("Eisagetai to title pou thelete na allaxete: "))
   author = int(input("Eisagetai to author pou thelete na allaxete: "))
   description = int(input("Eisagetai to description pou thelete na allaxete: "))
except ValueError:
   print("Dwste egkiro id")
