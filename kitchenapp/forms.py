from django import forms 
from .models import  User, Menu, Kitchen


# kitchen = forms.mode(widget = forms.HiddenInput(), required = False)

class UserForm(forms.ModelForm):   
   username  = forms.CharField(max_length=100, required = True)
   first_name = forms.CharField(max_length=100, required = True)
   last_name = forms.CharField(max_length=100, required = True)
   password = forms.CharField(max_length=32, widget=forms.PasswordInput, required = True)
   question_1 = forms.CharField(max_length=100, required = True, initial="What is your favorite color?")
   answer_1 = forms.CharField(max_length=100, required = True)
   question_2 = forms.CharField(max_length=100, required = True, initial="What is your favorite place to live?")
   answer_2 = forms.CharField(max_length=100, required = True)
   is_provider = forms.BooleanField()
   class Meta:
      model = User
      fields = ('username', 'first_name', 'last_name', 'password', 'question_1',  'answer_1', 'question_2','answer_2', 'is_provider')

   def __init__(self, *args, **kwargs):
      super(UserForm, self).__init__(*args, **kwargs) # Call to ModelForm constructor
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
   
   
   

class MenuForm(forms.ModelForm):
   
   class Meta:
      model = Menu
      fields =('dish_name', 'price')

   class KitchenChoiceField(forms.ModelChoiceField):
      def label_from_instance(self, obj):
         return obj.kitchen_name

   dish_name  = forms.CharField(max_length=100, required=True)
   price = forms.DecimalField(max_digits=4, decimal_places=2, required=True)
   kitchen = forms.ModelChoiceField(queryset=Kitchen.objects.all(), initial=0, required=True)

   
   def __init__(self, *args, **kwargs):
        super(MenuForm, self).__init__(*args, **kwargs)
        self.fields['kitchen'].label_from_instance = lambda obj: "%s" % obj.kitchen_name