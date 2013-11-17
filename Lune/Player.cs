using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using NAudio;
using NAudio.Wave;
using System.Windows.Controls;

namespace Lune
{
    /*This is the man-meat of the program. It deals with the audio library and plays audio
     * TODO: add support for other audio formats
     */
    class Player
    {
        private IWavePlayer _waveOutDevice;
        private WaveStream _mainOutputStream;
        private WaveChannel32 _volumeStream;
        
        private SongQueue _queue;
        private Boolean _playing;

        private string currSongInfo;

        public Player()
        {
            _queue = new SongQueue();
            _waveOutDevice = new WaveOut();
            _waveOutDevice.PlaybackStopped += new EventHandler<StoppedEventArgs>(waveOutDevice_playbackstopped);
        }

        public bool IsPlaying()
        {
            return _playing;
        }

        public void Start()
        {
            if (!_queue.IsEmpty())
            {
                CloseWaveOut();
                currSongInfo = _queue.GetCurrent().name;
                _mainOutputStream = CreateInputStream(_queue.GetCurrent().path);
                _waveOutDevice.Init(_mainOutputStream);
                _waveOutDevice.Play();
                _playing = true;
            }
        }

        public void Resume()
        {
            if (_mainOutputStream != null){
                _waveOutDevice.Play();
                _playing = true;
            }
        }

        public void Pause()
        {
            _waveOutDevice.Pause();
            _playing = false;
        }

        public void Stop()
        {
            _waveOutDevice.Stop();
            _mainOutputStream = null;
            _queue = new SongQueue();
            currSongInfo = "";
            CloseWaveOut();
            _playing = false;
        }

        //the hybrid method combines Start, Resume and Pause depending on the context of the player
        public void Hybrid()
        {
            if (_playing)
                Pause();
            else
            {
                Resume();
                if (!_playing)
                    Start();
            }
        }

        public void Skip()
        {
            if (_queue != null)
                if (_queue.HasNext())
                {
                    _queue.GetNext();
                    Start();
                }
                else
                {
                    Stop();
                }
        }

        public void Prev()
        {
            if (_queue.HasPrev())
            {
                CloseWaveOut();
                _mainOutputStream = CreateInputStream(_queue.GetPrev().path);
                _waveOutDevice.Init(_mainOutputStream);
            }
            if (_playing)
                Start();
 
        }

        public void setQueue(SongQueue queue)
        {
            _queue = queue;
        }


        private void waveOutDevice_playbackstopped(object sender, StoppedEventArgs e)
        {
            if (_queue.HasNext())
                Skip();
        }

        private WaveStream CreateInputStream(string fileName)
        {
            WaveChannel32 inputStream;
            if (fileName.EndsWith(".mp3"))
            {
                WaveStream mp3Reader = new Mp3FileReader(fileName);
                inputStream = new WaveChannel32(mp3Reader);
            }
            else
            {
                throw new InvalidOperationException("Unsupported extension");
            }
            _volumeStream = inputStream;
            _volumeStream.PadWithZeroes = false;
            return _volumeStream;
        }

        private void CloseWaveOut()
        {
            if (_waveOutDevice != null)
            {
                _waveOutDevice.Stop();
                _waveOutDevice.Dispose();
                _waveOutDevice = new WaveOut();
                _waveOutDevice.PlaybackStopped += new EventHandler<StoppedEventArgs>(waveOutDevice_playbackstopped);
            }
        }
    }
}
