# AuthCode Gen

[![Python](https://img.shields.io/badge/python-3.x-blue)](https://www.python.org/) 
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

A simple Python script that generates **TOTP (2FA) codes**.  
Think of it as a lightweight alternative to Google Authenticator — just type your secret and get your codes instantly.


## Features
- Works on **Linux, macOS, and Windows**  
- **No extra dependencies** — pure Python  
- Does **not save your secret**, so it stays private  
- Small, fast, and easy to run


## How it Works
It uses the standard **TOTP algorithm (RFC 6238)**.  
You give it a **Base32 secret**, it generates a **6-digit code**, and shows how many seconds are left before it refreshes.  


## Credits
Made with ❤️ by [@whoshelby](https://github.com/whoshelby)


## Note
Make sure your system clock is accurate — otherwise the codes might not match your other devices.
