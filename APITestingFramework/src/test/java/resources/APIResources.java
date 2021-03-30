package resources;
// enum is special class in java which has collection of constant or method

public enum APIResources 
{
	addPlaceAPI("maps/api/place/add/json"),
	getPlaceAPI("maps/api/place/get/json"),
	deletePlaceAPI("maps/api/place/delete/json");

	private String resource;

	APIResources(String resource)
	{
		this.resource=resource;
	}

	public String getResource()
	{
		return resource;
	}
}
