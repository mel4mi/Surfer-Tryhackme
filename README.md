# Surfer-TryHackMe
Exploit for the Surfer room in TryHackMe. Written in Python 3.10

Requirements:
```
pip install -r requirements.txt
```
Please replace the IP values in "exploit.py" and "main.py" with your target IP
```
ip = "your_target_ip"
```
## Check login
To verify successful login on the site:

```
python main.py
```
Expected output format:

```
626a3f263723cc4e3f0e43355da54a95
```
## Exploit
To run the exploit:
```
python exploit.py
```

Note: The program does not automatically stop after finding the flag. Please keep your eyes on the screen :)

Expected Result:

![Image](/photo.png)

