using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using Lune;

namespace Lune.Tests
{
    [TestClass]
    public class UnitTest1
    {
        [TestMethod]
        public void TestMethod1()
        {
            Database b = new Database();
            Assert.AreEqual(1, 1);
        }
    }
}
