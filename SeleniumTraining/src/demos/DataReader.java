package demos;

public class DataReader 
{
	public static void main(String[] args) 
	{
		/*String csvFile = "./driver/TestEnvironment/annual-enterprise-survey-2019-financial-year-provisional-size-bands-csv.csv";
		utilites.CSVReaderTest.read(csvFile);
		*/
		readXLS();

	}
	public static void readXLS()
	{
		String filename = "C:\\Users\\Amitava\\eclipse-workspace\\SeleniumTraining\\driver\\TestEnvironment\\UserLogin.xls";
		String[][] data = utilites.Excel.get(filename);
		for(String[] record: data)
		{
			System.out.println("\n New Record:");
			System.out.println(record[0]);
			System.out.println(record[1]);
			System.out.println(record[2]);
		}
	}
	
}

 



