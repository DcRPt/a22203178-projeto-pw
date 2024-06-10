document.addEventListener('DOMContentLoaded', (event) => {
    const darkModeToggle = document.getElementById('dark-mode-toggle');
    const body = document.body;

    // Função para adicionar ou remover a classe dark-mode
    const applyDarkMode = (enable) => {
        body.classList.toggle('dark-mode', enable);
        document.querySelectorAll('.main-content, header, footer, nav, .weather-block, .clock-block, .about-me-section, .skills-section, .education-section').forEach(el => {
            el.classList.toggle('dark-mode', enable);
        });

        // Atualiza o texto do botão com base no estado do modo escuro
        darkModeToggle.textContent = enable ? 'Light Mode' : 'Dark Mode';
    };

    // Função de alternância baseada no estado atual
    const toggleDarkMode = () => {
        const isDarkModeEnabled = body.classList.contains('dark-mode');
        localStorage.setItem('darkMode', isDarkModeEnabled ? 'disabled' : 'enabled');
        applyDarkMode(!isDarkModeEnabled);
    };

    // Carrega o estado inicial do modo escuro do localStorage
    const initDarkMode = () => {
        const darkModeSetting = localStorage.getItem('darkMode');
        const isDarkMode = darkModeSetting === 'enabled';
        applyDarkMode(isDarkMode);
    };

    // Inicializa o modo escuro baseado na configuração salva
    initDarkMode();

    // Adiciona evento de clique ao botão
    darkModeToggle.addEventListener('click', toggleDarkMode);
});