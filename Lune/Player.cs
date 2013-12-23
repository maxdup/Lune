using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using NAudio;
using NAudio.Wave;
using System.Windows.Controls;
using System.ComponentModel;
using System.Windows.Threading;

namespace Lune
{
    /* This is the man-meat of the program. It deals with the audio library and plays audio
     * TODO: add support for other audio formats
     */
    class Player : INotifyPropertyChanged
    {
        private IWavePlayer _waveOutDevice;
        private WaveStream _mainOutputStream;
        private WaveChannel32 _volumeStream;
        private DispatcherTimer timer = new DispatcherTimer();

        private SongQueue _queue;
        private Boolean _playing;

        private string _currentTime;
        public string currentTime
        {
            get { return _currentTime; }
            set { _currentTime = value; PropertyChange("currentTime"); }
        }
        private string _songLength;
        public string songLength
        {
            get { return _songLength; }
            set { _songLength = value; PropertyChange("songLength"); }
        }
        const double sliderMax = 10.0;

        private string _currSongInfo;
        public string currSongInfo
        {
            get { return _currSongInfo; }
            set { _currSongInfo = value; PropertyChange("currSongInfo"); }
        }

        private double _sliderPosition;
        public double SliderPosition
        {
            get { return _sliderPosition; }
            set
            {
                if (_sliderPosition != value)
                {
                    _sliderPosition = value;
                    if (_mainOutputStream != null)
                    {
                        var pos = (long)(_mainOutputStream.Length * _sliderPosition / sliderMax);
                        _mainOutputStream.Position = pos;
                    }
                    PropertyChange("SliderPosition");
                    _currentTime = _mainOutputStream.CurrentTime.Minutes.ToString() + ":" + _mainOutputStream.CurrentTime.Seconds.ToString();
                    PropertyChange("currentTime");
                }
            }
        }

        private void TimerOnTick(object sender, EventArgs eventArgs)
        {
            if (_mainOutputStream != null)
            {
                _sliderPosition = Math.Min(sliderMax, _mainOutputStream.Position * sliderMax / _mainOutputStream.Length);
                PropertyChange("SliderPosition");
                _currentTime = _mainOutputStream.CurrentTime.Minutes.ToString() + ":" + _mainOutputStream.CurrentTime.Seconds.ToString();
                PropertyChange("currentTime");
            }
        }

        public Player()
        {
            _queue = new SongQueue();
            _waveOutDevice = new WaveOut();
            _waveOutDevice.PlaybackStopped += new EventHandler<StoppedEventArgs>(waveOutDevice_playbackstopped);
            currSongInfo = "";
            timer.Interval = TimeSpan.FromMilliseconds(1000);
            timer.Tick += TimerOnTick;
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
                _queue.GetCurrent();
                //_queue.GetCurrent().name += "•";//just a test for a future feature (should notify too)
                songLength = (_queue.GetCurrent().Duration.Minutes).ToString() + ":" + (_queue.GetCurrent().Duration.Seconds).ToString();
                _mainOutputStream = CreateInputStream(_queue.GetCurrent().path);
                _currentTime = _mainOutputStream.CurrentTime.Minutes.ToString() + ":" + _mainOutputStream.CurrentTime.Seconds.ToString();
                _waveOutDevice.Init(_mainOutputStream);
                _waveOutDevice.Play();
                _playing = true;
                timer.Start();
            }
        }

        public void Resume()
        {
            if (_mainOutputStream != null)
            {
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
            SliderPosition = 0;
            timer.Stop();
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

        public event PropertyChangedEventHandler PropertyChanged;

        private void PropertyChange(string prop)
        {
            if (PropertyChanged != null)
            {
                PropertyChanged(this, new PropertyChangedEventArgs(prop));
            }
        }
    }
}
