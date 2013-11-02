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
        public int scrapper(string sDir)
        {
            int i = 0; //file count
            try
            {
                foreach (string d in System.IO.Directory.GetDirectories(sDir))
                {
                    foreach (string f in Directory.GetFiles(d))
                    {
                        try
                        {
                            if (f.EndsWith(".mp3")) //todo: update this condition later on
                            {
                                lib.Add(new Song(f));
                                i++;
                            }
                        }
                        catch (Exception e)
                        {
                        }
                    }
                    i += scrapper(d);
                }
            }
            catch (System.Exception excpt)
            {
                return 0;
            }
            return i;
        }
    }
}
