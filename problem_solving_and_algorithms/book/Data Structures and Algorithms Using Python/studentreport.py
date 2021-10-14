from studentfile import StudentFileReader # Name of the file to open.
FILE_NAME = "students.txt"
def main():
# Extract the student records from the given text file.
  reader = StudentFileReader( FILE_NAME )
  reader.open()
  studentList = reader.fetchAll()
  reader.close()
# Sort the list by id number. Each object is passed to the lambda
   # expression which returns the idNum field of the object.
studentList.sort( key = lambda rec: rec.idNum ) # Print the student report.
  printReport( studentList )
