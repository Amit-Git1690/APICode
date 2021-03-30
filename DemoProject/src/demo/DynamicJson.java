package demo;

import org.testng.annotations.DataProvider;
import org.testng.annotations.Test;

import file.Payloads;
import io.restassured.RestAssured;
import io.restassured.path.json.JsonPath;

import static io.restassured.RestAssured.*;
public class DynamicJson 
{
	@Test(dataProvider = "BooksData")
	public void addbook(String isbn, String aisle) 
	{
		RestAssured.baseURI = "http://216.10.245.166";
		String postresponse = given().log().all().header("Content-Type","application/json").body(Payloads.addBook(isbn,aisle))
				.when().post("Library/Addbook.php")
				.then().log().all().assertThat().statusCode(200).extract().response().asString();

		JsonPath js = new JsonPath(postresponse);   //For parsing Json
		String id=js.getString("ID");
		System.out.println(id);

	}
	@DataProvider(name ="BooksData")
	public Object[][] getData()
	{
		//Array: collection of elements
		//Multidimensional Array: collection of arrays
		return new Object[][] {{"ojfhgty","69h69"},{"cwggwt","1gu236"},{"knbvjag","15h478"}};
	}
}