package BDDTest.demo;		


import org.junit.runner.RunWith;

import cucumber.api.CucumberOptions;
import cucumber.api.junit.Cucumber;
//import cucumber.api.CucumberOptions;


@RunWith(Cucumber.class)			
@CucumberOptions(features="Feature",glue={"StepDefinition"})	

public class TestRunner 				
{		

}


