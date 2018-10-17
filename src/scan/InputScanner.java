package scan;

import java.util.Scanner;

abstract public class InputScanner {
	
	private String _entered;
	
	public void askForInput() {
		Scanner ask = new Scanner(System.in);
		_entered = ask.nextLine();
		ask.close();
	}
	
	public String getEntered() {
		return _entered;
	}
	
}
