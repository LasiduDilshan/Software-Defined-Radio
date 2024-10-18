# End-to-End Communication System with BladeRF and GNU Radio 

Welcome to the End-to-End Communication System repository! This project showcases the implementation of a comprehensive communication system using BladeRF and GNU Radio software. Whether you're interested in digital communication, encryption, or real-time audio transmission, this repository has something for you.

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Components](#components)
    - [Digital Communication and Preamble Handling](#digital-communication-and-preamble-handling)
    - [Encryption and Decryption](#encryption-and-decryption)
    - [Real-Time Audio Transmission](#real-time-audio-transmission)
4. [Getting Started](#getting-started)
5. [Contributions](#contributions)
6. [License](#license)
7. [Contact](#contact)

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

**Dependencies:**

- Python 3.x
- Libraries: Crypto, base64

### Digital Communication (digital_com.py):

- Manages digital communication between systems.
- Provides functions for encoding and decoding digital data.

- **Functionality:**

   - Facilitates communication between systems using digital data encoding and decoding techniques.

- **Encoding:**

   - Provides functions to encode digital data into a format suitable for transmission.
   - Utilizes encoding schemes such as base64 for efficient data representation.

- **Decoding:**

   - Offers functions to decode received digital data back into its original format.
   - Ensures accurate retrieval of transmitted information.

- **Data Integrity:**

   - Implements mechanisms to maintain data integrity during transmission.
   - Utilizes error detection and correction techniques to minimize data loss or corruption.

- **Error Handling:**

   - Incorporates error handling mechanisms to manage transmission errors and ensure reliable communication.
   - Detects and addresses errors in transmitted data to maintain communication integrity.

### Preamble Script (preamble.py):

- Functions to add and remove preambles from files.
- Detects and removes preambles at the beginning and end of files.

- **Functionality:**

   - Manages the insertion and removal of preamble sequences in transmitted data streams.
   - Ensures synchronization and alignment between transmitting and receiving systems.

- **Preamble Generation:**

   - Generates preamble sequences to precede transmitted data.
   - Incorporates unique patterns or signatures for easy detection and synchronization.

- **Preamble Detection:**

   - Implements algorithms to detect and extract preamble sequences from received data streams.
   - Utilizes pattern matching or synchronization techniques to identify preamble boundaries.

- **Synchronization:**

   - Ensures synchronization between transmitting and receiving systems by aligning data streams based on detected preamble sequences.
   - Facilitates accurate data reception and interpretation.

**Integration:**
- These components seamlessly integrate into the end-to-end communication system, enhancing data reliability, integrity, and synchronization.
- Digital Communication and Preamble Handling modules work in conjunction with encryption, real-time transmission, and other system components to provide a comprehensive communication solution.

## 2. Encryption and Decryption

### Encryption (`encrypt.py`)

- **Purpose:** Encrypts a file using XOR operation.
- **Key Range:** Uses a single-byte key (0-255).
- **Key:** Fixed key `122` for XOR operation.
- **Process:**
  - Reads file as byte array.
  - XORs each byte with the key.
  - Writes encrypted data back to file.

### Decryption (`decrypt.py`)

- **Purpose:** Decrypts a file encrypted with XOR operation.
- **Key Range:** Uses the same single-byte key (0-255) as encryption.
- **Key:** Fixed key `122` for XOR operation.
- **Process:**
  - Reads encrypted file as byte array.
  - XORs each byte with the key to decrypt.
  - Writes decrypted data back to file.

### Key Considerations:

- **Security:** Basic XOR encryption is not secure for sensitive data.
- **Key Space:** Limited to a single byte (0-255).
- **Preamble:** Typically, no explicit preamble handling mentioned in the provided scripts.

## 3. Real-Time Audio Transmission

This component focuses on transmitting audio data using analog technologies, ensuring robust performance without synchronization issues common in digital communication.

**Dependencies:**

- Python 3.10.1.1
- GNU Radio 3.10.1.1
- PyQt5

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

## Contact

For any questions, suggestions, or feedback, please feel free to contact the project maintainer at dilshanlasindu0@gmail.com. Your input is highly appreciated!
