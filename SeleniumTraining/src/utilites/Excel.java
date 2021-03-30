package utilites;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import org.apache.poi.hssf.usermodel.HSSFCell;
import org.apache.poi.hssf.usermodel.HSSFRow;
import org.apache.poi.hssf.usermodel.HSSFSheet;
import org.apache.poi.hssf.usermodel.HSSFWorkbook;

public class Excel 
{
	//Dependencies: POI | HSSF Workbook/Sheet/Row/cell
	//This method will read and return Excel data into double array
	public static String[][] get(String filename)
	{
		String[][] dataTable = null;
		File file = new File(filename);
		//Create file input stream to read Workbook and Worksheet
		try 
		{
			FileInputStream xlfile = new FileInputStream(file);
			HSSFWorkbook xlwb = new HSSFWorkbook();
			HSSFSheet xlsheet = xlwb.getSheet("UserAccounts");
			
			//Get the number of rows and columns
			int numRows = xlsheet.getLastRowNum() + 1;
			int numcols = xlsheet.getRow(0).getLastCellNum();
			
			//Create double array data table = rows * cols
			//we will return this data table
			
			dataTable = new String[numRows][numcols];
			
			//For each row, create a HSSFRow, then Iterate through the "columns"
			//For each "column" create an HSSFcell to grab the value at the specified cell(1,1)
			
			for(int i =0; i<numRows; i++)
			{
				HSSFRow xlRow = xlsheet.getRow(i);
				for(int j=0; j<numcols; j++)
				{
					HSSFCell xlcell = xlRow.getCell(j);
					dataTable[i][j] = xlcell.toString();
							
				}
			}
		} 
		catch (Exception e) 
		{
			// TODO Auto-generated catch block
			System.out.println("ERROR FILE HANDLING " +e.toString());
		}
		
		return dataTable;
		
	}

}
