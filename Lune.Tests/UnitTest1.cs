using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using Lune;
using System.Collections.Generic;

namespace Lune.Tests
{
    [TestClass]
    public class UnitTest1
    {
        Database dbTest = new Database();
        Library lib = new Library();
        [TestMethod]
        public void DatabaseInit()
        {
            dbTest.DbInit();
        }

        [TestMethod]
        public void InsertArtists()
        {
            List<Artist> liArt = new List<Artist>();

            liArt.Add(new Artist("bobby"));
            liArt.Add(new Artist("tom"));
            liArt.Add(new Artist("jon"));

            foreach (Artist art in liArt){
                dbTest.addArtist(art);
            }

            Assert.AreEqual(3, dbTest.getArtists().Count);
        }
        [TestMethod]
        public void InsertLabels()
        {
            List<Label> liLab = new List<Label>();

            liLab.Add(new Label("v records"));
            liLab.Add(new Label("b records"));

            foreach (Label lab in liLab)
            {
                dbTest.addLabel(lab);
            }

            Assert.AreEqual(2, dbTest.getLabels().Count);
        }
        [TestMethod]
        public void InsertAlbums()
        {
            List<Album> liAlb = new List<Album>();

            liAlb.Add(new Album("some album"));
            liAlb.Add(new Album("some other album"));
            liAlb.Add(new Album("an other album"));
            liAlb.Add(new Album("yet an other album"));

            foreach (Album alb in liAlb)
            {
                lib.Add(alb);
                dbTest.addAlbum(alb);
            }
            Assert.AreEqual(4, lib.GetAlbums().Count);
            Assert.AreEqual(4, dbTest.getAlbums().Count);
        }
        public void InsertSong()
        {
            List<Song> liSong = new List<Song>();

            liSong.Add(new Song("hello world"));
            liSong.Add(new Song("2"));
            liSong.Add(new Song("3"));
            liSong.Add(new Song("4"));
            liSong.Add(new Song("bongo song"));

            foreach (Song song in liSong)
            {
                lib.Add(song);
                dbTest.addSong(song);
            }
            Assert.AreEqual(5 ,lib.GetSongs().Count);
            Assert.AreEqual(5, dbTest.getAlbums().Count);
        }
    }
}
