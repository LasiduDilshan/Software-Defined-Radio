# Software-Defined Radio Communication System
## Condensed Summary for CV Project Section

---

## PROJECT TITLE
**End-to-End Software-Defined Radio Communication System with BladeRF and GNU Radio**

---

## ONE-LINE DESCRIPTION
Developed a comprehensive SDR communication system implementing digital/analog modulation, encryption, error correction, and real-time audio transmission using BladeRF hardware and GNU Radio framework.

---

## QUICK OVERVIEW (2-3 sentences)
Designed and implemented a complete end-to-end communication system using Software-Defined Radio technology with BladeRF hardware and GNU Radio software. The system features three major modules: digital data transmission with error correction (supporting text, images, and audio), enhanced byte-stream communication, and real-time analog FM audio transmission. Includes XOR encryption for data security and comprehensive GUI for real-time signal monitoring and control.

---

## KEY ACCOMPLISHMENTS

• **Multi-Format Digital Communication**: Implemented BPSK modulation with FEC encoding to transmit text, images, and audio files reliably
• **Error Correction & Synchronization**: Designed robust system with convolutional coding, CRC error detection, and Costas loop synchronization
• **Real-Time FM Audio Transmission**: Developed GUI-based NBFM transmitter with live audio streaming at 433 MHz ISM band
• **Security Implementation**: Integrated XOR encryption/decryption for data protection during transmission
• **Hardware Integration**: Successfully interfaced BladeRF SDR hardware using SoapySDR abstraction layer
• **Custom Block Development**: Created embedded Python blocks for packet handling and state machine implementation

---

## TECHNICAL SKILLS DEMONSTRATED

**Communications:** BPSK/FM Modulation, FEC (Convolutional Coding), Symbol Synchronization, Carrier Recovery, Channel Modeling

**Programming:** Python 3.x, GNU Radio Framework, PyQt5 GUI Development, Embedded Python Blocks, State Machine Design

**DSP:** Sample Rate Conversion, Filtering, FFT Analysis, Constellation Mapping, CRC Error Detection

**Hardware:** BladeRF SDR, RF Transmission/Reception, Frequency Planning (433 MHz), Gain Control (17-73 dB)

**Tools:** GNU Radio Companion, SoapySDR, Base64 Encoding, Git Version Control

---

## TECHNICAL SPECIFICATIONS

| Component | Details |
|-----------|---------|
| **Hardware** | BladeRF x40/x115 SDR |
| **Software** | GNU Radio 3.10.1.1, Python 3.x, PyQt5 |
| **Modulation** | BPSK (Digital), NBFM (Analog) |
| **Frequency** | Configurable (433 MHz for FM) |
| **Sample Rate** | Up to 4 MSPS |
| **Error Correction** | Convolutional Encoding, CRC32 |
| **Encryption** | XOR Cipher (8-bit key) |
| **Data Types** | Text, Image, Audio (WAV) |
| **GUI** | Real-time FFT, Constellation, Waterfall plots |

---

## PROJECT COMPONENTS

### Module 1: Digital Communication with Preamble Handling
- Transmits any file type (text/image/audio) using BPSK modulation
- Forward Error Correction with convolutional coding
- Preamble/postamble for synchronization
- CRC32 for data integrity
- Base64 encoding for binary data
- Custom post-processing scripts

### Module 2: Enhanced Byte-Stream Digital Communication
- Improved efficiency with byte-stream approach
- Same reliability as Module 1 with optimized memory usage
- Integrated encryption workflow

### Module 3: Real-Time Analog Audio Transmission
- Narrowband FM (NBFM) modulation
- Live audio streaming with GUI controls
- Volume adjustment and signal visualization
- Low-latency transmission (44.1 kHz audio)

### Security Module: Encryption/Decryption
- XOR symmetric encryption (key: 122)
- Supports all binary file formats
- In-place encryption/decryption

---

## MEASURABLE RESULTS

• Successfully transmitted and received text, JPEG images, and WAV audio files with 100% data integrity
• Implemented error correction capable of recovering data in noisy channel conditions
• Achieved real-time audio transmission with <100ms latency
• Developed 5,000+ lines of documented Python code
• Created 3 complete, functional communication systems
• Generated 50+ pages of technical documentation
• Completed 32-page technical presentation

---

## IMPACT & APPLICATIONS

**Educational:** Demonstrates end-to-end understanding of communication systems from theory to hardware implementation

**Practical:** Can be adapted for emergency communications, IoT data transmission, remote sensing, or amateur radio

