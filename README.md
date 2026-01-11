# 🎙️ SAFE-VOICE  
### Multilingual Code-Switched Speech Moderation & Safe Text-to-Speech System for Indian Languages


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

## 🧠 System Architecture

```mermaid
flowchart TD
    A[Audio Input (.wav / Microphone)] --> B[Audio Preprocessing]
    B --> C[Audio Segmentation]

    C --> D[Segment-level Language Identification]
    D -->|English| E1[English ASR]
    D -->|Tamil| E2[Tamil ASR]
    D -->|Telugu| E3[Telugu ASR]
    D -->|Kannada| E4[Kannada ASR]
    D -->|Malayalam| E5[Malayalam ASR]

    E1 --> F[Merged Transcription]
    E2 --> F
    E3 --> F
    E4 --> F
    E5 --> F

    F --> G[Severity-based Hate Speech Detection]
    G --> H[Decision Engine]

    H -->|SAFE| I[Language-aware TTS]
    H -->|MILD_ABUSE| J[Warning Response TTS]
    H -->|SEVERE_HATE| K[Blocked Safety Message]

    I --> L[Audio Output]
    J --> L
    K --> L

🔹 **GitHub will render this automatically**  
🔹 No plugins, no screenshots needed  

---

## 🧠 HOW YOU EXPLAIN THIS DIAGRAM IN INTERVIEW (MEMORIZE)

> “The system first preprocesses and segments audio, performs segment-level language identification, routes each segment to language-specific ASR models, merges the transcription, applies severity-based hate speech detection, and finally generates a safe, language-aware TTS response.”

That explanation alone sounds **industry-grade**.

---

## ✅ OPTION 2: SIMPLE ASCII DIAGRAM (Fallback)

Use this **only if Mermaid is not rendering** (rare).

```markdown
## 🧠 System Architecture

Audio Input
   |
   v
Audio Preprocessing
   |
   v
Audio Segmentation
   |
   v
Language Identification
   |
   v
Language-specific ASR
   |
   v
Merged Transcription
   |
   v
Hate Speech Detection (Severity-based)
   |
   v
Decision Engine
   |
   v
Safe Text-to-Speech Output


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

