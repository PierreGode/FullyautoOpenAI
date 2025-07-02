using System;
using TechTalk.SpecFlow;

namespace HighLevelTests.Steps
{
    [Binding]
    public class Hooks
    {
        private readonly ScenarioContext _scenarioContext;

        public Hooks(ScenarioContext scenarioContext)
        {
            _scenarioContext = scenarioContext;
        }

        [BeforeScenario("@advanced")]
        public void BeforeAdvancedScenario()
        {
            Console.WriteLine($"Starting advanced scenario: {_scenarioContext.ScenarioInfo.Title}");
        }

        [AfterScenario]
        public void AfterScenario()
        {
            Console.WriteLine($"Finished scenario: {_scenarioContext.ScenarioInfo.Title}");
        }
    }
}