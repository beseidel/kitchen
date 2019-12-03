from .models import User, Kitchen, Menu


class KitchenSession(object):
   
   def __init__(self, request):
      self.session = request.session


   def getUserObject(self):
      user = self.session.get('user')
      return User.objects.get(username=user[0], password=user[1])

   def isProvider(self):
      user = self.session.get('user')
      if user == None:
         return False
      return user[2]
   
   def getKitchenObject(self, kitchen_id):
      return Kitchen.objects.get(id=kitchen_id)

   def getDishObject(self, dish_id):
      return Menu.objects.get(id=dish_id)

   def add(self, key, value):
      self.session[key] = value

   def remove(self, key, value):
      self.session.pop(key)

   def removeAll(self):
      self.session.clear()



