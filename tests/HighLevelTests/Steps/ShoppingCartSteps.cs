using System;
using System.Collections.Generic;
using NUnit.Framework;
using TechTalk.SpecFlow;

namespace HighLevelTests.Steps
{
    [Binding]
    public class ShoppingCartSteps
    {
        private readonly ScenarioContext _scenarioContext;
        private ShoppingCart _cart;

        public ShoppingCartSteps(ScenarioContext scenarioContext)
        {
            _scenarioContext = scenarioContext;
        }

        [Given("a new shopping cart")]
        public void GivenANewShoppingCart()
        {
            _cart = new ShoppingCart();
            _scenarioContext["cart"] = _cart;
        }

        [Given("a new shopping cart with items:")]
        public void GivenANewShoppingCartWithItems(Table table)
        {
            _cart = new ShoppingCart();
            foreach (var row in table.Rows)
            {
                var quantity = int.Parse(row["quantity"]);
                var price = decimal.Parse(row["price"]);
                _cart.AddItem(quantity, price);
            }
            _scenarioContext["cart"] = _cart;
        }

        [When("I add (.*) items with price (.*)")]
        public void WhenIAddItemsWithPrice(int quantity, decimal unitPrice)
        {
            _cart = (ShoppingCart)_scenarioContext["cart"];
            _cart.AddItem(quantity, unitPrice);
        }

        [When("I apply a discount of (.*)%")]
        public void WhenIApplyADiscountOfPercent(int percent)
        {
            _cart = (ShoppingCart)_scenarioContext["cart"];
            _cart.ApplyDiscount(percent);
        }

        [Then("the total should be (.*)")]
        public void ThenTheTotalShouldBe(decimal expected)
        {
            _cart = (ShoppingCart)_scenarioContext["cart"];
            Assert.AreEqual(expected, Math.Round(_cart.Total, 2));
        }
    }

    public class ShoppingCart
    {
        private readonly List<(int Quantity, decimal Price)> _items = new List<(int, decimal)>();
        private decimal _discountPercent;

        public void AddItem(int quantity, decimal price)
        {
            _items.Add((quantity, price));
        }

        public void ApplyDiscount(int percent)
        {
            _discountPercent = percent / 100m;
        }

        public decimal Total
        {
            get
            {
                var total = 0m;
                foreach (var (quantity, price) in _items)
                {
                    total += quantity * price;
                }
                return total * (1 - _discountPercent);
            }
        }
    }
}