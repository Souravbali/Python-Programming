import datetime

# Python script to generate a fully interactive HTML page
# User enters name in browser → clicks button → shows personalized Date, Time, Year

html_interactive = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interactive Date & Time</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #1e3c72, #2a5298);
            color: #fff;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 20px;
            text-align: center;
        }
        .container {
            background: rgba(255, 255, 255, 0.1);
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            max-width: 500px;
            width: 100%;
            transition: transform 0.3s ease;
        }
        .container:hover {
            transform: translateY(-8px);
        }
        h1 {
            margin-bottom: 15px;
            font-size: 2.3em;
            text-shadow: 0 2px 4px rgba(0,0,0,0.3);
        }
        .input-group {
            margin: 25px 0;
        }
        label {
            display: block;
            font-size: 1.2em;
            margin-bottom: 10px;
            color: #a0d8ff;
            font-weight: 500;
        }
        input[type="text"] {
            width: 100%;
            padding: 14px;
            font-size: 1.1em;
            border: none;
            border-radius: 12px;
            background: rgba(255, 255, 255, 0.2);
            color: white;
            text-align: center;
            transition: all 0.3s ease;
        }
        input[type="text"]::placeholder {
            color: #ddd;
        }
        input[type="text"]:focus {
            outline: none;
            background: rgba(255, 255, 255, 0.3);
            box-shadow: 0 0 15px rgba(160, 216, 255, 0.5);
        }
        button {
            margin-top: 20px;
            padding: 14px 30px;
            font-size: 1.1em;
            font-weight: bold;
            color: #1e3c72;
            background: #a0d8ff;
            border: none;
            border-radius: 12px;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(160, 216, 255, 0.4);
        }
        button:hover {
            background: #8ac8ff;
            transform: translateY(-3px);
            box-shadow: 0 8px 25px rgba(160, 216, 255, 0.6);
        }
        .result {
            margin-top: 30px;
            opacity: 0;
            transition: opacity 0.5s ease;
        }
        .result.show {
            opacity: 1;
        }
        .greeting {
            font-size: 1.5em;
            margin-bottom: 20px;
            color: #a0d8ff;
        }
        .info {
            margin: 16px 0;
            font-size: 1.4em;
            padding: 14px;
            background: rgba(255, 255, 255, 0.15);
            border-radius: 12px;
            transition: all 0.3s ease;
        }
        .info:hover {
            background: rgba(255, 255, 255, 0.25);
            transform: translateX(5px);
        }
        .label {
            display: inline-block;
            width: 100px;
            font-weight: bold;
            color: #a0d8ff;
        }
        footer {
            margin-top: 40px;
            font-size: 0.9em;
            color: #ccc;
        }
        .hidden {
            display: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🕰️ Live Date & Time</h1>
        
        <div class="input-group">
            <label for="userName">Enter Your Name:</label>
            <input type="text" id="userName" placeholder="e.g., Alex" autocomplete="off">
        </div>
        
        <button onclick="showDateTime()">Show Date & Time</button>
        
        <div id="result" class="result">
            <div class="greeting" id="greeting"></div>
            <div class="info"><span class="label">Date:</span> <span id="date"></span></div>
            <div class="info"><span class="label">Time:</span> <span id="time"></span></div>
            <div class="info"><span class="label">Year:</span> <span id="year"></span></div>
        </div>
        
        <footer>Interactive • Python-Generated • HTML/CSS/JS</footer>
    </div>

    <script>
        function showDateTime() {
            const nameInput = document.getElementById('userName').value.trim();
            const name = nameInput || "Guest";
            
            const now = new Date();
            const date = now.toLocaleDateString('en-US', { 
                weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' 
            });
            const time = now.toLocaleTimeString('en-US', { 
                hour: '2-digit', minute: '2-digit', second: '2-digit' 
            });
            const year = now.getFullYear();

            document.getElementById('greeting').innerHTML = `Hello, <strong>${name}</strong>!`;
            document.getElementById('date').textContent = date;
            document.getElementById('time').textContent = time;
            document.getElementById('year').textContent = year;
            
            document.getElementById('result').classList.add('show');
        }

        // Allow Enter key to trigger
        document.getElementById('userName').addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                showDateTime();
            }
        });
    </script>
</body>
</html>
"""

# Save interactive HTML file
filename = "interactive_datetime.html"
with open(filename, "w", encoding="utf-8") as f:
    f.write(html_interactive)

print(f"""
Interactive HTML file '{filename}' generated!
Open it in your browser:
1. Enter your name
2. Click 'Show Date & Time' or press Enter
3. See live Date, Time, Year with beautiful animation!

No Python needed after this — fully works in browser!
""")