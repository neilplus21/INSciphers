package monoalphabetic;

public class monoalp {
	public void encrypt(String text) {
	char[] ctext = text.toCharArray();
	String letters = "abcdefghijklmnopqrstuvwxyz";
	String mkey =    "qwertyuiopasdfghjklzxcvbnm";
	char[] makey = mkey.toCharArray();
	StringBuilder ciph = new StringBuilder();
	//char[] arr = letters.toCharArray();
	for(int i=0; i<text.length();i++) {
		if(letters.indexOf(ctext[i])>0) {
			ciph.append(makey[letters.indexOf(ctext[i])]);
		}
	 }
	//return ciph.toString();
	System.out.println(ciph.toString());
	}
	public void decrypt(String text) {
		char[] ctext = text.toCharArray();
		String letters = "abcdefghijklmnopqrstuvwxyz";
		char[] cletters = letters.toCharArray();
		String mkey =    "qwertyuiopasdfghjklzxcvbnm";
		char[] makey = mkey.toCharArray();
		StringBuilder decryp = new StringBuilder();
		//char[] arr = letters.toCharArray();
		for(int i=0; i<text.length();i++) {
			if(letters.indexOf(ctext[i])>0) {
				decryp.append(cletters[mkey.indexOf(ctext[i])]);
			}
		 }
		System.out.println(decryp.toString());
		
		
		
	}
	public static void main(String[] args) {
		monoalp m = new monoalp();
		m.encrypt("dingdong");
		m.decrypt("rofurgfu");
		
	}

}
