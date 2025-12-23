# End-to-End Software-Defined Radio Communication System
## Detailed Project Description for CV

---

## PROJECT OVERVIEW

Developed a comprehensive end-to-end communication system using Software-Defined Radio (SDR) technology, specifically implementing BladeRF hardware with GNU Radio software framework. The project demonstrates mastery of digital signal processing, RF communications, encryption techniques, and real-time system design across three major communication modules.

---

## TECHNICAL ARCHITECTURE

### Hardware Platform
- **BladeRF SDR Device**: Full-duplex software-defined radio transceiver
- **Operating Frequency Range**: 300 MHz - 3.8 GHz
- **Sample Rate**: Up to 40 MSPS (Mega Samples Per Second)
- **Transmission Power**: Configurable gain control (17-73 dB)

### Software Framework
- **GNU Radio 3.10.1.1**: Open-source software development toolkit for signal processing
- **Python 3.x**: Primary programming language for DSP algorithms
- **PyQt5**: GUI development for real-time visualization and control
- **SoapySDR**: Hardware abstraction layer for SDR device integration

---

## MODULE 1: DIGITAL COMMUNICATION SYSTEM WITH PREAMBLE HANDLING

### Purpose
Implemented a robust digital communication system capable of transmitting any type of data (text, images, audio, etc.) with error correction and synchronization mechanisms.

### Technical Implementation

#### Signal Processing Chain
1. **File Input & Encoding**
   - Custom embedded Python block for file reading and packet creation
   - Base64 encoding for binary data representation
   - Tagged stream architecture for packet boundary identification
   - State machine implementation (IDLE, PREAMBLE, DATA, FILENAME states)

2. **Forward Error Correction (FEC)**
   - Convolutional encoding with configurable polynomials
   - Code rate optimization for reliability vs. bandwidth trade-off
   - Viterbi decoding at receiver for error correction

3. **Modulation Scheme**
   - Binary Phase Shift Keying (BPSK) modulation
   - Differential encoding to resolve phase ambiguity
   - Symbol mapping and constellation design

4. **Synchronization & Recovery**
   - Symbol timing synchronization using Costas loop
   - Carrier phase recovery for coherent demodulation
   - Preamble/postamble detection for frame synchronization

5. **Data Integrity**
   - Cyclic Redundancy Check (CRC32) for error detection
   - Bit packing/unpacking for efficient transmission
   - Custom preamble stripping algorithm for post-processing

#### Channel Modeling
- Simulated real-world propagation effects (noise, frequency offset, multipath)
- AWGN (Additive White Gaussian Noise) channel implementation
- Frequency offset and timing error simulation

#### Visualization
- Real-time FFT spectrum display
- Constellation diagram monitoring
- Time-domain waveform analysis
- QT GUI sinks for comprehensive signal monitoring

### Key Scripts
- `digital_communication.py`: Main GNU Radio flowgraph (17,190 bytes)
- `digital_communication_epy_block_0.py`: Custom embedded Python block for packet handling
- `strip_preamble.py`: Post-processing script for preamble removal and Base64 decoding
- `digital communication.grc`: GNU Radio Companion flowgraph file (28,842 bytes)

### Performance Characteristics
- Supports transmission of text, image (JPEG), and audio (WAV) files
- Automatic file type detection and handling
- Reliable data recovery with error correction
- Configurable modulation parameters for different channel conditions

---

## MODULE 2: ENHANCED DIGITAL COMMUNICATION WITH BYTE STREAM APPROACH

### Purpose
An evolved version of Module 1 with improved efficiency using byte stream to tagged stream conversion methodology.

### Technical Improvements
- Streamlined data flow architecture
- More efficient memory management for large file transfers
- Optimized tagged stream approach reducing processing overhead
- Same reliable FEC and modulation schemes as Module 1

### Implementation Difference
- Replaced file source with byte stream approach
- Enhanced packet handling for reduced latency
- Maintained backward compatibility with encryption/decryption modules

### Usage Workflow
1. Encrypt input file using `Encrypt.py`
2. Execute `digital communication.grc` for transmission/reception
3. Decrypt output file using `Decrypt.py`

---

## MODULE 3: REAL-TIME ANALOG AUDIO TRANSMISSION SYSTEM

### Purpose
Developed a real-time voice communication system using analog Frequency Modulation (FM) to demonstrate mastery of analog communication techniques and avoid synchronization challenges inherent in digital systems.

