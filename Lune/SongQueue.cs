using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using NAudio;

namespace Lune
{   
    /*this class will typically be used as the "now playing" queue
     * (it's mostly a wrapper class for a linkedlist)
     * TODO: add constructors
     * later on: implement a playlist feature from here?
     * */
    class SongQueue
    {
        private LinkedList<Song> queue;
        private LinkedListNode<Song> _current;
        public SongQueue()
        {
            queue = new LinkedList<Song>();
            //for tests, you can declare new songs in this constructor. example:
            //Add(new Song("C:/example.mp3"));
        }
        public bool IsEmpty()
        {
            if (queue.Count == 0)
            {
                return true;
            }
            return false;
        }
        public bool HasNext()
        {
            if (_current != queue.Last && !IsEmpty())
                return true;
            return false;
        }
        public Song GetNext()
        {
            if (_current == null)
                _current = queue.First;
            else
                if (HasNext())
                    _current = _current.Next;
            return _current.Value;
        }
        public bool HasPrev()
        {
            if (_current != queue.First && !IsEmpty())
                return true;
            return false;
        }
        public Song GetPrev()
        {
            if (_current == null)
                _current = queue.First;
            else
                if (HasPrev())
                    _current = _current.Previous;
            return _current.Value;
        }
        public void Add(Song song)
        {
            queue.AddLast(song);
        }
        public Song GetCurrent()
        {
            if (_current == null)
                _current = queue.First;
            return _current.Value;
        }
    }
}
