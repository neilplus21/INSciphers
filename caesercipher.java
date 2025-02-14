package caesercipher;

import java.util.Scanner;

public class pprogram {
    public String encrypt(String text, int shift) {
        StringBuilder ciph = new StringBuilder();
        for (int i = 0; i < text.length(); i++) {
            char curr = text.charAt(i);
            if (Character.isUpperCase(curr)) {
                char encryptedChar = (char) ((curr + shift - 'A') % 26 + 'A');
                ciph.append(encryptedChar);
            } else if (Character.isLowerCase(curr)) {
                char encryptedChar = (char) ((curr + shift - 'a') % 26 + 'A'); // Changed 'A' to 'a'
                ciph.append(encryptedChar);
            } else {
                ciph.append(curr);
            }
        }
        return ciph.toString();
    }

    public String decrypt(String ciph, int shift) {
        StringBuilder text = new StringBuilder();

        for (int i = 0; i < ciph.length(); i++) {
            char curr = ciph.charAt(i);
            if (Character.isUpperCase(curr)) {
                char decryptedChar = (char) ((curr - shift - 'A' + 26) % 26 + 'A');
                text.append(decryptedChar);
            } else if (Character.isLowerCase(curr)) {
                char decryptedChar = (char) ((curr - shift - 'a' + 26) % 26 + 'A'); // Changed 'A' to 'a'
                text.append(decryptedChar);
            } else {
                text.append(curr); 
            }
        }
        return text.toString();

    }

    public static void main(String[] args) {
        pprogram caesarCipher = new pprogram();     
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter text:");
        String orig = sc.nextLine();
        System.out.println("Enter shift:");
        int shift = sc.nextInt();
        
        String encyp = caesarCipher.encrypt(orig, shift);
        System.out.println("Encrypted: " + encyp);
        
        String decryp = caesarCipher.decrypt(encyp, shift);
        System.out.println("Decrypted: " + decryp);
        
        sc.close();
    }
}
