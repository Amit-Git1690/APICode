package exceldataDriven;

import org.testng.annotations.Test;
import static io.restassured.RestAssured.*;

import java.util.HashMap;

import io.restassured.RestAssured;
import io.restassured.path.json.JsonPath;

public class ExcelDriven 
{
	@Test
	public void addbook()
	{
		HashMap<String, Object> map = new HashMap<String, Object>();
		map.put("name", "Rest Assured");
		map.put("isbn", "gggshjhjhr");
		map.put("aisle", "574jhjfdh");
		map.put("author", "Amrutha");

		/*		//---------------Used of nested HashMap --- 
		HashMap<String, Object> map2 = new HashMap<String, Object>();
		map2.put("lat", "123");
		map2.put("lng", "456"); 
		map2.put("location", map2);
		 */
		RestAssured.baseURI="http://216.10.245.166";
		String resp=
				given()
				.header("Content-Type","application/json")
				.body(map)
				/*				.body("{\r\n" + 
						"\r\n" + 
						"\"name\":\"Learn Appium Automation with Java\",\r\n" + 
						"\"isbn\":\"bcdjjghhg\",\r\n" + 
						"\"aisle\":\"2275jdj4\",\r\n" + 
						"\"author\":\"John foe\"\r\n" + 
						"}\r\n" + 
						" \r\n" + 
						"")
				 */
				.when()
				.post("/Library/Addbook.php")
				.then()
				.extract().response().asString();
		System.out.println(resp);
		JsonPath js=new JsonPath(resp);
		String id=js.getString("ID");
		System.out.println(id);


	}


}
