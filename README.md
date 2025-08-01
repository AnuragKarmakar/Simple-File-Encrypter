# 🔐 Simple File Encryptor & Decryptor (Python CLI)

A lightweight command-line tool that encrypts and decrypts any file using a simple XOR-based method and a numeric key. Useful for basic file obfuscation and as a learning project to understand byte-level operations.

> ⚠️ This is **not** secure for real-world encryption. It's a demonstration of XOR encryption for educational use only.

---

## 🧠 How It Works

This script uses a **bitwise XOR operation** to modify each byte of the file with a user-provided key between 1 and 255. The same function is used for both encryption and decryption due to the reversible nature of XOR.

---

## 📂 Features

- ✅ Encrypt any file (text, images, binaries, etc.)
- ✅ Decrypt previously encrypted files with the correct key
- ✅ Clear terminal before starting
- ✅ Progress display (with optional time delay)
- ✅ Simple and readable Python code
- ⚠️ Adds `"CC-"` prefix to encrypted filenames to avoid overwriting

---

## 🛠️ Technologies

- Python 3.x
- Built-in modules only (`os`, `time`)

---

## 🚀 Usage

### 🔧 Run the Script
```bash
python encryptor.py
