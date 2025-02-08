document.getElementById('theme-toggle').addEventListener('click', function() {
    const body = document.body;
    const isDark = body.dataset.bsTheme === 'dark';
    body.dataset.bsTheme = isDark ? 'light' : 'dark';
    this.classList.toggle('btn-dark', !isDark);
    this.classList.toggle('btn-light', isDark);
});

