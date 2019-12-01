from django import forms 
from .models import  User, Menu, Kitchen


# kitchen = forms.mode(widget = forms.HiddenInput(), required = False)
class SignUpForm(forms.ModelForm):   
   question_1 = forms.CharField(max_length=100, required = True, initial="What is your favorite color?")
   answer_1 = forms.CharField(required = True)
   question_2 = forms.CharField(max_length=100, required = True, initial="What is your favorite place to live?")
   answer_2 = forms.CharField(required = True)
   is_provider = forms.BooleanField(required=False)
   class Meta:
      model = User
      fields = "__all__"

   def __init__(self, *args, **kwargs):
      super(UserForm, self).__init__(*args, **kwargs) 
      self.fields['question_1'].widget.attrs['style'] = 'width:300px;'
      self.fields['question_2'].widget.attrs['style'] = 'width:300px;'


class LoginForm(forms.ModelForm):
   class Meta:
      model = User
      fields = ('username','password')

   class UserChoiceField(forms.ModelChoiceField):
      def label_from_instance(self, obj):
         return obj.username
   
   username  = forms.CharField(max_length=100, required = True, initial="What is your favorite place to live?")
   password = forms.CharField(max_length=32, widget=forms.PasswordInput)
   
   

class AddDishForm(forms.ModelForm):
   
   class Meta:
      model = Menu
      fields = "__all__"

   class KitchenChoiceField(forms.ModelChoiceField):
      def label_from_instance(self, obj):
         return obj.kitchen_name

   def __init__(self, *args, **kwargs):
      super(AddDishForm, self).__init__(*args, **kwargs)
      self.fields['kitchen']=forms.ModelChoiceField(queryset=Kitchen.objects.all(), required=True)
      self.fields['kitchen'].label_from_instance = lambda obj: "%s" % obj.kitchen_name
      self.fields['is_vegan'] =  forms.BooleanField(required=False)

   # @classmethod
   #  def create(cls):
   #      book = cls(price=678)
   #      return book
   # def setNew(self):
   #    dish = super(AddDishForm, self).save(commit=False)
   #    dish.price = 789
   #    dish.save()

      

   


class AddKitchenForm(forms.ModelForm):
   class Meta:
      model = Kitchen
      fields = ('kitchen_name',)
   kitchen_name = forms.CharField(max_length=50, required=True)
   image = forms.FileField(required=True)

