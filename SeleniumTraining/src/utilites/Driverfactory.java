package utilites;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.ie.InternetExplorerDriver;

public class Driverfactory 
{
	//This method return WebDriver object
	public static WebDriver open(String browserType)
	{
		if(browserType.equalsIgnoreCase("chrome"))
		{
			System.setProperty("webdriver.chrome.driver", "./driver/TestEnvironment/chromedriver.exe");
			return new ChromeDriver();
		}
		else if(browserType.equalsIgnoreCase("firefox"))
		{
			System.setProperty("webdriver.gecko.driver", "./driver/TestEnvironment/geckodriver.exe");
			return new FirefoxDriver();
		}
		else
		{
			System.setProperty("webdriver.chrome.driver", "./driver/TestEnvironment/IEDriverServer.exe");
			return new InternetExplorerDriver();
		}
	}

}
