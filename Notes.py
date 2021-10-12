
def saisir_note() -> float :
    """ ==================================================================================================================
    
       * Description :
            permet d'entrer une valeur
        
        * Exemple :
            entrée: 10
            sortie: 10 (en float)
            
        * Préconditions :
            les valeurs entées doivent être des nombres (int ou float)
                    
        * Postconditions :
            la valeur est convertie en float       
                      
        
        ==================================================================================================================
    """
    # on convertit l'entrée en float...
    note = float(inptut())
    # ...puis on la renvoie
    return note

def minimum_table(valeurs:list) -> float :
    """ ==================================================================================================================
    
         * Description :
            renvoie le minimum d'une liste d'entier
        
        * Exemple :
            entrée: [30,20,40,10]
            sortie: 10
            
        * Préconditions :
            les valeurs entées doivent être sous forme de liste
                    
        * Postconditions :
            la valeur mini renvoyée par la liste est un float       
               
        
        ==================================================================================================================
    """
    # on définie une valeur minimale tès grande
    mini = 1000
    # pour chaque valeur de la liste, on la compare a mini, si elle est plus petite on met mini a sa valeur
    for i in valeur:
        if i <= mini:
            mini = i
    return mini
    
def maximum_table(valeur :list) -> float :
    """ ==================================================================================================================
    
       * Description :
            renvoie le maximum d'une liste d'entier
        
        * Exemple :
            entrée: [30,20,40,10]
            sortie: 40
            
        * Préconditions :
            les valeurs entées doivent être sous forme de liste
                    
        * Postconditions :
            la valeur maxi renvoyée par la liste est un float   
        
        ==================================================================================================================
    """
     # on définie une valeur maxamale tès petite
    val_max = 0
    # pour chaque valeur de la liste, on la compare a maxi, si elle est plus grande on met maxi a sa valeur
    for i in valeur:
        if i >= maxi:
            maxi = i
    return maxi

def moyenne_table(valeurs:list) -> float :
    """ ==================================================================================================================
    
        * Description :
            renvoie la moyenne d'une liste d'entiers
        
        * Exemple :
            entrée: [30,20,40,10]
            sortie: 25
            
        * Préconditions :
            les valeurs entrées doivent être sous forme de liste
                    
        * Postconditions :
            la valeur moyenne renvoyée par la liste est un float 
        
        ==================================================================================================================
    """
    
    moyenne = 0
    # on additione les valeurs
    for i in valeurs : 
        moyenne += i
    # on divise par le nombre de valeurs pour avoir la moyenne
    moyenne = moyenne/len(valeurs)
    return moyenne

def demander_entier_V2(message : str) -> int :
    """ ==================================================================================================================
    
        * Description : 
            Je demande à l'utilisateur un nombre correspondant à la question du message et renvoie le résultat au format entier ;
                > avec une gestion de vérification de la validité de la saisie utilisateur.
                        
        * Exemple :
            >>> demander_entier("Combien de notes sont à saisir ? ")
            Combien de notes sont à saisir ? 5
            5
                                           
        * Préconditions :
            message (str) : question définissant le nombre à saisir ;
                    
        * Postconditions :
            (int) : la valeur saisie convertie en entier.       
        
        ==================================================================================================================
    """
    # Assertions de vérification des préconditions :
    assert type(message) == str  , "L'argument message doit être une chaine de caractères."
            
    # bloc d'instructions :
    try :
        nombre = int(input(message))
        return nombre
    except ValueError :
        print("La valeur saisie doit être convertible en un nombre entier exprimé en base 10 : \n    -> la saisie ne doit pas contenir d'autres caractères que 0, 1, 2, 3, 4, 5, 6, 7, 8, 9")