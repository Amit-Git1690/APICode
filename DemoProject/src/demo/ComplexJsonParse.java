package demo;

import file.Payloads;
import io.restassured.path.json.JsonPath;

public class ComplexJsonParse 
{
	public static void main(String[] args)
	{
		// TODO Auto-generated method stub
		JsonPath jsobjpath = new JsonPath(Payloads.coursePrice());

		//1. Print No of courses returned by API
		int count = jsobjpath.getInt("courses.size()");
		System.out.println(count);
		
		//2.Print Purchase Amount
		int totalAmount = jsobjpath.getInt("dashboard.purchaseAmount");
		System.out.println(totalAmount);
		
		//3. Print Title of the first course
		 String titleFirstCourse=jsobjpath.get("courses[0].title");
		  System.out.println(titleFirstCourse);
		  
		  //Print All course titles and their respective Prices
		  for(int i=0;i<count;i++)
		  {
			  String courseTitles=jsobjpath.get("courses["+i+"].title");
			  System.out.println(jsobjpath.get("courses["+i+"].price").toString());
			  
			  System.out.println(courseTitles);
			  
		  }
		  //Print no of copies sold by RPA Course
		  
		 System.out.println("Print no of copies sold by RPA Course");
		 
		 for(int i=0;i<count;i++)
		 {
			  String courseTitles=jsobjpath.get("courses["+i+"].title");
			  if(courseTitles.equalsIgnoreCase("RPA"))
			  {
				  int copies=jsobjpath.get("courses["+i+"].copies");
				  System.out.println(copies);
				  break;
			  }
	 }	
	}

}
