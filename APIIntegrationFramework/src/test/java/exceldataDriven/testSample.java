package exceldataDriven;

import java.io.IOException;
import java.util.ArrayList;

public class testSample 
{
	public static void main(String[] args) throws IOException
	{
		DataDriven data = new DataDriven();
		ArrayList<String> d = data.getData("Login");
		System.out.println(d.get(0));
		System.out.println(d.get(1));
		System.out.println(d.get(2));
		System.out.println(d.get(3));


	}

}
