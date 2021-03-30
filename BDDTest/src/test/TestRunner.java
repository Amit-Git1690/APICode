package test;		


import cucumber.api.CucumberOptions;
import cucumber.runtime.model.CucumberExamples;


@RunWith(Cucumber.class)				
@CucumberOptions(Features="demologin",glue={"StepDefinition"})						
public class TestRunner 				
{		

}






