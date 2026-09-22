# 🎰 Random Generator Hub

A simple and interactive **Streamlit-based Random Generator Hub** that brings multiple randomization tools together in one application.

Generate random numbers, roll dice, or flip a coin — all through a clean and interactive dashboard with animated results. ✨


## 🚀 Features

### 🔢 Random Number Generator

- Set your own minimum and maximum values
- Enter a hidden secret number
- Animated random number generation
- Checks whether the generated number matches the secret number
- 🎉 Displays a winning message when the numbers match
- 😅 Displays a retry message when they don't
- 🎈 Celebration animation when the secret number is matched


### 🎲 Dice Roller

- Choose between 1 and 6 dice
- Animated dice rolling effect
- Displays individual dice results
- Automatically calculates the total
- 🎯 Clear final result display


### 🪙 Coin Flip

- Interactive coin-flipping animation
- Randomly generates HEADS or TAILS
- Displays the final result clearly
- 🎉 Celebration animation after the coin lands


## 🛠️ Tech Stack

- Python
- Streamlit
- NumPy

## 🖥️ Application Screenshots
!(<img width="909" height="419" alt="image" src="https://github.com/user-attachments/assets/67436549-238a-4251-bf94-7a1ed06980c7" />)
(<img width="898" height="410" alt="image" src="https://github.com/user-attachments/assets/b52fc337-76c7-4cc2-b748-e4c89c47e670" />
)
(<img width="828" height="408" alt="image" src="https://github.com/user-attachments/assets/7d5b84b3-b3fd-483d-bea9-518c222ccbf3" />
)


## 📂 Project Structure

```text
Random-Generator/
│
├── main.py
├── random_number.py
├── dice.py
├── coin_flip.py
├── requirements.txt
│
└── .streamlit/
    └── config.toml

▶️ Run Locally
1. Clone the repository
git clone https://github.com/YOUR-USERNAME/Random-Generator.git
2. Navigate to the project directory
cd Random-Generator
3. Install the required dependencies
pip install -r requirements.txt
4. Run the Streamlit application
streamlit run main.py

The application will open in your default web browser.

📦 Requirements
The project requires the following Python packages:

streamlit
numpy
🎨 Application Modules

The application provides three generators from a single dashboard:

🔢 Random Number
       ↓
🎲 Dice Roller
       ↓
🪙 Coin Flip

🔮 Future Improvements
🎯 Random number history
📊 Statistics and probability information
🎲 Custom-sided dice
🪙 Custom coin options
🔊 Sound effects
🏆 Score and challenge system
📱 Improved mobile responsiveness
🎨 Additional themes
👨‍💻 Author

Karthik Reddy / KarthikReddy1971

Built with ❤️ using Python and Streamlit.

📄 License

This project is open-source and available for learning and personal use.
