import string
import random
table = {
    'book': 'NA',
    'author': 'NA',
}
newData = {}
def add(table, newData):
  while True:
      inputData = dict.fromkeys(table.keys())
      inputData = {
          'book': input("Student Name : "),
          'author': input("Student Class : ")
      }
      key = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
      newData.update({key: inputData})
      print(f"\n {'key':<10} {'book name':<35} {'author':<20}")
      print('-'*50)
      for inputData in newData:
          key = inputData
          data = {
              'book': newData[key]['book'],
              'author': newData[key]['author']
          }
          print(f"\n {key:<10} {data['book']:<35} {data['author']:<20}")
      print('\n')
      y = input("wanna continue? (y/n)")
      if y.upper() == "N":
          break

def remove(newData):
  for data in newData:
      dataId = data
  remove = newData.pop(dataId)
  print(f"Removing : {remove['book']}")
  print(f"\n {'key':<10} {'book':<35} {'author':<20}")
for data in newData:
    dataId = data
    print(
        f"\n {dataId:<10} {newData[dataId]['book']:<35} {newData[dataId]['author']:<20}")