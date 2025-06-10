# MediSight
MediSight is a multimodal AI system that extracts, summarizes, and explains medical documents such as lab reports, prescriptions, and discharge summaries. It supports document upload (PDF/image), OCR, structured extraction, layman translation, and interactive question answering.

## 🚀 Features

- 📄 **PDF/Image Upload**: Accepts medical documents in PDF or image format.
- 🧾 **OCR & Layout Parsing**: Uses LayoutLM/Donut for document understanding.
- ✂️ **Entity Extraction**: Extracts patient info, medications, and medical terms.
- 🧠 **Summarization**: Summarizes medical content into readable insights.
- 🗣️ **Layman Explanation**: Translates jargon into everyday language.
- 💬 **Visual Q&A**: Answer natural-language questions about uploaded documents.
- 🖥️ **Web UI**: Simple, clinician-friendly interface built with React.

---

## 🛠️ Tech Stack

- **Frontend**: React + TailwindCSS
- **Backend**: FastAPI + Python
- **Models**: Hugging Face Transformers (LayoutLMv3, BART, T5, Donut)
- **OCR**: Tesseract / PaddleOCR
- **Audio (Future)**: Whisper / SpeechBrain
- **Deployment**: Docker + Hugging Face Spaces (demo)
