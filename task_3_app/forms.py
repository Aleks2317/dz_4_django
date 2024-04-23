from django import forms


class GameForm(forms.Form):
    game = forms.ChoiceField(choices=[('coin', 'монета'), ('numb', 'кости'), ('number', 'числа')],
                             widget=forms.RadioSelect(attrs={
                                 'class': 'form-check-input',
                             }))
    count_game = forms.IntegerField(min_value=1, max_value=64,
                                    widget=forms.NumberInput(attrs={
                                        'class': 'from-control'
                                    }))
