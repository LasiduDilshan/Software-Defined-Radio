# End-to-End Communication System with BladeRF and GNU Radio

Welcome to the End-to-End Communication System repository! This project showcases the implementation of a comprehensive communication system using BladeRF and GNU Radio software. Whether you're interested in digital communication, encryption, or real-time audio transmission, this repository has something for you.

## Overview

The project focuses on designing and implementing a versatile communication system capable of transmitting and receiving various types of data. Leveraging the power of Software-Defined Radio (SDR) technology, it provides a platform for experimenting with different modulation techniques and signal processing algorithms.

## Features

- **BladeRF Integration**: Utilizes the BladeRF platform for radio frequency (RF) signal processing.
- **GNU Radio Implementation**: Implements signal processing and modulation/demodulation using GNU Radio blocks.
- **End-to-End Communication**: Demonstrates a complete communication system, including transmission and reception of data.
- **Modulation Techniques**: Supports various modulation techniques such as Amplitude Shift Keying (ASK), Frequency Shift Keying (FSK), and Quadrature Amplitude Modulation (QAM).
- **Graphical User Interface (GUI)**: Provides a user-friendly interface for configuring and monitoring the communication system parameters.

## Components

## 1. Digital Communication and Preamble Handling

This component manages digital communication between systems and handles preamble sequences.

### Preamble Script (preamble.py):

- Functions to add and remove preambles from files.
- Detects and removes preambles at the beginning and end of files.

### Digital Communication (digital_com.py):

- Manages digital communication between systems.
- Provides functions for encoding and decoding digital data.

## 2. Encryption and Decryption

Python scripts utilizing the AES algorithm for file encryption and decryption.

### Encryption (encrypt.py):

- Encrypts a file using the AES algorithm.
- Pads the plaintext to ensure its length is a multiple of 16 bytes.
- Adds a preamble to the ciphertext after encryption.

### Decryption (decrypt.py):

- Decrypts a file encrypted using the AES algorithm.
- Removes the preamble and then decrypts the ciphertext.
- Writes the decrypted data to a file.

## 3. Real-Time Audio Transmission

This component focuses on transmitting audio data using analog technologies, ensuring robust performance without synchronization issues common in digital communication.

**Dependencies:**

Python 3.10.1.1
GNU Radio 3.10.1.1
PyQt5

**Components:**

- **Real-Time FM Class**: Inherits from gr.top_block and Qt.QWidget. Sets up the GUI for the GNU Radio flowgraph.
   - **Initialization**: Initializes variables such as volume and sample rate. Sets up GUI elements using PyQt5.
   - **Blocks**:
      - **Volume Control**: Enables volume adjustment via a slider.
      - **Soapy BladeRF Sink**: Sends data to the BladeRF device for transmission.
      - **Wavfile Source**: Reads audio data from a WAV file.
      - **Multiply Constants**: Adjusts volume and applies modulation.
      - **Analog NBFM TX**: Generates narrow-band FM signals for transmission.
      - **QT GUI Sink**: Displays time-domain and frequency-domain plots.
   - **Connections**: Establishes data flow between various blocks.
   - **Event Handling**: Manages the close event to save settings and stop the flowgraph.
   - **Main Function**: Initializes the flowgraph, starts it, and displays the GUI. Handles signals for graceful termination.


## Getting Started

To set up and use the end-to-end communication system, follow these steps:

1. **Clone the Repository**: Clone this repository to your local machine using Git.

Copy code
git clone https://github.com/LasiduDilshan/Software-Defined-Radio.git

2. **Install Dependencies**: Ensure you have GNU Radio and BladeRF drivers installed on your system. Refer to the documentation for installation instructions.

3. **Configure BladeRF**: Connect your BladeRF device to the computer and configure it using the provided Python scripts or command-line tools.

4. **Run GNU Radio Flowgraphs**: Execute the GNU Radio flowgraphs for the transmitter and receiver to initiate communication. Adjust parameters as needed.

5. **Monitor and Analyze**: Use the GUI or command-line tools to monitor system performance, visualize signals, and analyze transmitted and received data.

## Contributions

Contributions to this project are encouraged! If you have ideas for improvements, bug fixes, or new features, please submit a pull request. Your contributions help make this project better for everyone.

## License

This project is licensed under the MIT License, allowing you to use and modify the code for your own projects. Feel free to customize and extend the functionality to suit your needs.

## Contact

For any questions, suggestions, or feedback, please feel free to contact the project maintainer at dilshanlasindu0@gmail.com. Your input is highly appreciated!