### Technical Implementation

#### Audio Processing Pipeline
1. **Audio Input**
   - WAV file source (supports 44.1 kHz standard audio)
   - Real-time streaming capability
   - Buffer management for continuous playback

2. **Signal Processing**
   - Dynamic volume control with GUI slider (0-10 range)
   - Sample rate conversion using rational resampler (interpolation: 500, decimation: 11)
   - Audio signal conditioning and filtering

3. **Modulation**
   - Narrowband FM (NBFM) transmission
   - Audio rate: 44.1 kHz
   - Quadrature rate: 88.2 kHz (2x audio rate)
   - Maximum frequency deviation: 1 kHz
   - Pre-emphasis time constant: 75 μs (North American standard)

4. **RF Transmission**
   - Carrier frequency: 433 MHz (ISM band)
   - Sample rate: 4 MSPS
   - Bandwidth: Full duplex capable
   - Gain: 20 dB (adjustable 17-73 dB range)

#### User Interface
- **PyQt5-based GUI** with real-time controls
- **Volume slider** for dynamic audio level adjustment
- **Time-domain visualization** showing modulated waveform
- **Frequency-domain display** (FFT spectrum analyzer)
- **Waterfall plot** for time-frequency analysis
- **Constellation diagram** for signal quality monitoring

#### Real-Time Performance
- Low-latency audio transmission
- Continuous streaming without buffer underruns
- Visual feedback for signal quality monitoring
- Graceful shutdown with settings persistence

### Key Scripts
- `real_time_fm.py`: Main application with GUI (9,202 bytes)
- `real time fm.grc`: GNU Radio Companion flowgraph (22,205 bytes)
- Test audio file: 5.3 MB WAV sample for demonstration

---

## SECURITY MODULE: XOR ENCRYPTION/DECRYPTION SYSTEM

### Purpose
Implemented a symmetric encryption system for data protection during transmission, demonstrating understanding of cryptographic principles.

### Technical Implementation

#### Encryption Algorithm
- **Method**: XOR cipher (symmetric key encryption)
- **Key**: Fixed 8-bit key (value: 122)
- **Key space**: 0-255 (single-byte)
- **Operation**: Bitwise XOR on byte array

#### Process Flow
1. Read file as binary data (supports any file type)
2. Convert to bytearray for byte-level manipulation
3. Perform XOR operation on each byte: `encrypted_byte = original_byte XOR key`
4. Write encrypted data back to file (in-place encryption)

#### Decryption Process
- Identical algorithm to encryption (XOR property: A XOR B XOR B = A)
- Same key (122) applied to decrypt
- Reversible operation maintaining data integrity

#### Supported File Types
- Text files (.txt)
- Image files (.jpeg, .jpg)
- Audio files (.wav)
- Any binary file format

### Security Considerations
- XOR encryption is suitable for educational purposes and demonstration
- Single-byte key space provides 256 possible keys
- Not recommended for production security (limited key space)
- Demonstrates understanding of encryption fundamentals and bitwise operations

### Key Scripts
- `Encrypt.py`: Encryption implementation (661 bytes)
- `Decrypt.py`: Decryption implementation (664 bytes)
- Identical scripts in both Digital Communication modules

---

## TECHNICAL SKILLS DEMONSTRATED

### Signal Processing
- Digital modulation/demodulation (BPSK)
- Analog FM modulation
- Forward Error Correction (FEC) with convolutional coding
- Symbol synchronization and timing recovery
- Carrier phase recovery (Costas loop)
- Sample rate conversion and filtering

### Software Development
- Python programming for DSP applications
- GNU Radio flowgraph design and optimization
- Object-oriented programming with GUI development
- State machine implementation
- Real-time system design
- Custom block development for GNU Radio

### RF & Communications
- Software-Defined Radio (SDR) architecture
- RF transmission and reception principles
- Channel modeling and simulation
- Frequency planning and spectrum management
- Antenna theory and propagation

### Data Processing
- Base64 encoding/decoding
- Bit packing and unpacking
- CRC error detection
- Byte stream processing
- File I/O and binary data manipulation

### User Interface Design
- PyQt5 GUI development
- Real-time visualization (FFT, constellation, waterfall)
- Interactive controls and sliders
- Event handling and signal management

---

## PROJECT DELIVERABLES

### Documentation
- Comprehensive README with component explanations
- Detailed module-specific documentation for each subsystem
- Code comments and inline documentation
- 32-page presentation PDF on Communication Design

