package alpha;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

public class Demo 
{
	/*ERROR StatusLogger No log4j2 configuration file found. Using default configuration: 
		for that error and fatal statement will be display to the console.
	*/
	private static Logger log = LogManager.getLogger(Demo.class.getName());
	public static void main(String[] args)
	{
		log.debug("I have clicked on button");
		if(5>4)
		{
			log.info("Button is displayed");
		log.error("Button is not displayed");
		log.fatal("Button is missing");
		}


	}

}
