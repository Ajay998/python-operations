document.addEventListener("DOMContentLoaded", function () {
    const musicItems = document.querySelectorAll('.musicitem');
    const musicContent = document.querySelector('.musiccontent');
    const playerImgElement = musicContent.querySelector('.playerimg');
    const musicNameElement = musicContent.querySelector('.musicname');
    const artistElement = musicContent.querySelector('.artist');
    const playPauseBtn = document.getElementById('playPause');
    const progressBar = document.getElementById('progressbar');
    let startTimeSpan = document.querySelector('.starttimespan');
    let endTimeSpan = document.querySelector('.endtimespan');
    let volume = document.getElementById('volume');
    let backward = document.getElementById('backward');
    let forward = document.getElementById('forward');
    let nextMusic = document.getElementById('lastmusic');
    let lastMusic = document.getElementById('nextmusic');
    let audioPlayer = new Audio();
    let isPlaying = false;
    let currentIndex = 0;
    let currentTime = 0;
    let pausedTimes = Array.from({ length: musicItems.length }, () => 0); // Array to store paused time for each song
    let song = [];

    musicItems.forEach(function (musicItem, index) {
        const songElement = musicItem.querySelector('.currentmusic');
        const musicImage = musicItem.querySelector('img').src;
        const musicName = musicItem.querySelector('.musicname').innerHTML;
        const musicArtist = musicItem.querySelector('.artistname').innerHTML;

        song.push({ name: musicName, artist: musicArtist, image: musicImage, file: songElement });

        musicItem.addEventListener('click', function () {
            currentIndex = index;
            playPause(currentIndex);
            changeBottomContent(currentIndex);
        });
    });

    function changeBottomContent(index) {
        playerImgElement.src = song[index].image;
        musicNameElement.textContent = song[index].name;
        artistElement.textContent = song[index].artist;
    }

    async function playPause(index) {
        const newSrc = song[index].file.src;
        progressBar.value = 0;

        startTimeSpan.textContent = '00:00';
        endTimeSpan.textContent = '00:00';

        if (isPlaying && audioPlayer.src === newSrc) {
            isPlaying = false;
            pausedTimes[currentIndex] = audioPlayer.currentTime;
            audioPlayer.pause();
        } else {
            audioPlayer.src = newSrc;

            await audioPlayer.play();
            isPlaying = true;
            changePlayPauseIcon(isPlaying);

            audioPlayer.addEventListener('loadedmetadata', function () {
                audioPlayer.currentTime = pausedTimes[currentIndex];
            });

            audioPlayer.addEventListener('timeupdate', function () {
                seekTime(audioPlayer);
            });
        }

        changePlayPauseIcon(isPlaying);
        changeBottomContent(index);
    }

    function changePlayPauseIcon(isPlaying) {
        if (isPlaying) {
            playPauseBtn.classList.remove('fa-circle-play');
            playPauseBtn.classList.add('fa-circle-pause');
        } else {
            playPauseBtn.classList.remove('fa-circle-pause');
            playPauseBtn.classList.add('fa-circle-play');
        }
    }

    function seekTime(audioPlayer) {
        currentTime = audioPlayer.currentTime;
        let songDuration = audioPlayer.duration;
        let seekTime = (currentTime / songDuration) * 100;

        progressBar.value = seekTime;
        startTimeSpan.textContent = formatTime(currentTime);
        endTimeSpan.textContent = formatTime(songDuration);
    }

    function formatTime(seconds) {
        seconds = Math.floor(seconds);
        const hours = Math.floor(seconds / 3600);
        const minutes = Math.floor((seconds % 3600) / 60);
        const remainingSeconds = seconds % 60;

        const formattedHours = (hours > 0 ? hours.toString().padStart(2, '0') + ':' : '');
        const formattedMinutes = minutes.toString().padStart(2, '0');
        const formattedSeconds = remainingSeconds.toString().padStart(2, '0');

        return formattedHours + formattedMinutes + ':' + formattedSeconds;
    }

    playPauseBtn.addEventListener('click', function () {
        playPause(currentIndex);
    });

    volume.addEventListener('input', function () {
        const volumePercentage = volume.value;
        const normalizedVolume = Math.min(1, Math.max(0, volumePercentage / 100));

        audioPlayer.volume = normalizedVolume;
    });

    backward.addEventListener('click', function () {
        audioPlayer.currentTime -= 10;
    });

    forward.addEventListener('click', function () {
        audioPlayer.currentTime += 10;
    });

    nextMusic.addEventListener('click', function () {
        currentIndex = (currentIndex + 1) % song.length;
        playPause(currentIndex);
    });

    lastMusic.addEventListener('click', function () {
        currentIndex = (currentIndex - 1 + song.length) % song.length;
        playPause(currentIndex);
    });

    progressBar.addEventListener('input', function () {
        let seekTime = (progressBar.value / 100) * audioPlayer.duration;
        audioPlayer.currentTime = seekTime;
        pausedTimes[currentIndex] = seekTime; // Update paused time when user manually seeks
    });

    audioPlayer.addEventListener('ended', function () {
        // Reset paused time to zero
        pausedTimes[currentIndex] = 0;

        // Play the next song or restart the current song
        currentIndex = (currentIndex + 1) % song.length;
        playPause(currentIndex);
    });
});
document.addEventListener("DOMContentLoaded", function () {
    const musicItems = document.querySelectorAll('.musicitem');
    const musicContent = document.querySelector('.musiccontent');
    const playerImgElement = musicContent.querySelector('.playerimg');
    const musicNameElement = musicContent.querySelector('.musicname');
    const artistElement = musicContent.querySelector('.artist');
    const playPauseBtn = document.getElementById('playPause');
    const progressBar = document.getElementById('progressbar');
    let startTimeSpan = document.querySelector('.starttimespan');
    let endTimeSpan = document.querySelector('.endtimespan');
    let volume = document.getElementById('volume');
    let backward = document.getElementById('backward');
    let forward = document.getElementById('forward');
    let nextMusic = document.getElementById('lastmusic');
    let lastMusic = document.getElementById('nextmusic');
    const playlistItems = document.querySelectorAll('.playlistcontentitem');
    let audioPlayer = new Audio();
    let isPlaying = false;
    let currentIndex = 0;
    let currentTime = 0;
    let pausedTimes = Array.from({ length: musicItems.length }, () => 0); // Array to store paused time for each song
    let song = [];

    musicItems.forEach(function (musicItem, index) {
        const songElement = musicItem.querySelector('.currentmusic');
        const musicImage = musicItem.querySelector('img').src;
        const musicName = musicItem.querySelector('.musicname').innerHTML;
        const musicArtist = musicItem.querySelector('.artistname').innerHTML;
        song.push({ name: musicName, artist: musicArtist, image: musicImage, file: songElement });

        musicItem.addEventListener('click', function () {
            currentIndex = index;
            playPause(currentIndex);
            changeBottomContent(currentIndex);
        });
    });

    playlistItems.forEach(function (playlistItem, index) {
        playlistItem.addEventListener('click', function () {
            console.log("working")
            currentIndex = index;
            playPause(currentIndex);
            changeBottomContent(currentIndex);
        });
    });

    musicItems.forEach(function (musicItem, index) {
        const songElement = musicItem.querySelector('.currentmusic');
        const musicImage = musicItem.querySelector('img').src;
        const musicName = musicItem.querySelector('.musicname').innerHTML;
        const musicArtist = musicItem.querySelector('.artistname').innerHTML;

        song.push({ name: musicName, artist: musicArtist, image: musicImage, file: songElement });

        musicItem.addEventListener('click', function () {
            currentIndex = index;
            playPause(currentIndex);
            changeBottomContent(currentIndex);
        });
    });

    function changeBottomContent(index) {
        playerImgElement.src = song[index].image;
        musicNameElement.textContent = song[index].name;
        artistElement.textContent = song[index].artist;
    }

    async function playPause(index) {
        const newSrc = song[index].file.src;
        progressBar.value = 0;

        startTimeSpan.textContent = '00:00';
        endTimeSpan.textContent = '00:00';

        if (isPlaying && audioPlayer.src === newSrc) {
            isPlaying = false;
            pausedTimes[currentIndex] = audioPlayer.currentTime;
            audioPlayer.pause();
        } else {
            audioPlayer.src = newSrc;

            await audioPlayer.play();
            isPlaying = true;
            changePlayPauseIcon(isPlaying);

            audioPlayer.addEventListener('loadedmetadata', function () {
                audioPlayer.currentTime = pausedTimes[currentIndex];
            });

            audioPlayer.addEventListener('timeupdate', function () {
                seekTime(audioPlayer);
            });
        }

        changePlayPauseIcon(isPlaying);
        changeBottomContent(index);
    }

    function changePlayPauseIcon(isPlaying) {
        if (isPlaying) {
            playPauseBtn.classList.remove('fa-circle-play');
            playPauseBtn.classList.add('fa-circle-pause');
        } else {
            playPauseBtn.classList.remove('fa-circle-pause');
            playPauseBtn.classList.add('fa-circle-play');
        }
    }

    function seekTime(audioPlayer) {
        currentTime = audioPlayer.currentTime;
        let songDuration = audioPlayer.duration;
        let seekTime = (currentTime / songDuration) * 100;

        progressBar.value = seekTime;
        startTimeSpan.textContent = formatTime(currentTime);
        endTimeSpan.textContent = formatTime(songDuration);
    }

    function formatTime(seconds) {
        seconds = Math.floor(seconds);
        const hours = Math.floor(seconds / 3600);
        const minutes = Math.floor((seconds % 3600) / 60);
        const remainingSeconds = seconds % 60;

        const formattedHours = (hours > 0 ? hours.toString().padStart(2, '0') + ':' : '');
        const formattedMinutes = minutes.toString().padStart(2, '0');
        const formattedSeconds = remainingSeconds.toString().padStart(2, '0');

        return formattedHours + formattedMinutes + ':' + formattedSeconds;
    }

    playPauseBtn.addEventListener('click', function () {
        playPause(currentIndex);
    });

    volume.addEventListener('input', function () {
        const volumePercentage = volume.value;
        const normalizedVolume = Math.min(1, Math.max(0, volumePercentage / 100));

        audioPlayer.volume = normalizedVolume;
    });

    backward.addEventListener('click', function () {
        audioPlayer.currentTime -= 10;
    });

    forward.addEventListener('click', function () {
        audioPlayer.currentTime += 10;
    });

    nextMusic.addEventListener('click', function () {
        currentIndex = (currentIndex + 1) % song.length;
        playPause(currentIndex);
    });

    lastMusic.addEventListener('click', function () {
        currentIndex = (currentIndex - 1 + song.length) % song.length;
        playPause(currentIndex);
    });

    progressBar.addEventListener('input', function () {
        let seekTime = (progressBar.value / 100) * audioPlayer.duration;
        audioPlayer.currentTime = seekTime;
        pausedTimes[currentIndex] = seekTime; // Update paused time when user manually seeks
    });

    audioPlayer.addEventListener('ended', function () {
        // Reset paused time to zero
        pausedTimes[currentIndex] = 0;

        // Play the next song or restart the current song
        currentIndex = (currentIndex + 1) % song.length;
        playPause(currentIndex);
    });
});
