# On insère notre alphabet
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"

# On demande à l'utilisateur d'entrer un message
message_a_crypter = input("Entrer votre message : ")

# On met notre message en majuscules
message_a_crypter = message_a_crypter.upper()

# On demande à l'utilisateur d'entrer une clé
votre_cle = input("Entrer un mot en guise de clé :")

# On met notre clé en majuscules
votre_cle = votre_cle.upper()

# On veut vérifier la longueur de notre clé
def verifier_cle(cle):
    
    if len(message_a_crypter) == len(cle):
       return cle

    else:
        i = 0
        while len(message_a_crypter) != len(cle):
            cle = cle + cle[i]
            i = i + 1
        return cle

nouvelle_cle = verifier_cle(votre_cle)
print("Votre clé est", nouvelle_cle)

"""---------------------------------------------------------------PHASE DE CRYPTAGE------------------------------------------------------------"""
# On veut crypter notre message à partir d'une clé
def crypter_message(message, cle):

    message_crypte = ""
    i = 0
    for caractere in cle:

        # On récupère le numéro de position de chaque caractère composant la clé
        num_position_caractere_cle = alphabet.find(caractere)

        # On récupère le numéro de position de chaque caractère composant le message
        num_position_caractere_message =  alphabet.find(message[i])

        # On additionne les numéros de position
        nv_num_position = num_position_caractere_cle + num_position_caractere_message

        # On veut récupérer le correpondant crypté
        lettre_cryptee =  alphabet[nv_num_position]
        message_crypte = message_crypte + lettre_cryptee

        i = i+1

    # On récupère notre message en entier à la sortie de la boucle
    return message_crypte

#On récupère notre message décrypté en entier et on l'affiche
message_crypte = crypter_message(message_a_crypter,nouvelle_cle)
print("Votre message :", message_a_crypter, "a été crypté de la façon suivante :", message_crypte)

"""---------------------------------------------------------------PHASE DE DECRYPTAGE------------------------------------------------------------"""
# On veut crypter notre message à partir d'une clé
def decrypter_message(message, cle):

    message_decrypte = ""
    i = 0
    for caractere in cle:

        # On récupère le numéro de position de chaque caractère composant la clé
        num_position_caractere_cle = alphabet.find(caractere)

        # On récupère le numéro de position de chaque caractère composant le message
        num_position_caractere_message =  alphabet.find(message[i])

        # On soustrait les numéros de position
        nv_num_position = num_position_caractere_message - num_position_caractere_cle

        # On veut récupérer le correpondant crypté
        lettre_cryptee =  alphabet[nv_num_position]
        message_decrypte = message_decrypte + lettre_cryptee

        i = i+1

    # On récupère notre message en entier à la sortie de la boucle
    return message_decrypte

#On récupère notre message décrypté en entier et on l'affiche
message_decrypte = decrypter_message(message_crypte, nouvelle_cle)
print("Votre message :", message_crypte, "a été décrypté de la façon suivante :", message_decrypte)