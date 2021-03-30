package smoketests;

import org.junit.After;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;
import org.openqa.selenium.WebDriver;

public class PageTitleJunit 
{
	WebDriver driver;
	String webURL = "https://www.wix.com/";
	
	@Test
	public void pageTitleTest()
	{
		// Declare varible and objects at CLASS in order to access in multiple method through program
		System.out.println("Running the Test");
		driver.get(webURL);
		String actualTitle = driver.getTitle();
		String expTitle = "Free Website Builder | Create a Free Website | Wix.com";
		Assert.assertEquals(expTitle, actualTitle);
//		Assert.fail("We Intentionally Fail the Test cases");
		System.out.println("Closing the Test");
	}
	@Before
	public void setUp()
	{
		System.out.println("Setting up the test");
		System.out.println("Initializing the driver");
		driver = utilites.Driverfactory.open("chrome");
	}
	@After
	public void teardown()
	{
		System.out.println("Closing the driver");
		driver.close();
	}
}
