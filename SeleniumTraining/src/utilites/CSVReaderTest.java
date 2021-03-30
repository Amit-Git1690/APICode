package utilites;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.List;


public class CSVReaderTest 
{
	public static List<String[]> read(String csvFile) 
	{
		List<String[]> data = new ArrayList<String[]>();
		String testRow;
		try 
		{
			File file = new File(csvFile);
			FileReader fr = new FileReader(file);
			BufferedReader br = new BufferedReader(fr);
			while((testRow = br.readLine()) != null)
			{
				String[] line = testRow.split(",");
				data.add(line);
			}
		}
		catch(Exception e) 
		{
			System.out.println("Could raed the file or file not found" + csvFile);
		}
		return data;
	}

}

