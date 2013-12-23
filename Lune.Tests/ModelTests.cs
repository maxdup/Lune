using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using Lune;
using System.Collections.Generic;


namespace Lune.Tests
{
    [TestClass]
    public class ModelTests
    {
        [TestMethod]
        public void SongConstruct()
        {
            Song song = new Song("D:\\Music\\01 Take Care Of You.mp3");
            Assert.AreEqual(song.name, "Take Care Of You");
        }
    }
}