### Source Code
- 3 complete communication system implementations
- Encryption/decryption utilities
- Custom GNU Radio blocks (embedded Python blocks)
- Post-processing scripts (preamble handling)

### Flowgraphs
- GNU Radio Companion (.grc) files for visual design
- Generated Python scripts for standalone execution
- Configurable parameters for experimentation

### Test Files
- Sample text, image, and audio files for testing
- Demonstration of multi-format data transmission
- Validation of system functionality

---

## SYSTEM INTEGRATION & WORKFLOW

### Digital Communication Workflow
1. Prepare input file (text/image/audio)
2. Apply XOR encryption for data security
3. Execute GNU Radio flowgraph for transmission
4. Receive and demodulate signal at receiver
5. Post-process with preamble stripping
6. Decrypt output file to recover original data
7. Verify data integrity

### Real-Time Audio Workflow
1. Load audio file or configure live input
2. Start GNU Radio flowgraph with GUI
3. Adjust volume and transmission parameters in real-time
4. Monitor signal quality through visualization
5. Transmit via BladeRF at 433 MHz
6. Receive and demodulate at receiver station

---

## CHALLENGES OVERCOME

1. **Synchronization in Digital Communications**
   - Implemented robust preamble detection
   - Symbol timing recovery with adaptive algorithms
   - Carrier phase ambiguity resolution

2. **Error Correction**
   - Designed FEC system with convolutional coding
   - Balanced coding gain vs. bandwidth efficiency
   - CRC implementation for data validation

3. **Real-Time Processing**
   - Managed buffer underflow/overflow conditions
   - Optimized sample rate conversions
   - Minimized latency in audio transmission

4. **Hardware Integration**
   - BladeRF driver configuration and optimization
   - SoapySDR abstraction layer implementation
   - Frequency and gain calibration

5. **Multi-Format Data Handling**
   - Universal encoding scheme (Base64)
   - File type detection and appropriate processing
   - Preserved data integrity across different formats

---

## TESTING & VALIDATION

### Functional Testing
- End-to-end data transmission verified for multiple file types
- Encryption/decryption cycle validated for data integrity
- Real-time audio transmission tested with various audio sources
- GUI responsiveness and control validation

### Performance Testing
- Bit Error Rate (BER) measurement under various SNR conditions
- Latency measurements for real-time audio
- Throughput analysis for digital data transmission
- Channel capacity evaluation

### System Integration Testing
- Complete workflow validation for all three modules
- Hardware compatibility verification with BladeRF
- Cross-platform testing (Linux environment)

---

## TECHNICAL SPECIFICATIONS SUMMARY

| Parameter | Digital Comm 1 & 2 | Real-Time Audio |
|-----------|-------------------|-----------------|
| Modulation | BPSK | NBFM |
| Sample Rate | Configurable | 4 MSPS |
| Carrier Frequency | Configurable | 433 MHz |
| FEC | Convolutional | N/A |
| Error Detection | CRC32 | N/A |
| Audio Rate | N/A | 44.1 kHz |
| Max Deviation | N/A | 1 kHz |
| Bandwidth | Variable | Narrowband |
| Data Types | Text, Image, Audio | Audio (WAV) |
| GUI | QT (monitoring) | PyQt5 (full control) |

---

## LEARNING OUTCOMES & IMPACT

### Technical Expertise Gained
- Hands-on experience with professional SDR hardware (BladeRF)
- Mastery of GNU Radio framework for communication system design
- Deep understanding of digital and analog modulation techniques
- Practical knowledge of error correction and synchronization
- Real-time signal processing and visualization

### Problem-Solving Skills
- Debugging complex RF and DSP issues
- Optimization of signal processing algorithms
- Trade-off analysis (reliability vs. efficiency)
- System-level design and integration

### Project Management
- Modular system architecture design
- Comprehensive documentation practices
- Version control and code organization
- Testing and validation methodologies

---

## POTENTIAL APPLICATIONS

1. **Emergency Communications**: Backup communication system for disaster scenarios
2. **Remote Sensing**: Telemetry and data collection from remote sensors
3. **Education**: Teaching platform for communication theory and SDR concepts
4. **Research**: Testbed for novel modulation schemes and algorithms
5. **IoT Applications**: Low-power data transmission for IoT devices
6. **Amateur Radio**: Experimentation platform for radio enthusiasts

---

