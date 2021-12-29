
# CHIP-8 Programming Language Interpreter/Emulator

CHIP-8 is an interpreted programming language developed by Joseph Weisbecker in the late 1970s. Weisbecker designed CHIP-8 to allow video games to be programmed once and then run on an assortment of 8-bit microcomputers. As such, the CHIP-8 interpreter takes the form of a hardware emulator, even though an actual CHIP-8 console never existed. 
 
Programs were written for the CHIP-8 console were always run on 8-bit computers emulating the CHIP-8 console (like the COSMAC VIP or Telmac 1800). The virtual console consists of 4K main memory, 16 registers, a stack, two timers, input/output with graphics and sound, and a font set. Programs are written for CHIP-8 using a set of 35 hexadecimal opcodes. For a detailed language specification, check out [CowGod's CHIP-8 Technical Reference](http://devernay.free.fr/hacks/chip8/C8TECH10.HTM#3.0). Here's a code snippet from CHIP-8.com:
```
                    0x00E0             // Clear the Screen.
                    0x6A00             // Set the X co-ordinate to 00H.
                    0x6B00             // Set the Y co-ordinate to 00H.
                    0x2400             // Draw SPRITE.
                    0x2500             // Keep on the Screen for a moment.
                    0x2400             // Erase the Sprite. (XOR with the previously drawn Sprite).
```  
