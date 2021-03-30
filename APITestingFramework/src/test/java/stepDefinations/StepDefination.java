package stepDefinations;

import static io.restassured.RestAssured.given;
import static org.junit.Assert.*;
import java.io.IOException;
import io.cucumber.java.en.*;
import io.restassured.builder.ResponseSpecBuilder;
import io.restassured.http.ContentType;
import io.restassured.response.Response;
import io.restassured.specification.RequestSpecification;
import io.restassured.specification.ResponseSpecification;
import resources.APIResources;
import resources.TestDataBuild;
import resources.Utils;

public class StepDefination extends Utils
{
	ResponseSpecification res;
	Response response;
	RequestSpecification request;
	static String place_id;
	TestDataBuild td = new TestDataBuild();

	@Given("add place payload with {string} {string} {string}")
	public void add_place_payload_with(String name, String language, String address) throws IOException 
	{
		request =given().spec(requestSpecification()).body(td.addPlacepayload(name,language,address)); //request 
	}

	@When("user call {string} with {string} http request")
	public void user_call_with_http_request(String resource, String method) 
	{
		APIResources resourceAPI = APIResources.valueOf(resource);
		System.out.println(resourceAPI.getResource());

		res =new ResponseSpecBuilder().expectStatusCode(200).expectContentType(ContentType.JSON).build();

		if(method.equalsIgnoreCase("POST"))
		{
			response =request.when().post(resourceAPI.getResource())  ;
		}
		else if(method.equalsIgnoreCase("GET"))
		{
			response =request.when().get(resourceAPI.getResource());
		}
	}

	@Then("the API call got success with status code {int}")
	public void the_api_call_got_success_with_status_code(Integer int1)
	{
		assertEquals(response.getStatusCode(),200);
	}

	@Then("{string} is response body is {string}")
	public void is_response_body_is(String keyValue, String expectedvalue) 
	{
		assertEquals(getJsonPath(response,keyValue), expectedvalue);
	}

	@Then("verify placeId created maps to {string} using {string}")
	public void verify_place_id_created_maps_to_using(String expectedName, String resource) throws IOException 
	{
		place_id = getJsonPath(response, "place_id");
		request =given().spec(requestSpecification()).queryParam("place_id", place_id);
		user_call_with_http_request(resource,"GET");
		String actualName = getJsonPath(response, "name");
		assertEquals(actualName, expectedName);
	}

	@Given("DeletePlace payload")
	public void delete_place_payload() throws IOException 
	{
		request = given().spec(requestSpecification()).body(td.deletePlacePayload(place_id));
	}


}
