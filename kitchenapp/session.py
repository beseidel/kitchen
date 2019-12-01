

class Session(object):
   
   def __init__(self, request):
      self.session = request.session

   def get(self,key):
      return self.session.get(key) 

   def add(self, key, value):
      self.session[key] = value

   def remove(self, key, value):
      self.session.pop(key)

   def removeAll(self):
      self.session.clear()



