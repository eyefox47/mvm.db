from django import forms
from .models import Pokemon, Character, Pet


class PokemonForm(forms.ModelForm):

    class Meta:
        model = Pokemon
        fields = ('image', 'name', 'player', 'campaign', 'pronouns',
                  'pokedex_nr', 'kind', 'type_p',
                  'trainer', 'nature', 'description')


class CharacterForm(forms.ModelForm):

    class Meta:
        model = Character
        fields = ('image', 'name', 'player', 'campaign', 'pronouns',
                  'cclass', 'description')


class PetForm(forms.ModelForm):

    class Meta:
        model = Pet
        fields = ('image', 'name', 'player', 'trainer', 'campaign', 'pronouns',
                  'cclass', 'description')


class NPCForm(forms.ModelForm):

    class Meta:
        model = Character
        fields = ('image', 'name', 'campaign', 'pronouns',
                  'cclass', 'description')
