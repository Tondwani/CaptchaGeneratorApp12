# CAPTCHA Generator Application

This is a simple CAPTCHA generator application built using Python and Tkinter. It generates a random CAPTCHA and allows users to enter and validate the CAPTCHA.

## Features

- Generate random CAPTCHAs consisting of letters and numbers.
- Refresh button to generate a new CAPTCHA.
- Input field for users to enter the CAPTCHA.
- Validation of the entered CAPTCHA with feedback messages.

## Requirements

- Python 3.x

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/captcha-generator.git
    ```
2. **Navigate to the project directory:**
    ```sh
    cd captcha-generator
    ```

## Running the Application

1. **Open Visual Studio Code:**
    - Go to `File` > `Open Folder` and select the project directory.

2. **Open the terminal in Visual Studio Code:**
    - Go to `View` > `Terminal` to open the terminal.

3. **Run the Python script:**
    ```sh
    python captcha_generator.py
    ```

## Code Explanation

### `captcha_generator.py`

This script contains the main logic for the CAPTCHA generator application.

- **Imports:**
    - `tkinter` is imported for creating the GUI.
    - `random` and `string` are used for generating the random CAPTCHA.

- **Class `CaptchaGeneratorApp`:**
    - Initializes the main window and sets up the GUI elements.
    - The `create_widgets` method creates and packs the GUI widgets.
    - The `generate_captcha` method generates a random CAPTCHA and updates the display.
    - The `validate_captcha` method checks if the user-entered CAPTCHA matches the generated one and updates the message label.

- **Main Execution Block:**
    - Creates a Tkinter root window.
    - Instantiates the `CaptchaGeneratorApp` class.
    - Runs the Tkinter main loop.

### UI Elements

- **Header:** Displays "Captcha Generator" with specified styling.
- **CAPTCHA Display:** Shows the generated CAPTCHA in a read-only input field.
- **Refresh Button:** Allows users to generate a new CAPTCHA.
- **Input Field:** Allows users to enter the CAPTCHA.
- **Submit Button:** Validates the entered CAPTCHA.
- **Message Label:** Displays feedback messages regarding CAPTCHA validation.

### Styling

- The application uses similar colors and fonts as specified in the CSS:
    - Background color: `#826afb`
    - Font: Poppins
    - Text color for correct CAPTCHA: `#826afb`
    - Text color for incorrect CAPTCHA: `#FF2525`

## Conclusion

This project demonstrates a simple CAPTCHA generator application using Python and Tkinter. The generated CAPTCHAs can be used to verify user input and provide basic validation feedback.

Feel free to contribute to the project or modify it as needed!
