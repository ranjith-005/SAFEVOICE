# 🎙️ SAFE-VOICE  
### Multilingual Code-Switched Speech Moderation & Safe Text-to-Speech System for Indian Languages


::contentReference[oaicite:0]{index=0}


---

## 📌 Overview

SAFE-VOICE is an end-to-end speech AI system designed for multilingual Indian environments, where users naturally communicate using a mix of regional languages and English. Traditional speech systems often assume single-language input and fail to handle code-switched speech or ensure safety in spoken interactions. SAFE-VOICE addresses these challenges through a production-style, responsible AI pipeline.

The system automatically detects spoken languages, handles code-switched speech across English and South Indian languages, transcribes audio using language-aware ASR models, and performs severity-based hate and abusive speech detection. A decision engine ensures that harmful content is blocked or neutralized before generating safe, language-specific text-to-speech output.

---

## 🚩 Problem Statement

In India, spoken communication frequently involves code-switching between regional languages and English. Most existing speech systems:
- Assume single-language input
- Perform poorly on code-switched speech
- Lack mechanisms to detect spoken hate or abusive content
- Risk repeating harmful speech through TTS systems

These limitations make them unsuitable for real-world deployment in voice assistants, IVR systems, and public-facing speech platforms.

---

## ✅ Solution

SAFE-VOICE provides a unified pipeline that:
1. Detects the spoken language(s) from raw audio  
2. Handles code-switched speech using segment-level language identification  
3. Transcribes speech using language-specific ASR models  
4. Classifies content into SAFE, MILD_ABUSE, or SEVERE_HATE  
5. Applies policy-based moderation decisions  
6. Generates safe, language-aware speech output  

---

## 🌐 Supported Languages

- English  
- Tamil  
- Telugu  
- (Architecture supports easy extension to Kannada and Malayalam)

---

## 🧠 System Architecture

Audio Input
↓
Audio Segmentation (for code-switching)
↓
Segment-level Language Identification
↓
Language-specific ASR
↓
Merged Transcription
↓
Severity-based Hate Speech Detection
↓
Decision Engine
↓
Safe Language-Aware TTS Output


---

## 🔧 Core Modules

### 1️⃣ Language Identification (LID)
- Detects language at segment level
- CNN + BiLSTM using MFCC features
- Metric: Accuracy

### 2️⃣ Automatic Speech Recognition (ASR)
- Language-aware routing
- Whisper-based baseline
- Metric: Word Error Rate (WER)

### 3️⃣ Hate / Abusive Speech Detection
- Multilingual transformer-based classifier
- Severity levels:
  - SAFE
  - MILD_ABUSE
  - SEVERE_HATE
- Metric: Precision, Recall, F1-score

### 4️⃣ Decision Engine
| Severity | System Action |
|--------|---------------|
| SAFE | Normal TTS output |
| MILD_ABUSE | Warning message |
| SEVERE_HATE | Blocked with safety notice |

### 5️⃣ Text-to-Speech (TTS)
- Language-specific neural TTS models
- Generates safe speech in detected language
- Metric: Mean Opinion Score (MOS)

---

# 🎙️ SAFE-VOICE  
### Multilingual Code-Switched Speech Moderation & Safe Text-to-Speech System for Indian Languages


::contentReference[oaicite:0]{index=0}


---

## 📌 Overview

SAFE-VOICE is an end-to-end speech AI system designed for multilingual Indian environments, where users naturally communicate using a mix of regional languages and English. Traditional speech systems often assume single-language input and fail to handle code-switched speech or ensure safety in spoken interactions. SAFE-VOICE addresses these challenges through a production-style, responsible AI pipeline.

The system automatically detects spoken languages, handles code-switched speech across English and South Indian languages, transcribes audio using language-aware ASR models, and performs severity-based hate and abusive speech detection. A decision engine ensures that harmful content is blocked or neutralized before generating safe, language-specific text-to-speech output.

---

## 🚩 Problem Statement

