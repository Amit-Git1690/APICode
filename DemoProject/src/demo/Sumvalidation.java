package demo;

import org.testng.Assert;
import org.testng.annotations.Test;

import file.Payloads;
import io.restassured.path.json.JsonPath;

public class Sumvalidation 
{
	@Test
	public void sumOfCourse()
	{
		int sum =0;
		JsonPath jsobjpath = new JsonPath(Payloads.coursePrice());
		int count = jsobjpath.getInt("courses.size()");
	//	System.out.println(count);
		for(int i =0; i<count; i++)
		{
			int price = jsobjpath.get("courses["+i+"].price");
			int copies = jsobjpath.get("courses["+i+"].copies");
			int amount = price * copies;
			System.out.println(amount);
			sum = sum + amount; 
		}
		System.out.println(sum);
		int purchaseAmount =jsobjpath.getInt("dashboard.purchaseAmount");
		Assert.assertEquals(sum, purchaseAmount);
	}
	
}
