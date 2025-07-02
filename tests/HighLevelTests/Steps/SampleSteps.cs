using NUnit.Framework;
using TechTalk.SpecFlow;

namespace HighLevelTests.Steps
{
    [Binding]
    public class SampleSteps
    {
        private int _value;

        [Given(@"a value (.*)")]
        public void GivenAValue(int value)
        {
            _value = value;
        }

        [When(@"I increment the value by (.*)")]
        public void WhenIIncrementTheValueBy(int increment)
        {
            _value += increment;
        }

        [Then(@"the value should be (.*)")]
        public void ThenTheValueShouldBe(int expected)
        {
            Assert.AreEqual(expected, _value);
        }
    }
}