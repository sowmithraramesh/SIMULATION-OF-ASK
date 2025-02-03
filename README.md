

---

# Simulation of Digital Modulation Schemes

## Aim:
To study:
- a) **Scilab Simulation** for digital modulation techniques
- b) **Python Simulation** for digital modulation techniques

## Software Required:
- **Scilab** / **Python**

---

## Procedure:

### 1. **Scilab Simulation for Digital Modulation Techniques**:

#### Step 1: **Generate a Message Signal**
- Create a message signal to modulate. This can be a random binary signal or a continuous analog signal.
- The message signal is usually a low-frequency signal that will be modulated onto a carrier wave.

#### Step 2: **Modulate the Message Signal**
- Use digital modulation techniques such as **Binary Phase Shift Keying (BPSK)**, **Binary Frequency Shift Keying (BFSK)**, **Amplitude Shift Keying (ASK)**, or **Quadrature Amplitude Modulation (QAM)**.
- Modulate the message signal using the chosen modulation method.

#### Step 3: **Plot the Modulated Signal**
- Plot the modulated signal and display its characteristics, such as the carrier frequency, modulation depth, and signal amplitude.

#### Step 4: **Demodulate the Signal**
- Implement the corresponding demodulation scheme (such as coherent detection or non-coherent detection).
- Compare the demodulated signal with the original message signal to assess the quality of the modulation technique.

#### Step 5: **Observe the Results**
- Display the modulated and demodulated signals. Analyze the performance of each modulation technique under different conditions such as noise or signal attenuation.

---

### 2. **Python Simulation for Digital Modulation Techniques**:

#### Step 1: **Generate a Message Signal**
- Create a message signal, which can be a binary or continuous signal.
- You can use random number generation or predefined data for the message signal.

#### Step 2: **Modulate the Message Signal**
- Use a modulation technique (BPSK, BFSK, ASK, QAM, etc.) to modulate the message signal onto a carrier.
- For example, for **BPSK**, modulate the binary data by shifting the phase of a sinusoidal carrier.

#### Step 3: **Plot the Modulated Signal**
- Plot the modulated signal over time, showing how the carrier signal varies with respect to the message signal.

#### Step 4: **Add Noise (optional)**
- You can add noise (such as Gaussian noise) to the modulated signal to simulate real-world conditions.
- This step helps in evaluating the performance of the modulation technique under noise.

#### Step 5: **Demodulate the Signal**
- Implement the demodulation algorithm corresponding to the modulation technique.
- Evaluate the recovery of the original message signal and compare the demodulated signal to the transmitted signal.

#### Step 6: **Visualize the Results**
- Plot the original, modulated, and demodulated signals.
- Analyze the effect of noise and the quality of demodulation.

---

##  Output:

- ![image](https://github.com/user-attachments/assets/7740ddac-3ea5-4236-a441-8cf45b4d693e)

  
- **Python Output**:
    
![image](https://github.com/user-attachments/assets/a878f5b7-c4a9-451f-8153-039df73ed8d7)

---

## Result:

- **Analysis of Modulation Techniques**:
    - Digital modulation schemes allow efficient use of the available bandwidth in communication systems.
    - By comparing the modulated and demodulated signals, the effectiveness of each modulation technique can be observed.
    - The performance of different modulation schemes can be evaluated in terms of:
      - **Bandwidth efficiency**
      - **Power efficiency**
      - **Susceptibility to noise and signal degradation**
    - Techniques such as BPSK, ASK, and BFSK each have specific advantages depending on the application.
  
- **Key Findings**:
    - **BPSK**: Simple and efficient, but susceptible to noise.
    - **ASK**: Useful in low-frequency applications but is affected by amplitude variations due to noise.
    - **BFSK**: Robust against noise but requires more bandwidth.
    - **QAM**: Provides high data rates but is more susceptible to noise, requiring better signal conditions.

By simulating these techniques in Scilab and Python, we can gain insights into their performance and how to choose the best technique for different communication scenarios.

---

