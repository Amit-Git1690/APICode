package demo;

import io.restassured.RestAssured;
import io.restassured.builder.RequestSpecBuilder;
import io.restassured.builder.ResponseSpecBuilder;
import io.restassured.http.ContentType;
import io.restassured.response.Response;
import io.restassured.specification.RequestSpecification;
import io.restassured.specification.ResponseSpecification;
import pojo.AddPlace;
import pojo.LocationPlace;

import static io.restassured.RestAssured.*;

import java.util.ArrayList;
import java.util.List;

//For Serialization Parse json will give we will need write java code and response(payload body) will get

public class SpecBuilderTest 
{

	public static void main(String[] args) 
	{
		// TODO Auto-generated method stub
		RestAssured.baseURI = "https://rahulshettyacademy.com";

		AddPlace ap = new AddPlace();
		ap.setAccuracy(50);
		ap.setAddress("29, side layout, cohen 09");
		ap.setLanguage("French-IN");
		ap.setName("Frontline house");
		ap.setPhone_number("(+91) 983 893 3937");
		ap.setWebsite("http://google.com");
		List<String> myList = new ArrayList<String>();
		myList.add("shoe park");
		myList.add("shop");
		ap.setTypes(myList);

		LocationPlace l = new LocationPlace();
		l.setLat(-38.383494);
		l.setLng( 33.427362);
		ap.setLocation(l);

		RequestSpecification req = new RequestSpecBuilder().setBaseUri("https://rahulshettyacademy.com").addQueryParam("key", "qaclick123").setContentType(ContentType.JSON).build();

		ResponseSpecification res =new ResponseSpecBuilder().expectStatusCode(200).expectContentType(ContentType.JSON).build();
		
		RequestSpecification request =given().spec(req).body(ap); //request 
		
		Response respose =request.when().post("/maps/api/place/add/json")  //sending
				
		.then().spec(res).extract().response(); //got back
		
		String responseString = respose.asString();
		System.out.println(responseString);



	}

}
