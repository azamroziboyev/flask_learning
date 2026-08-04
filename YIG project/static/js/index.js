// Wait until the DOM is fully loaded
document.addEventListener("DOMContentLoaded", function () {

    // ===========================
    // DOM Element References
    // Executed immediately on DOM ready
    // ===========================
    const urlInputField = document.getElementById("urlInputField");
    const getActionButton = document.getElementById("getActionButton");
    const resultCardBox = document.getElementById("resultCardBox");
    const streamTextContent = document.getElementById("streamTextContent");

    // Dynamic stream interval & animation timer references
    let activeStreamInterval = null;
    let cardAppearanceTimeout = null;
    let getButtonDelayTimeout = null;

    // ===========================
    // Initialize Event Listeners
    // Executed on script setup
    // ===========================
    function initializeEventListeners() {
        urlInputField.addEventListener("input", handleInputChange);
        getActionButton.addEventListener("click", handleGetButtonClick);
    }

    // ===========================
    // Handle Input Changes
    // Delays GET button appearance by 1 second and triggers smooth dissolution when empty
    // Executed on every keystroke/paste in input field
    // ===========================
    function handleInputChange() {
        const currentInputValue = urlInputField.value.trim();

        if (getButtonDelayTimeout) {
            clearTimeout(getButtonDelayTimeout);
        }

        if (currentInputValue.length > 0) {
            // Aynan 1 soniya (1000ms) kutib, GET tugmasini ko'rsatamiz
            getButtonDelayTimeout = setTimeout(function () {
                showGetButton();
            }, 1000);
        } else {
            hideGetButton();
            fadeOutResultCard();
        }
    }

    // ===========================
    // Show GET Button
    // Displays the light-blue GET button smoothly
    // Executed 1 second after user pastes/types link
    // ===========================
    function showGetButton() {
        getActionButton.classList.remove("hidden");
        requestAnimationFrame(function () {
            getActionButton.classList.add("visible");
        });
    }

    // ===========================
    // Hide GET Button
    // Smoothly fades out the GET button
    // Executed when input is cleared
    // ===========================
    function hideGetButton() {
        if (getButtonDelayTimeout) {
            clearTimeout(getButtonDelayTimeout);
        }
        getActionButton.classList.remove("visible");
        setTimeout(function () {
            getActionButton.classList.add("hidden");
        }, 400);
    }

    // ===========================
    // Handle GET Button Click
    // Triggers smooth 0.5s box fade-in, followed by text streaming
    // Executed on GET button press
    // ===========================
    async function handleGetButtonClick() {
        if (activeStreamInterval) clearInterval(activeStreamInterval);
        if (cardAppearanceTimeout) clearTimeout(cardAppearanceTimeout);

        streamTextContent.textContent = "";
        
        // Step 1: Box va uning joylashuvi 0.5s davomida ravon paydo bo'ladi
        resultCardBox.classList.remove("hidden");
        
        requestAnimationFrame(function () {
            resultCardBox.classList.add("visible");
        });

        const targetUrl = urlInputField.value.trim();

        try {
            // Flask backend'ingizga so'rov yuboramiz va to'liq matnni olamiz
            const response = await fetch('/get-summary', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ url: targetUrl })
            });

            const data = await response.json();
            const fullTextFromFlask = data.result; // Flask qaytargan tayyor matn

            // Step 2: Box 0.5s to'liq ochilgandan so'ng Flask matnini stream (typing) qilamiz
            cardAppearanceTimeout = setTimeout(function () {
                streamResponse(fullTextFromFlask);
            }, 500);

        } catch (error) {
            console.error("Xatolik:", error);
            streamTextContent.textContent = "Ma'lumot olishda xatolik yuz berdi.";
        }
    }

    // ===========================
    // Fade Out Result Card
    // Smoothly dissolves card and returns input area back down gently over 0.5s
    // Executed when input field becomes empty
    // ===========================
    function fadeOutResultCard() {
        if (resultCardBox.classList.contains("hidden")) return;

        if (activeStreamInterval) clearInterval(activeStreamInterval);
        if (cardAppearanceTimeout) clearTimeout(cardAppearanceTimeout);

        // Karta yo'qolishi va input joyiga qaytishi 0.5s silliq davom etadi
        resultCardBox.classList.remove("visible");

        setTimeout(function () {
            resultCardBox.classList.add("hidden");
            streamTextContent.textContent = "";
        }, 500);
    }

    // ===========================
    // Stream Response
    // Types characters dynamically ChatGPT-style
    // Executed 0.5s after box has fully appeared
    // ===========================
    function streamResponse(fullText) {
        streamTextContent.textContent = "";
        let currentCharIndex = 0;

        activeStreamInterval = setInterval(function () {
            if (currentCharIndex < fullText.length) {
                streamTextContent.textContent += fullText.charAt(currentCharIndex);
                currentCharIndex++;
            } else {
                clearInterval(activeStreamInterval);
            }
        }, 20); // Matn yozilish tezligi (ms)
    }

    // Launch app logic
    initializeEventListeners();
});