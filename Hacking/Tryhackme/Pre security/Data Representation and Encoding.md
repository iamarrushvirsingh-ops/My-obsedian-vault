
## Colours 
- Colours and everything in a computer is represented as 0 and 1 's .
- You can combine 3 bits representing blue , green and red in different combinations to get all 12 shades of colours 
- And if you increase the control of shade and contrast of colour by increasing the bits used to denote it , you can represent even more shades of colour . 
- Your computer uses 24 bits to represent a standard colour , this allows for 16.7 million distinct colours .
- It uses 8 bit for each green , blue and red .

## Characters 
- Characters are just numbers with agreed meanings. That agreement is called an **encoding**
- One of the earliest standards for encoding english letters was ASCII .
- ASCII stands for American Standard Code for Information Interchange
- And it is an early character encoding from 1963 that uses numbers 0-127 to represent English letters, digits, punctuation, and some control characters.
- While saving a file or performing a operation in programing , usualy at the bit level , the system adds a new line `\n` as default measures .
- Because reading binary numbers is cumbersome and error-prone for us, we prefer to use hexadecimal digits.
- We group 4 bits into a single hexadecimal digit.
- It is uncommon to use decimal digits.
- It is more common to use hexadecimal digits when we want to show the bits.
- But the problem was that ASCII did'nt help with other european languages .
- So the ISO/IEC 8859 Series (International Standards) created several standards; each standard covered a set of languages:

- **ISO-8859-1 (Latin-1)**: Covered **Western European languages** like German (ß, ü), French (é, ç), Spanish (ñ, ¿), Italian, Portuguese, Catalan, and Nordic languages (e.g., Icelandic ð/Ð). Check this [link(opens in new tab)](https://www.charset.org/charsets/iso-8859-1).
- **ISO-8859-2 (Latin-2)**: Supported **Central/Eastern European languages** like Polish (ł, ń), Czech (č, ř), Hungarian (ő, ű), Croatian (đ), Romanian (ș, ț), and Slovak. Check this [link(opens in new tab)](https://www.charset.org/charsets/iso-8859-2).

- So if your document is saved using ISO-8859-1 and later read and displayed as if it were saved using ISO-8859-2, non-English letters are likely to be displayed differently.

#unicode
- Unicode is a universal character encoding standard. 
- It assigns unique code points to characters from all modern and historical writing systems worldwide.
- Unicode supports the interchange, processing, and display of text in diverse languages
#utf-8
- This is very common for the web .
- It dynamically allots bits to a character . Based on need . 
- It allots bits between 1 to 4 as per need . 
#utf-16
- It uses either 2 or 4 bits for characters .
- Sometimes we club multiple bits to represent emojis . 
#utf-32
- It assigns 4 bits to everything .
- This is where the most bit wastage happens .
- 