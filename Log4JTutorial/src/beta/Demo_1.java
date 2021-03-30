package beta;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

public class Demo_1 
{
	/*ERROR StatusLogger No log4j2 configuration file found. Using default configuration: 
		for that error and fatal statement will be display to the console.
	*/
	private static Logger log = LogManager.getLogger(Demo_1.class.getName());
	public static void main(String[] args)
	{
		log.debug("I am debugging");
		if(5>4)
		{
			log.info("Object is present");
		log.error("Object is not present");
		log.fatal("This is fatal");
		}


	}

}
