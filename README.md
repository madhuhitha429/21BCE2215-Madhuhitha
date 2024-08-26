# 21BCE2215-Madhuhitha
Battle on the Grid
Project Description
"Battle on the Grid" is a turn-based strategy game where two players take turns to move characters on a grid. The game features different types of characters with unique movement patterns and abilities. This project uses Flask for the backend and Socket.IO for real-time communication between the server and clients. The frontend is built with HTML, CSS, and JavaScript.

Features
Real-Time Gameplay: Using Socket.IO for real-time updates.
Dynamic Grid: The game board updates dynamically based on player moves.
Move History: Tracks and displays the move history of both players.
Reset Functionality: Allows players to reset the game state.
Technologies Used
Backend: Python, Flask, Socket.IO
Frontend: HTML, CSS, JavaScript
WebSocket: Socket.IO




Create a virtual environment and activate it:

bash
Copy code
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
Install the required Python packages:

bash
Copy code
pip install -r requirements.txt
Install Node.js Dependencies

Install Socket.IO for the frontend:

bash
Copy code
npm install
Run the Flask Application

bash
Copy code
python app.py
Access the Game

Open a web browser and go to http://localhost:5000 to play the game.

Usage
Submitting Moves: Enter the move command in the input box and click "Submit Move."
Resetting the Game: Click the "Reset Game" button to restart the game.
Move History: View the move history for each player on the right side of the game board.
Contributing
Contributions are welcome! If you would like to contribute to this project, please follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Commit your changes (git commit -am 'Add new feature').
Push to the branch (git push origin feature-branch).
Create a new Pull Request.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Flask: For serving the application and handling server-side logic.
Socket.IO: For real-time communication between the client and server.
Google Fonts: For the stylish font used in the game.
