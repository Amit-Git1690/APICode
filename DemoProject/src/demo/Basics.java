package demo;
import io.restassured.RestAssured;
import io.restassured.path.json.JsonPath;

import static io.restassured.RestAssured.*;
import static org.hamcrest.Matchers.*;

import java.io.IOException;


import org.testng.Assert;

import file.Payloads;

public class Basics 
{
	public static void main(String[] args) throws IOException 
	{
		//Add place -> Update place with new Address -> get place to validate if new address is present in response
		// TODO Auto-generated method stub
		/*Validate if Add place API working as expected
		 Given - all input details
		 When - submit the API
		 Then - validate the response
		 //Content of the file to String -> Content of the file can convert into Byte -> Byte data to String
		 */
		RestAssured.baseURI = "https://rahulshettyacademy.com";
		// Add Place
		String postresponse = given().log().all().queryParam("key", "qaclick123").header("Content-Type","application/json")
					.body(Payloads.addPlace())
				//.body(new String(Files.readAllBytes(Paths.get("C:\\Users\\Amitava\\Desktop\\UdemyJAvABDDAutomation\\API\\AddPlace.json"))))
				.when().post("maps/api/place/add/json")
				.then().log().all().assertThat().statusCode(200)
				.body("scope", equalTo("APP"))
				.header("Server", "Apache/2.4.18 (Ubuntu)").extract().response().asString();

		System.out.println("Output:" +postresponse);

		JsonPath js = new JsonPath(postresponse);   //For parsing Json
		String placeId=js.getString("place_id");
		System.out.println(placeId);


		//Update palce

		String expectedAddress = "70 Summer walk, KA";
		given().log().all().queryParam("key", "qaclick123").header("Content-Type","application/json")
		.body("{\r\n" + 
				"\"place_id\":\""+placeId+"\",\r\n" + 
				"\"address\":\""+expectedAddress+"\",\r\n" + 
				"\"key\":\"qaclick123\"\r\n" + 
				"}\r\n" + 
				"")
		.when().put("maps/api/place/update/json")
		.then().log().all().assertThat().statusCode(200)
		.body("msg", equalTo("Address successfully updated"));

		// Get place
		String getresponse = given().log().all().queryParam("key", "qaclick123").queryParam("place_id", placeId)
				.when().get("maps/api/place/get/json")
				.then().log().all().assertThat().statusCode(200).extract().response().asString();


		JsonPath jsobj = new JsonPath(getresponse);   //For parsing Json
		String actualaddress=jsobj.getString("address");
		System.out.println(actualaddress);
		Assert.assertEquals(actualaddress, expectedAddress);

	}

}
