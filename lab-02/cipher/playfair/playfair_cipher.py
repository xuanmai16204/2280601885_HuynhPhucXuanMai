class PlayFairCipher:
    def __init__(self):
        pass

    def create_playfair_matrix(self, key):
        key = key.replace("J", "I").upper()
        key_set = set(key)
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        matrix = list(key) + [letter for letter in alphabet if letter not in key_set]

        playfair_matrix = [matrix[i:i+5] for i in range(0, 25, 5)]
        return playfair_matrix

    def find_letter_coords(self, matrix, letter):
        for row in range(5):
            for col in range(5):
                if matrix[row][col] == letter:
                    return row, col
        return None, None

    def playfair_encrypt(self, plaintext, matrix):
        plaintext = plaintext.replace("J", "I").upper()
        encrypted_text = ""
        pairs = [plaintext[i:i+2] for i in range(0, len(plaintext), 2)]
        
        for pair in pairs:
            if len(pair) < 2:
                pair += "X"

            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])

            if row1 is None or row2 is None or col1 is None or col2 is None:
                raise ValueError(f"Invalid character in input: {pair}")

            if row1 == row2:
                encrypted_text += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                encrypted_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
            else:
                encrypted_text += matrix[row1][col2] + matrix[row2][col1]
        
        return encrypted_text

    def playfair_decrypt(self, ciphertext, matrix):
        decrypted_text = ""
        pairs = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]

        for pair in pairs:
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])

            if row1 is None or row2 is None or col1 is None or col2 is None:
                raise ValueError(f"Invalid character in input: {pair}")

            if row1 == row2:
                decrypted_text += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:
                decrypted_text += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
            else:
                decrypted_text += matrix[row1][col2] + matrix[row2][col1]

        return decrypted_text.rstrip("X")
