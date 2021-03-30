package tests;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

public class Expedia
{
	WebDriver driver;
	String browserType = "chrome";
	String city = "New York";
	String checkIn = "27 Feb 2021";
	String chkOut = "24 Mar 2021";
	
	@Test
	public void hotelReservation() throws InterruptedException
	{
		//1. Search
		
		 driver.findElement(By.xpath("//*[contains(@aria-label,'Going to')]")).click();
		 driver.findElement(By.id("location-field-destination")).sendKeys(city);
		 System.out.println("City was selected: " + city);
		 Thread.sleep(3);
		 
		 driver.findElement(By.xpath("//*[contains(@id,'d1-btn')]")).click();
		 System.out.println("---------------");
		 driver.findElement(By.xpath("//*[@id=\"wizard-hotel-pwa-v2-1\"]/div[1]/div[2]/div/div/div/div[1]/div/div[2]/div/"
		 		+ "div[2]/div[2]/div[1]/table/tbody/tr[4]/td[7]/button")).sendKeys(checkIn);
		 System.out.println(" CheckIn Date: " +checkIn);
		 Thread.sleep(3);
		 driver.findElement(By.xpath("//*[@id=\"wizard-hotel-pwa-v2-1\"]/div[1]/div[2]/div/div/div/div[1]/div/div[2]/div/div[3]/button/span")).click();
		 
		 System.out.println("---------------");
		 driver.findElement(By.xpath("//*[contains(@id,'d2-btn')]")).click();
		 Thread.sleep(3);
		 driver.findElement(By.xpath("//*[@id=\"wizard-hotel-pwa-v2-1\"]/div[1]/div[2]/div/div/div/div[1]/div/div[2]"
		 		+ "/div/div[2]/div[2]/div[2]/table/tbody/tr[4]/td[4]/button")).sendKeys(chkOut);
		 System.out.println(" CheckOut Date: " +chkOut);
		 driver.findElement(By.xpath("//*[@id=\"wizard-hotel-pwa-v2-1\"]/div[1]/div[2]/div/div/div/div[1]/div/div[2]/div/div[3]/button/span")).click();

		//2. Modify the search results page, give criteria

		//3. Analyze the results and make our selection

		//4. Book reservation

		//5. Fill out contact / billing

		//Get confirmation
	}
	@Before
	public void setUp()
	{
		driver = utilites.Driverfactory.open(browserType);
		driver.get("https://www.expedia.co.in/");

	}
	@After
	public void tearDown()
	{
		//driver.quit();

	}


}
