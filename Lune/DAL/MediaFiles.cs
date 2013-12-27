using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lune
{
    //lots of borked code
    class MediaFiles
    {
        Library lib;
        public MediaFiles(Library lib)
        {
            this.lib = lib;
        }
        public int scrapper(string searchDir)
        {
            int SongCount = 0; //file count
            try
            {
                foreach (string f in Directory.GetFiles(searchDir)) //checks for files
                {
                    try
                    {
                        if (f.EndsWith(".mp3")) //todo: update this condition later on
                        {
                            
                            Song thisSong = new Song(f); //this song http://www.youtube.com/watch?v=XxlhECbIW4g

                            var existingAlbum = lib.GetAlbums().Where(x => x.name == thisSong.album.name).ToList();
                            if (existingAlbum.Count > 0)
                            {
                                thisSong.album = existingAlbum.ElementAt(0);
                            }
                            else
                            {
                                var existingArtist = lib.GetArtists().Where(x => x.getName() == thisSong.ArtistName).ToList();
                                if (existingArtist.Count > 0)
                                {
                                    thisSong.artist = existingArtist.ElementAt(0);
                                }
                                else
                                {
                                    lib.Add(thisSong.artist);
                                }
                                
                                lib.Add(thisSong.album);
                            }
                            lib.Add(thisSong);
                            SongCount++;
                        }
                    }
                    catch (Exception e){}
                }
                foreach (string d in System.IO.Directory.GetDirectories(searchDir)) //checks for subdirectories
                {
                    SongCount += scrapper(d);
                }
            }
            catch (System.Exception excpt)
            {
                return 0;
            }
            return SongCount;
        }
    }
}
