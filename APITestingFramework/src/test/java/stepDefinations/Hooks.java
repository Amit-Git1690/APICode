package stepDefinations;

import java.io.IOException;

import io.cucumber.java.Before;

public class Hooks
{
	@Before("@DeletePlace")
	public void beforeScenario() throws IOException
	{
		//Execute this code when place id is null
		//write a code that will give you place id

		if(StepDefination.place_id==null)
		{
			StepDefination m = new StepDefination();
			m.add_place_payload_with("Rahit", "French", "Asia");
			m.user_call_with_http_request("addPlaceAPI", "POST");
			m.verify_place_id_created_maps_to_using("Rahit", "getPlaceAPI");
		}
	}
}