In India, spoken communication frequently involves code-switching between regional languages and English. Most existing speech systems:
- Assume single-language input
- Perform poorly on code-switched speech
- Lack mechanisms to detect spoken hate or abusive content
- Risk repeating harmful speech through TTS systems

These limitations make them unsuitable for real-world deployment in voice assistants, IVR systems, and public-facing speech platforms.

---

## ✅ Solution

SAFE-VOICE provides a unified pipeline that:
1. Detects the spoken language(s) from raw audio  
2. Handles code-switched speech using segment-level language identification  
3. Transcribes speech using language-specific ASR models  
4. Classifies content into SAFE, MILD_ABUSE, or SEVERE_HATE  
5. Applies policy-based moderation decisions  
6. Generates safe, language-aware speech output  

---

## 🌐 Supported Languages

- English  
- Tamil  
- Telugu  
- (Architecture supports easy extension to Kannada and Malayalam)

---

## 🧠 System Architecture

Audio Input
↓
Audio Segmentation (for code-switching)
↓
Segment-level Language Identification
↓
Language-specific ASR
↓
Merged Transcription
↓
Severity-based Hate Speech Detection
↓
Decision Engine
↓
Safe Language-Aware TTS Output


---

## 🔧 Core Modules

### 1️⃣ Language Identification (LID)
- Detects language at segment level
- CNN + BiLSTM using MFCC features
- Metric: Accuracy

### 2️⃣ Automatic Speech Recognition (ASR)
- Language-aware routing
- Whisper-based baseline
- Metric: Word Error Rate (WER)

### 3️⃣ Hate / Abusive Speech Detection
- Multilingual transformer-based classifier
- Severity levels:
  - SAFE
  - MILD_ABUSE
  - SEVERE_HATE
- Metric: Precision, Recall, F1-score

### 4️⃣ Decision Engine
| Severity | System Action |
|--------|---------------|
| SAFE | Normal TTS output |
| MILD_ABUSE | Warning message |
| SEVERE_HATE | Blocked with safety notice |

### 5️⃣ Text-to-Speech (TTS)
- Language-specific neural TTS models
- Generates safe speech in detected language
- Metric: Mean Opinion Score (MOS)

---

## 🖥️ Demo (Streamlit UI)

SAFE-VOICE includes a Streamlit-based interface that allows:
- Uploading audio files
- Viewing detected language(s)
- Viewing transcription and severity classification
- Listening to safe TTS output

Run locally:
```bash
streamlit run app.py

---

## 🔧 Core Modules

### 1️⃣ Language Identification (LID)
- Detects language at segment level
- CNN + BiLSTM using MFCC features
- Metric: Accuracy

### 2️⃣ Automatic Speech Recognition (ASR)
- Language-aware routing
- Whisper-based baseline
- Metric: Word Error Rate (WER)

### 3️⃣ Hate / Abusive Speech Detection
- Multilingual transformer-based classifier
- Severity levels:
  - SAFE
  - MILD_ABUSE
  - SEVERE_HATE
- Metric: Precision, Recall, F1-score

### 4️⃣ Decision Engine
| Severity | System Action |
|--------|---------------|
| SAFE | Normal TTS output |
| MILD_ABUSE | Warning message |
| SEVERE_HATE | Blocked with safety notice |

### 5️⃣ Text-to-Speech (TTS)
- Language-specific neural TTS models
- Generates safe speech in detected language
- Metric: Mean Opinion Score (MOS)

---
🎯 Use Cases

Voice assistants for Indian users

Customer support IVR systems

Public grievance and helpline platforms

Speech moderation systems

Safe conversational AI applications

🧪 Key Contributions

Multilingual and code-switched speech handling

Severity-aware hate speech detection

Responsible AI through policy-based moderation

Modular, extensible system design

Interactive demo and evaluation framework

🚀 Future Enhancements

Kannada and Malayalam ASR/TTS models

Real-time streaming inference

Emotion-aware speech synthesis

Fine-tuning on Indic speech datasets
