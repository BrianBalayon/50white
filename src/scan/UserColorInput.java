package scan;

public class UserColorInput extends InputScanner {
	
	
	
	public UserColorInput() {
	}
	
	@Override
	public void askForInput() {
		System.out.println("Please enter a color as RGB (RRR,GGG,BBB) or Hex (RRGGBB)");;
		super.askForInput();
		if (!checkValidColor());
	}
	
	private chackValidColor

}