**Technical:** Showcases proficiency in DSP, RF engineering, software development, and hardware-software integration

---

## EXAMPLE CV BULLET POINTS

**For RF/Communications Engineer Role:**
• Designed and implemented end-to-end SDR communication system using BladeRF hardware and GNU Radio, featuring BPSK digital modulation with FEC, real-time FM audio transmission, and comprehensive error correction (CRC32, convolutional coding)

**For Software Engineer Role:**
• Developed 5,000+ lines of Python code for Software-Defined Radio application with PyQt5 GUI, custom GNU Radio blocks, state machine implementation, and real-time signal processing achieving <100ms audio latency

**For DSP Engineer Role:**
• Implemented digital signal processing algorithms including BPSK modulation/demodulation, symbol synchronization (Costas loop), convolutional encoding/decoding, and multi-rate sample conversion for SDR communication system

**For Embedded Systems Role:**
• Integrated BladeRF SDR hardware with GNU Radio software framework using SoapySDR abstraction, implementing RF transmission at 433 MHz with configurable gain (17-73 dB) and sample rates up to 4 MSPS

**For General Engineering Role:**
• Built complete communication system with three functional modules (digital data transmission, enhanced byte-stream communication, and real-time audio) demonstrating full-stack development from hardware integration to user interface

---

## CONDENSED TECHNICAL DESCRIPTION (For CV)

Developed a comprehensive Software-Defined Radio (SDR) communication system using BladeRF hardware and GNU Radio 3.10.1.1 framework. Implemented three major components: (1) Digital communication module with BPSK modulation, convolutional FEC encoding, CRC32 error detection, and custom preamble handling for transmitting multi-format files; (2) Enhanced byte-stream version with optimized memory management; (3) Real-time analog FM audio transmission system with PyQt5 GUI featuring live volume control and signal visualization. Integrated XOR encryption for data security and developed custom GNU Radio embedded Python blocks for packet handling. Successfully demonstrated end-to-end transmission of text, images, and audio with full data integrity recovery. Technologies: Python 3.x, GNU Radio, PyQt5, SoapySDR, BladeRF, DSP algorithms, RF communications.

---

## RELEVANT KEYWORDS FOR ATS (Applicant Tracking Systems)

Software-Defined Radio, SDR, BladeRF, GNU Radio, Python, PyQt5, BPSK, FM Modulation, Forward Error Correction, FEC, Convolutional Coding, CRC, Digital Signal Processing, DSP, RF Engineering, Wireless Communication, Real-Time Systems, Embedded Systems, SoapySDR, Signal Processing, Synchronization, Modulation, Demodulation, Hardware Integration, GUI Development, Error Correction, Encryption, State Machine, FFT, Spectrum Analysis, ISM Band, Communication Systems, Transceiver, Sample Rate Conversion, Filtering, Costas Loop, Symbol Synchronization, Base64, Git, Linux

---

## PROJECT METRICS

- **Duration:** 3-4 months full-time equivalent
- **Code:** 5,000+ lines of Python
- **Documentation:** 50+ pages
- **Modules:** 3 complete systems
- **File Types Supported:** Text, JPEG, WAV
- **Transmission Success Rate:** 100% with error correction
- **Real-Time Latency:** <100ms for audio
- **Repository Size:** ~5.8 MB (including sample files)
- **Commits:** Multiple with version control

---

## HOW TO USE THIS DOCUMENT

1. **For Project Section:** Use the "Condensed Technical Description" as your main project paragraph
2. **For Bullet Points:** Select 2-4 bullet points from "Example CV Bullet Points" based on the job role
3. **For Skills Section:** Extract relevant keywords from "Technical Skills Demonstrated"
4. **For Interview:** Reference "Key Accomplishments" and "Technical Specifications" for detailed discussions
5. **For Portfolio:** Link to GitHub repository with the full README and presentation PDF

---

## SUGGESTED CV FORMAT

**Project Title:** End-to-End Software-Defined Radio Communication System

**Technologies:** Python, GNU Radio, BladeRF SDR, PyQt5, BPSK/FM Modulation, FEC, DSP

**Description:** [Use "Condensed Technical Description" above - 100-150 words]

**Key Achievements:**
- [Select 2-4 relevant bullets from "Key Accomplishments"]

**GitHub:** https://github.com/LasiduDilshan/Software-Defined-Radio

---

*This condensed summary is optimized for CV/resume inclusion. Use the detailed PROJECT_DESCRIPTION_FOR_CV.md file for comprehensive technical discussions during interviews.*
