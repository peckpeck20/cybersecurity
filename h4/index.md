# H4 Some Disassembly Required

## X - Summary
- Idapro & Ghidra lets the user break down a programs executable into C code
- There are also lower level CLI tools such as ltrace & strace which give a glance of what the executable is doing, showing reading and writing operations
- Ghidra is an extensive tool, overall it's easy to pick up and debug code
- Although the code is in C, with the enhanced IDE the tool offers, its possible to follow, rename and ultimately understand what the code is actually doing and how it's being executed
## A - install Ghidra
https://github.com/NationalSecurityAgency/ghidra?tab=readme-ov-file#install

## B - rever-C

Get binary
```
wget https://terokarvinen.com/loota/yctjx7/ezbin-challenges.zip  
```
Enter executable directory & run
```
./packd
```
![Pasted image 20260208160800](Pasted%20image%2020260208160800.png)
Copy executable input string `What's the password`

Open and view executable in code editor - the input string can be seen and parts of the password as well. A link to the UPX executable packer is available.
![Pasted image 20260208173256](Pasted%20image%2020260208173256.png)
Unpack the executable

![Pasted image 20260208173626](Pasted%20image%2020260208173626.png)

Open unpacked executable in IDE
![Pasted image 20260208173719](Pasted%20image%2020260208173719.png)

Password and flag found
```
What's the password?
piilos-AnAnAs
Yes! That's the password. FLAG{Tero-0e3bed0a89d8851da933c64fefad4ff2}
```
