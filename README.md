![Alt text](https://github.com/xdityagr/SHIELD/blob/main/Images/SHIELD_banner.png?raw=true "Banner Image")
# SHIELD
SHIELD (System for Halting Illegal Exploitation & Ensuring Lasting Defense) is an AI and IoT-powered system designed to combat human trafficking, with a strong focus on safeguarding women and children. It integrates AI-driven facial recognition, RFID wearables, Zigbee-based communication, ESP32/Arduino hardware, and advanced biometric techniques such as iris scanning for enhanced victim identification.  

---

## Features  

- **AI-Powered Facial Recognition**  
  - One-image recognition technology for real-time identification.  
  - Optimized for low-power IoT nodes integrated with CCTV networks.  

- **Iris Scanning Technology (New Feature)**  
  - Software-integrated biometric verification using iris recognition.  
  - Ensures higher accuracy when facial features are obscured or altered.  

- **RFID Wearables**  
  - Rings, bracelets, and shoes embedded with RFID modules for vulnerable individuals.  
  - Provides reliable tracking even if facial identification is not possible.  

- **Wireless Sensor Network (WSN)**  
  - Smart nodes (ESP32, Arduino, Zigbee modules) form a mesh topology.  
  - Nodes transmit processed detection data securely to the Cluster-head Console.  

- **Cluster-Head Console (GUI)**  
  - Built with PySide6 for a user-friendly interface.  
  - Provides real-time alerts, victim location, and live tracking.  
  - Enables command of nearby nodes by elevating them into high-alert mode.  

- **Secure Communication**  
  - AI-driven dynamic encryption for secure transmission of sensitive data.  
  - Protects against unauthorized access or data misuse.  

- **Continuous Learning**  
  - Machine learning algorithms continuously refine recognition accuracy.  
  - Adapts to real-world conditions and emerging threats.  

---

## Technology Stack  

### Hardware  
- ESP32 (IoT microcontroller)  
- Arduino Uno (Prototyping and control)  
- RFID Modules (RC522)  
- Zigbee Module (WSN communication)  
- Camera Modules (for facial and iris recognition)  

### Software  
- Python (backend AI logic and data processing)  
- Embedded C (hardware programming for ESP32 and Arduino)  
- PySide6 (GUI framework for the console)  
- Deep Learning Models (facial recognition and iris scanning)  
- AI-Driven Encryption Algorithms (secure communication)  

---

## System Workflow  

1. Complaint/FIR is filed → victim details (photo, iris scan, description) uploaded to SHIELD software.  
2. Data is distributed across IoT-enabled camera and RFID nodes.  
3. Nodes perform real-time facial and iris recognition, along with RFID detection.  
4. Upon match, node ID and location are transmitted to the Cluster-head Console.  
5. Nearby nodes enter high-alert mode for continuous tracking.  
6. Law enforcement receives real-time updates, enabling rapid intervention.  

---

## Screenshots  

<div style="display: flex; flex-wrap: wrap; gap: 10px;">
    <img src="https://github.com/xdityagr/SHIELD/blob/main/preview/ShieldConsoleScreenshot (2).png" width="50%">
    <img src="https://github.com/xdityagr/SHIELD/blob/main/preview/ShieldConsoleScreenshot (3).png" width="50%">
    <img src="https://github.com/xdityagr/SHIELD/blob/main/preview/ShieldConsoleScreenshot (4).png" width="50%">
    <img src="https://github.com/xdityagr/SHIELD/blob/main/preview/ShieldConsoleScreenshot (1).png" width="50%">
</div>

## Future Scope  

- Scale deployment nationwide by leveraging existing Smart City CCTV infrastructure.  
- Enhance iris recognition under low-light and crowded conditions.  
- Apply predictive analytics to detect and prevent trafficking hotspots.  
- Collaborate with government agencies and NGOs for broader implementation.  

---

Developed by **Aditya Gaur**, Made with <3 In India!

