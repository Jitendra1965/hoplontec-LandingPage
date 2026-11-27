// Choose the mobile edit once; resizing must never restart playback.
(() => {
  const video = document.getElementById('nivilog-demo-video');
  if (video && window.matchMedia('(max-width: 640px)').matches) {
    video.src = 'assets/nivilog-demo/nivilog-demo-en-portrait.mp4';
    video.poster = 'assets/nivilog-demo/nivilog-demo-poster-portrait.jpg';
    video.width = 720;
    video.height = 1560;
    video.classList.add('nivi-video-portrait');
  }
})();
