# Python Downloads Janitor 
**"If you do it twice, automate it."**

The **Python Downloads Janitor** is a lightweight, efficient automation script designed to triage and organize chaotic directories. Originally built to handle a "Downloads" folder that had accumulated 184+ files over several months, this tool applies the SOC (Security Operations Center) mindset of **Visibility and Order** to personal file management.

Note: While I originally built this tool to solve my own chaos on *Ubuntu*, I believe a tool is only truly "cool" if everyone can use it. I have since updated the logic to be fully cross-platform, supporting **Windows, Linux, and macOS**.

---

## The Problem
As a Cybersecurity student, my workspace moves fast. Between packet captures, research PDFs, and security scripts, my Downloads folder quickly became a digital graveyard. 
* **The Mess:** 184 files of mixed types.
* **The Risk:** Reduced visibility and wasted time searching for critical lab resources.
* **The Manual Fix:** ~2 hours of dragging and dropping.
* **The Python Fix:** < 1 second of execution.

---

## How It Works
The script utilizes the Python Standard Library to perform a "Search and Triage" operation:

1. **`Pathlib` Library:** Modern, object-oriented path handling that automatically detects your OS (Windows \ vs Linux /).
2. **`shutil` Library:** Provides the "muscle" to move files securely across the file system.
3. **Normalization:** Uses .lower() to ensure file extensions are identified regardless of case-sensitivity—a key practice in identifying obfuscated files.
4. **Self-Healing Logic:** The script checks if destination folders (Documents, Images, Scripts, Archives) exist. If they don't, it creates them on the fly before moving data.

---

### Categorization Logic:
* **Documents:** `.pdf`, `.docx`, `.txt`, `.pptx`, `.csv`, `.xlsx`
* **Images:** `.jpg`, `.png`, `.jpeg`, `.svg`, `.webp`
* **Scripts:** `.py`, `.sh`, `.bin`, `.deb`
* **Archives:** `.zip`, `.tar`, `.gz`, `.7z`
* **Others:** Acts as a Quarantine/Sandbox for unknown file types that require manual review.

---

## Performance Metrics
* **Files Processed:** 184
* **Execution Time:** ~0.04 seconds
* **Human Effort Saved:** 100%

---

## Installation & Usage
1. Clone the repository:
```bash
git clone https://github.com/TechOunik/python-downloads-janitor.git
```

2. Navigate to the folder:
```bash
cd python-downloads-janitor
```

3. Run the script:
(The script uses Path.home() to automatically find your profile on any Linux, Mac, or Windows system)
```bash
python3 organize_downloads.py
```
--- 

## The Blue Team Perspective
In cybersecurity, visibility is the foundation of defense. You cannot protect what you cannot find. This project demonstrates three core SOC principles:

* **Automation:** Eliminating manual toil to focus on high-value analysis.
* **Data Triage:** Categorizing assets for faster incident response.
* **Hygiene:** Maintaining a predictable, clean environment to make anomalies easier to spot.


### The Story Behind the Script
I wrote a detailed technical walkthrough on Medium about the "breaking point" that led to this project and how my background in Software Engineering informs my journey into Cybersecurity.
👉 [Read the Medium Article Here](https://medium.com/@obiomauzoh16/the-184-file-breaking-point-how-i-used-python-to-cure-my-chronic-downloads-chaos-8f4d2f19e5b6)

## Connect with the Architect
* LinkedIn: [Obioma Felicity Uzoh](www.linkedin.com/in/felicityuzoh)
* Portfolio: [TechOunik](https://techounik.github.io/techounik/)

```Created with resilience and a love for clean code by Obioma - Final Year Cybersecurity Student.```

