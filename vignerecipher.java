public class vignerecipher {
    static char[][] table = new char[26][26];

    static void createTable() {
        for (int i = 0; i < 26; i++)
            for (int j = 0; j < 26; j++)
                table[i][j] = (char) ('A' + (i + j) % 26);
    }

    static void printTable() {
        System.out.println("Vigenère Table:");
        for (char[] row : table) {
            for (char c : row)
                System.out.print(c + " ");
            System.out.println();
        }
    }

    static String encryptDecrypt(String text, String key, boolean encrypt) {
        StringBuilder result = new StringBuilder();
        key = key.toUpperCase().repeat(text.length() / key.length() + 1);
        for (int i = 0; i < text.length(); i++) {
            char t = Character.toUpperCase(text.charAt(i)), k = key.charAt(i);
            if (Character.isLetter(t))
                result.append(encrypt ? table[t - 'A'][k - 'A'] : (char) ('A' + (t - k + 26) % 26));
            else
                result.append(t);
        }
        return result.toString();
    }

    public static void main(String[] args) {
        createTable();
        printTable();
        String text = "HELLO", key = "KEY";
        String encrypted = encryptDecrypt(text, key, true);
        String decrypted = encryptDecrypt(encrypted, key, false);
        System.out.println("\nPlaintext: " + text);
        System.out.println("Encrypted: " + encrypted);
        System.out.println("Decrypted: " + decrypted);
    }
}
