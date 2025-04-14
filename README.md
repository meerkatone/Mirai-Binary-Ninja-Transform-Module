# Mirai Binary Ninja Transform Module
Binary Ninja transform module to decrypt the obfuscated strings in the Mirai sample. Heavily inspired by, and based on the following:

Mirai_string_deobfuscation:
- https://github.com/mrphrazer/mirai_string_deobfuscation/tree/master

Example transform API plugin for Binary Ninja:
- https://gist.github.com/psifertex/6f1b0ff23bc4b09c75cd13701a5b8e04

## Mirai sample:
- https://github.com/mrphrazer/mirai_string_deobfuscation/blob/master/sample/mirai_arm

## Installation
1. Place the `mirai_tranform.py` file in your Binary Ninja plugins directory:
   - Windows: `%APPDATA%\Binary Ninja\plugins`
   - Linux: `~/.binaryninja/plugins`
   - MacOS: `~/Library/Application Support/Binary Ninja/plugins`
2. Restart Binary Ninja or reload plugins

## Usage
1. Open the Mirai sample in Binary Ninja
2. Switch to `Hex` view
3. Select the hex from `0x15fa0` to `0x16701`
4. Right Click `Transform > XOR_MIRAI`
5. Watch out for that Rick Roll URL ;-)

## References
- Binary Binja API Transform Module: https://dev-api.binary.ninja/binaryninja.transform-module.html
- Automation in Reverse Engineering: String Decryption: https://synthesis.to/2021/06/30/automating_string_decryption.html
