document.addEventListener('DOMContentLoaded', () => {
    const searchForm = document.getElementById('search-form');
    const cityInput = document.getElementById('city-input');
    const weatherContent = document.getElementById('weather-content');
    const loadingDiv = document.getElementById('loading');
    const errorDiv = document.getElementById('error-message');

    // DOM Elements for weather data
    const cityNameEl = document.getElementById('city-name');
    const tempValueEl = document.getElementById('temp-value');
    const weatherDescEl = document.getElementById('weather-desc');
    const windSpeedEl = document.getElementById('wind-speed');

    searchForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const city = cityInput.value.trim();
        if (!city) return;

        // Reset UI State
        weatherContent.classList.add('hidden');
        errorDiv.classList.add('hidden');
        loadingDiv.classList.remove('hidden');

        try {
            const response = await fetch(`/api/weather?city=${encodeURIComponent(city)}`);
            const data = await response.json();

            loadingDiv.classList.add('hidden');

            if (!response.ok) {
                throw new Error(data.error || 'Failed to fetch weather data');
            }

            // Update UI with data
            cityNameEl.textContent = data.city;
            tempValueEl.textContent = Math.round(data.temperature);
            weatherDescEl.textContent = data.description;
            windSpeedEl.textContent = data.windspeed;

            // Show weather content
            weatherContent.classList.remove('hidden');
            
            // Re-trigger animation
            weatherContent.classList.remove('fade-in');
            void weatherContent.offsetWidth; // Trigger reflow
            weatherContent.classList.add('fade-in');

        } catch (error) {
            loadingDiv.classList.add('hidden');
            errorDiv.textContent = error.message;
            errorDiv.classList.remove('hidden');
        }
    });
});
