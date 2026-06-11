listItems = list()

class ListItem():

  isComplete = False
  title = ''

  def __init__(self, title):
    listItems.append(self)
    self.title = title

  def set_as_complete(self):
    self.isComplete = True

  def get_listItem(self):
    return self

  @staticmethod
  def updateTitle(index, title):
    listItems[index].title = title

  @staticmethod
  def delete(index):
    del listItems[index]

listItemOne = ListItem('wash the dishes')

listItemTwo = ListItem('wash the floor')

# ListItem.delete(1)

ListItem.updateTitle(1, 'wash the kitchen')

# listItem.set_as_complete()
# print listItem.get_listItem().title

for item in listItems:
  print item.title
