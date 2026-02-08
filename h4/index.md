# H4 Some Disassembly Required

## X - Summary
- Idapro & Ghidra lets the user break down a programs executable into C code
- There are also lower level CLI tools such as ltrace & strace which give a glance of what the executable is doing, showing reading and writing operations
- Ghidra is an extensive tool, overall it's easy to pick up and debug code
- Although the code is in C, with the enhanced IDE the tool offers, its possible to follow, rename and ultimately understand what the code is actually doing and how it's being executed
## A - install Ghidra
https://github.com/NationalSecurityAgency/ghidra?tab=readme-ov-file#install

## B - Rever-C

Get binary
```
wget https://terokarvinen.com/loota/yctjx7/ezbin-challenges.zip  
```
Enter executable directory & run
```
./packd
```
![](images/1.png)

Copy executable input string `What's the password`

Open and view executable in code editor - the input string can be seen and parts of the password as well. A link to the UPX executable packer is available.
![Pasted image 20260208173256](images/2.png)
Unpack the executable

![Pasted image 20260208173626](images/Pasted%20image%2020260208173626.png)

Open unpacked executable in IDE
![Pasted image 20260208173719](images/Pasted%20image%2020260208173719.png)

Password and flag found
```
What's the password?
piilos-AnAnAs
Yes! That's the password. FLAG{Tero-0e3bed0a89d8851da933c64fefad4ff2}
```

## C - If backwards

Get binary

```
wget https://terokarvinen.com/loota/yctjx7/ezbin-challenges.zip  
```

Enter executable directory & run

```
./passtr
```

Navigate to your local Ghidra directory & start
```
./ghidraRun
```
Create new project & click on green dragon then import binary
![Pasted image 20260208160052](images/Pasted%20image%2020260208160052.png)
select and run analysis
![Pasted image 20260208160155](images/Pasted%20image%2020260208160155.png)
The main function can be observed
![Pasted image 20260208195630](images/Pasted%20image%2020260208195630.png)
Hack: Patch instruction in Ghidra by changing the conditional IF statement to return a false value when the correct password is inputted. By changing the assembly entry to from `JNZ`->  `JZ`
![Pasted image 20260208195808](../Pasted%20image%2020260208195808.png)
Save patched executable by going to File -> Export program
![Pasted image 20260208200205](../Pasted%20image%2020260208200205.png)

Test setup
```
# Apply executable permissions to file
sudo chmod +x passtr_patched
# run
./passtr_patched
```

Result
![Pasted image 20260208200419](../Pasted%20image%2020260208200419.png)