# fichier contenant mes validateurs de mots de passe on peut creer d'autre validateur pour d'autre champ d'1 autre formulaire

# cette classe /chaque classe validator possede 2 methodes a implementer elle ont ces nom par conevention

#on ajouitera notre validateur dans le fichier setting au niveau de  validation

#par exple si on veut verifier les code postal entrer depuis un formulaire il suffit juste de definir ici une class validator pour ce formulaire et importer ce fivhier de validations dans notre fichier de forms
#ceci pour etre sur de la nature de donner recu :il suffit juste d'ajouter un champ (conevention validators=[validators.Nom_De_Ma_Classe_De_Validation])

from django.core.exceptions import ValidationError



class ContainsLetterValidator:

	def validate(self,password,user=None):
		if not any(char.isalpha() for char in password):
			raise ValidatonError('Le Mot de Passe doit contenir une lettre ',code='password_no_letters')


	def get_help_text(self):
	  return 'Votre mot de passe doit contenir au moins une lettre majuscule ou miniscuele.'




#validateur qui verifie si le mot de passe contient un chifrre 

class ContainsNumberValidator:

	def validate(self,password,user=None):
		if not any(character.isdigit() for character in password):
			raise ValidatonError('Le Mot de Passe doit contenir une chiffre ',code='password_no_digit')

	def get_help_text(self):
		return 'Votre Mot De passe doit conteniir au moins un chiffre !'
				