## FUTURE ENHANCEMENT POSSIBILITIES

1. Implement advanced modulation schemes (QAM, OFDM)
2. Add adaptive coding and modulation (ACM)
3. Implement AES encryption for production-grade security
4. Develop mobile application for remote control
5. Add MIMO (Multiple-Input Multiple-Output) support
6. Implement automatic channel quality adaptation
7. Add digital voice codecs for compressed audio
8. Develop receiver diversity and beamforming algorithms

---

## REPOSITORY STRUCTURE

```
Software-Defined-Radio/
├── Digital Communication 1/
│   ├── digital_communication.py (17 KB)
│   ├── digital_communication_epy_block_0.py
│   ├── strip_preamble.py
│   ├── Encrypt.py
│   ├── Decrypt.py
│   ├── digital communication.grc (29 KB)
│   ├── input files (text, jpeg, wav)
│   └── README.md
├── Digital Communication 2/
│   ├── digital_communication.py (17 KB)
│   ├── digital_communication_epy_block_0.py
│   ├── Encrypt.py
│   ├── Decrypt.py
│   ├── digital communication.grc (29 KB)
│   ├── input files (text, jpeg, wav)
│   └── README.md
├── Real Time Audio/
│   ├── real_time_fm.py (9 KB)
│   ├── real time fm.grc (22 KB)
│   ├── file_example_WAV_5MG.wav (5.3 MB)
│   └── README.md
├── Encrypt.py (root level)
├── Decrypt.py (root level)
├── Communication Design project presentation.pdf (32 pages)
└── README.md (main documentation)
```

---

## TECHNOLOGIES & TOOLS USED

**Hardware:**
- BladeRF SDR (Software-Defined Radio) x40/x115

**Software & Frameworks:**
- GNU Radio 3.10.1.1
- Python 3.x
- PyQt5 (GUI development)
- SoapySDR (hardware abstraction)
- gr-osmosdr (GNU Radio blocks for SDR hardware)

**Libraries:**
- NumPy (numerical computing)
- Crypto (encryption utilities)
- base64 (data encoding)
- gnuradio.analog (analog signal processing)
- gnuradio.digital (digital modulation)
- gnuradio.fec (forward error correction)
- gnuradio.filter (signal filtering)
- gnuradio.qtgui (visualization)

**Development Environment:**
- Linux operating system
- GNU Radio Companion (visual flowgraph editor)
- Python IDE
- Git version control

**Protocols & Standards:**
- ISM Band compliance (433 MHz)
- FM broadcasting standards (75 μs pre-emphasis)
- Standard audio formats (WAV, 44.1 kHz)

---

## PROJECT TIMELINE & COMPLEXITY

**Estimated Development Time:** 3-4 months full-time equivalent

**Complexity Level:** Advanced undergraduate / Graduate level

**Lines of Code:** ~5,000+ lines (Python, flowgraph definitions, documentation)

**Documentation:** 50+ pages of comprehensive technical documentation

---

## SKILLS ALIGNMENT WITH INDUSTRY NEEDS

### Telecommunications Industry
- SDR development and deployment
- Wireless system design
- RF engineering principles
- Communication protocol implementation

### Embedded Systems
- Real-time processing
- Hardware-software integration
- Driver development and optimization

### Software Engineering
- Object-oriented design
- GUI development
- Testing and validation
- Documentation practices

### Research & Development
- Algorithm development
- Performance analysis
- System optimization
- Technical writing

---

## CONCLUSION

This project demonstrates comprehensive understanding of modern communication systems, from fundamental DSP concepts to practical hardware implementation. The three-module architecture showcases versatility in handling both digital and analog communication schemes, while the encryption component demonstrates awareness of security considerations. The complete end-to-end system, from data encoding to RF transmission and reception, represents a production-quality educational platform for Software-Defined Radio applications.

The project successfully bridges theoretical knowledge with practical implementation, utilizing industry-standard tools (GNU Radio, BladeRF) and demonstrating proficiency in signal processing, RF engineering, software development, and system integration.

---

## CONTACT & REPOSITORY

**Repository:** https://github.com/LasiduDilshan/Software-Defined-Radio
**License:** Open source
**Documentation:** Comprehensive README files and code comments
**Presentation:** 32-page technical presentation included

---

*This detailed description provides comprehensive information about the Software-Defined Radio project for CV/resume purposes. The content can be adapted and condensed as needed for specific job applications or portfolio presentations.*
