def vigenere_encrypt(text, key):
    encrypted_text = ""  # Variable zum Speichern des verschlüsselten Textes
    key_index = 0   # Index für den Schlüssel
    for char in text: # Schleife für jeden Buchstaben im Text
        if char.isalpha(): # Überprüfen, ob der an gegebener wert ein Buchstabe ist
            shift = ord(key[key_index]) - 97    # Berechnen des Shift-Werts basierend auf dem Schlüssel
            shifted_char = chr((ord(char) - 97 + shift) % 26 + 97) #Verschieben des Buchstabens um den Shift-Wert
            encrypted_text += shifted_char # Verschlüsselte Buchstaben einzeln hinzufügen
            key_index = (key_index + 1) % len(key)  # Schlüsselindex aktualisieren 
    return encrypted_text #den verschlüsselten Text zurückgeben


encrypted_text = vigenere_encrypt("hallo", "key") #"hallo" verschlüsseln mit dem Schlüssel "key" 
print(f"Verschlüsselter Text: {encrypted_text}") #verschlüsselten Text ausgeben



def vigenere_decrypt(text, key):
    decrypted_text = ""
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('a')
            shifted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a')) #Entschlüsselung
            decrypted_text += shifted_char
            key_index = (key_index + 1) % len(key)
        else:
            decrypted_text += char
    return decrypted_text

encrypted_text = "rejvs"
key = "key"
decrypted_text = vigenere_decrypt(encrypted_text, key)
print(f"Entschlüsselter Text: {decrypted_text}")