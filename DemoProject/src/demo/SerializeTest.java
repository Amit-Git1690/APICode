package demo;

import io.restassured.RestAssured;
import io.restassured.response.Response;
import pojo.AddPlace;
import pojo.LocationPlace;

import static io.restassured.RestAssured.*;

import java.util.ArrayList;
import java.util.List;

//For Serialization Parse json will give we will need write java code and response(payload body) will get

public class SerializeTest 
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

		Response res =given().log().all().queryParam("key", "qaclick123")
				.body(ap)
				.when().post("/maps/api/place/add/json")
				.then().assertThat().statusCode(200).extract().response();
		String responseString = res.asString();
		System.out.println(responseString);



	}

}
