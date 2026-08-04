from flask import Flask, Response, render_template_string
import time

app = Flask(__name__)

# Frontend sahifasi
@app.route('/')
def index():
    html_code = """
    <!DOCTYPE html>
    <html>
    <head><title>Stream Test</title></head>
    <body>
        <h2>Flask Stream Testi:</h2>
        <div id="output" style="border: 1px solid #ccc; padding: 15px; font-family: monospace;"></div>

        <script>
            const outputDiv = document.getElementById('output');
            
            // EventSource yordamida streamga ulanamiz
            const eventSource = new EventSource('/stream');

            eventSource.onmessage = function(event) {
                // Har bir kelgan so'zni ekranga qo'shamiz
                outputDiv.innerText += event.data + " ";
            };

            eventSource.onerror = function() {
                console.log("Stream tugadi.");
                eventSource.close();
            };
        </script>
    </body>
    </html>
    """
    return render_template_string(html_code)

# Stream uzatuvchi backend yo'nalishi
@app.route('/stream')
def stream():
    def generate():
        text = "Salom! Bu matn Flask serveridan kompyuteringizda real-vaqt rejimida stream bo'lib kelmoqda..."
        for word in text.split(" "):
            yield f"data: {word}\n\n"  # SSE formati
            time.sleep(0.2)  # Har so'z orasida 0.2 soniya kutiladi

    return Response(generate(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True)