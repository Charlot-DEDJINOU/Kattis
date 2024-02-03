import base64

def est_base64(chaine):
    try:
        # Décode la chaîne en base64
        base64.b64decode(chaine)
        # Si aucune exception n'est levée, la chaîne est probablement en base64
        return True
    except:
        return False

chaine_test = "cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9"
if est_base64(chaine_test):
    print("La chaîne est encodée en base64.")
else:
    print("La chaîne n'est pas encodée en base64.")
