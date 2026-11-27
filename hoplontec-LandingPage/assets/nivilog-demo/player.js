// Select the mobile edit once, before playback. Resizing never restarts a video.
// The landscape source, native controls and captions also work without JavaScript.
(() => {
  const videos = Array.from(document.querySelectorAll('video[data-nivilog-video]'));
  const mobile = window.matchMedia('(max-width: 640px)').matches;
  for (const video of videos) {
    if (mobile && video.dataset.portraitSrc && video.dataset.portraitPoster) {
      video.src = video.dataset.portraitSrc;
      video.poster = video.dataset.portraitPoster;
      video.width = 720;
      video.height = 1560;
      video.classList.add('nivi-video-portrait');
    }
    // Two narrated videos should never speak over one another.
    video.addEventListener('play', () => {
      for (const other of videos) {
        if (other !== video && !other.paused) other.pause();
      }
    });
  }
})();
