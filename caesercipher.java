package inslabexam;

public class CaeserCipher {
	public static void encrypt(String text, int shift) {
		StringBuilder ciph = new StringBuilder();
		for(int i = 0; i<text.length(); i++) {
			char curr = Character.toUpperCase(text.charAt(i));
			char encryptedchar = (char) ((curr + shift - 'A')%26 + 'A');
			ciph.append(encryptedchar);
		}
		System.out.println(ciph.toString());
	}
	
	public static void decrypt(String text, int shift) {
		StringBuilder deciph = new StringBuilder();
		for(int i = 0; i<text.length(); i++) {
			char curr = Character.toUpperCase(text.charAt(i));
			char decryptedchar = (char) ((curr - shift - 'A' + 26)%26 + 'A');
			deciph.append(decryptedchar);
		}
		System.out.println(deciph.toString());
	}
	
	public static void main(String[] args) {
		encrypt("MEOW", 7);
		decrypt("tlvd", 7);
	}

}
