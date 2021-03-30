package demos;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class Login {

	public static void main(String[] args) throws Exception
	{


		// 1. Define the web browser
		System.setProperty("webdriver.chrome.driver", "./driver/TestEnvironment/chromedriver.exe");
		WebDriver driver = new ChromeDriver();

		// 2.Navigate to the web browser
		driver.get("https://www.j2store.org/");
		driver.manage().window().maximize();

		/* find Elements: Locate the element, Determine/Decide the action, Pass any parameters */

		//3.Click on Login button
		driver.findElement(By.xpath("//*[contains(text(),'Login')]")).click();
		System.out.println("Clicked on Login button");


		//4.Enter Create account details
		driver.findElement(By.xpath("//*[contains(text(),'have an account?')]")).click();


		driver.findElement(By.xpath("(//*[contains(@id,'jform_name')]//following::input[1])[1]")).sendKeys("Amita Roy");
		driver.findElement(By.xpath("(//*[contains(@id,'jform_username')]//following::input[1])[1]")).sendKeys("roy@email.com");
		
		driver.findElement(By.xpath("(//*[contains(@id,'jform_password1')]//following::input[1])[1]")).sendKeys("Amit@2001");
		driver.findElement(By.xpath("(//*[contains(@id,'jform_password2')]//following::input[1])[1]")).sendKeys("Amit@2001");
		
		
		driver.findElement(By.xpath("(//*[contains(@id,'jform_email1')]//following::input[1])[1]")).sendKeys("roy@email.com");
		driver.findElement(By.xpath("(//*[contains(@id,'jform_email2')]//following::input[1])[1]")).sendKeys("roy@email.com");
		

		

		// 5.Click on Sign-Up button
		driver.findElement(By.xpath("(//*[contains(@id,'recaptcha-anchor')])[1]")).click();
		driver.findElement(By.xpath("(//*[contains(text(),'Register')])[1]")).click();
		
		//6. Get Confirmation
		System.out.println("-----------------------");
		int size = driver.findElements(By.tagName("iframe")).size();
		System.out.println(size);
		driver.switchTo().frame(0);
		System.out.println("----------------");
		Thread.sleep(5);
		
		System.out.println("------------------");
		WebElement chkbox =driver.findElement(By.xpath("//input[@value='Login']"));
		for(int i=0; i<2;i++) 
		{
			chkbox.click();
			System.out.println("Checkbox status is: " + chkbox.isSelected());
		}
		System.out.println("----------------");
		
		//7.Click on Complete Registration button
		driver.findElement(By.xpath("//*[contains(text(),'Complete Registration')]")).click();
		driver.switchTo().defaultContent();
		//8.Close the browser
		//driver.quit();


	}

}
