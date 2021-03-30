package demos;

public class HelloWorld {

	public static void main(String[] args) 
	{
		// TODO Auto-generated method stub
		System.out.println("Hello World");

	}

}


/*	
		//Get all window handles
		Set<String> allHandles = driver.getWindowHandles();
		//count the handles Here count is=2
		System.out.println("Count of windows:"+allHandles.size()); 
		//Get current handle or default handle
		
		//String currentWindowHandle = driver.getWindowHandle();
		String currentWindowHandle = allHandles.iterator().next();
		System.out.println("currentWindow Handle: " + currentWindowHandle);
		
		//Remove first/default Handle
		boolean rm = allHandles.remove(allHandles.iterator().next());
		System.out.println("-----------" + rm);
		
		//get the last Window Handle
		String lastHandle = allHandles.iterator().next();
		System.out.println("last window handle"+lastHandle);
		
		//switch to second/last window, because we know there are only two windows 1-parent window 2-other window(ad window)
		driver.switchTo().window(lastHandle);
		System.out.println(driver.getTitle());

 */