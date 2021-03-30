package tests;

import java.util.List;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.Parameterized;
import org.junit.runners.Parameterized.Parameters;

@RunWith(value = Parameterized.class)
public class NewAccountDDT 
{
//	String year;
	String industry_code_ANZSIC;
	String industry_name_ANZSIC;
	// This is our test method
	@Test
	public void newAccountTest()
	{
		System.out.println("New Record: "  +" " + industry_code_ANZSIC + " " + industry_name_ANZSIC);
	}
	
	//This annotated method is design to pass parameters into the class via constructor 
	@Parameters
	public static List<String[]> getData()
	{
		return utilites.CSVReaderTest.read("./driver/TestEnvironment/annual-enterprise-survey-2019-financial-year-provisional-size-bands-csv.csv");

	}

	//Constructor that passes parameters to the test method
	public NewAccountDDT(String industry_code_ANZSIC,String industry_name_ANZSIC)
	{
//		this.year = year;
		this.industry_code_ANZSIC = industry_code_ANZSIC;
		this.industry_name_ANZSIC = industry_name_ANZSIC;

	}


}
