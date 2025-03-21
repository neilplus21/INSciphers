package inslabexam;

public class MonoalphabeticCipher {
	public static void encrypt (String text) {
		String letters = "abcdefghijklmnopqrstuvwxyz";
		String key = 	 "qwertyuiopasdfghjklzxcvbnm";
		char [] mkey = key.toCharArray();
		StringBuilder ciph = new StringBuilder();
		for(int i = 0; i<text.length(); i++) {
			if(letters.indexOf(text.charAt(i))>0) {
				ciph.append(mkey[letters.indexOf(text.charAt(i))]);
			}
		}
		System.out.println(ciph.toString());
		
	}
	public static void decrypt(String text) {
		String letters = "abcdefghijklmnopqrstuvwxyz";
		String key = 	 "qwertyuiopasdfghjklzxcvbnm";
		char [] cletters = letters.toCharArray();
		char [] mkey = key.toCharArray();
		StringBuilder ciph = new StringBuilder();
		for(int i = 0; i<text.length(); i++) {
			if(letters.indexOf(text.charAt(i))>0) {
				ciph.append(cletters[key.indexOf(text.charAt(i))]);
			}
		}
		System.out.println(ciph.toString());
		
	}
	public static void main(String[] args) {
		encrypt("meow");
		decrypt("dtgv");
	}

}
