using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace Lune.Tests
{
    [TestClass]
    public class ModelTests
    {
        [TestMethod]
        public void SongConstruct()
        {
            Song song = new Song("D:\\Music\\01 Take Care Of You.mp3");
            Assert.AreEqual(song.getName(), "Take Care Of You");
        }
    }
}
