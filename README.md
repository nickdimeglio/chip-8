
CHIP-8 is an interpreted programming language developed by Joseph Weisbecker in the late 1970s. Initially used on the COSMAC VIP and Telmac 1800 8-bit microcomputers, Weisbecker designed CHIP-8 to allow video games to be programmed once and then run on an assortment of platforms. 

The CHIP-8 interpreter is essentially a virtual machine with 4K memory consisting of main memory, 16 registers, a stack, two timers, input/output with graphics and sound, and a font set. Programs are written for CHIP-8 using a set of 35 hexadecimal opcodes. The op codes manipulate the memory and registers to let users play their favorite games. 

Here's a CHIP-8 code snippet from CHIP-8.com:

                    0x00E0             // Clear the Screen.
                    0x6A00             // Set the X co-ordinate to 00H.
                    0x6B00             // Set the Y co-ordinate to 00H.
                    0x2400             // Draw SPRITE.
                    0x2500             // Keep on the Screen for a moment.
                    0x2400             // Erase the Sprite. (XOR with the previously drawn Sprite).
  
