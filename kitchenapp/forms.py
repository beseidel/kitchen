from django import forms 
from .models import  User, Menu, Kitchen, KitchenImage


# kitchen = forms.mode(widget = forms.HiddenInput(), required = False)
class SignUpForm(forms.ModelForm):   
   question_1 = forms.CharField(max_length=100, required = True, initial="What is your favorite color?")
   answer_1 = forms.CharField(required = True)
   question_2 = forms.CharField(max_length=100, required = True, initial="What is your favorite place to live?")
   answer_2 = forms.CharField(required = True)
   class Meta:
      model = User
      fields = "__all__"
      labels = {
        "is_provider": "Become seller"
      }

   def __init__(self, *args, **kwargs):
      super(SignUpForm, self).__init__(*args, **kwargs) 
      fields = self.fields
      fields['question_1'].widget.attrs['style'] = 'width:300px;'
      fields['question_2'].widget.attrs['style'] = 'width:300px;'
      fields['is_provider'].required = False


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
      fields = self.fields
      fields['kitchen']=forms.ModelChoiceField(queryset=Kitchen.objects.all(), required=True, initial=0)
      fields['kitchen'].widget.attrs['style'] = 'width:100px;'
      fields['kitchen'].label_from_instance = lambda obj: "%s" % obj.kitchen_name
      fields['is_vegan'].required=False


class AddKitchenForm(forms.ModelForm):
   class Meta:
      model = KitchenImage
      fields = '__all__'
   # kitchen_name = forms.CharField(max_length=50, required=True)
   
   def __init__(self, *args, **kwargs):
      super(AddKitchenForm, self).__init__(*args, **kwargs)
      self.fields['image'].required = True
      self.fields['name'].required = True









# @classmethod
   #  def create(cls):
   #      book = cls(price=678)
   #      return book
   # def setNew(self):
   #    dish = super(AddDishForm, self).save(commit=False)
   #    dish.price = 789
   #    dish.save()