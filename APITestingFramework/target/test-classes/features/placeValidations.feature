Feature: validating Place API's
@AddPlace @Regression
Scenario Outline: verify if place is being successfully added using AddPlaceAPI
	Given add place payload with "<name>" "<language>" "<address>"
	When user call "addPlaceAPI" with "POST" http request
	Then the API call got success with status code 200
	And "status" is response body is "OK"
	And "scope" is response body is "APP"
	And verify placeId created maps to "<name>" using "getPlaceAPI"
	
Examples:
		|name	 |language	|address		   |
		|Amitava |English   |World cross center|	
	#	|Amrutha |Spanish   |Sea cross center|
	
@DeletePlace @Regression
Scenario: Verify if DeletePlace functionality is working
	Given DeletePlace payload
	When user call "deletePlaceAPI" with "POST" http request
	Then the API call got success with status code 200
	And "status" is response body is "OK"
	
