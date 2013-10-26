using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using Lune;

namespace Lune.Tests
{
    [TestClass]
    public class UnitTest1
    {
        Database dbTest = new Database();

        [TestMethod]
        public void DatabaseInit()
        {
            dbTest.DbInit();
        }

        [TestMethod]
        public void InsertArtist()
        {
            Artist art1 = new Artist("bobby");
            Artist art2 = new Artist("tom");
            Artist art3 = new Artist("jon");
            dbTest.addArtist(art1);
            dbTest.addArtist(art2);
            dbTest.addArtist(art3);
            Assert.AreEqual(3, dbTest.getArtists().Count);
        }
    }
}
