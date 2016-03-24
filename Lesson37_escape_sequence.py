# ~https://docs.python.org/2/reference/lexical_analysis.html

print """
Escape Sequence\tMeaning\t\t\t\t\t\t\tNotes
\\newline\tIgnored	 
\\\\\t\tBackslash (\)	 
\\'\t\tSingle quote (')	 
\\"\t\tDouble quote (")	 
\\a\t\tASCII Bell (BEL)	 
\\b\t\tASCII Backspace (BS)	 
\\f\t\tASCII Formfeed (FF)	 
\\n\t\tASCII Linefeed (LF)	 
\\N{name}\tCharacter named name in the Unicode database (Unicode only)	 
\\r\t\tASCII Carriage Return (CR)	 
\\t\t\tASCII Horizontal Tab (TAB)	 
\\uxxxx\t\tCharacter with 16-bit hex value xxxx (Unicode only)\t(1)
\\Uxxxxxxxx\tCharacter with 32-bit hex value xxxxxxxx (Unicode only)\t(2)
\\v\t\tASCII Vertical Tab (VT)	 
\\ooo\t\tCharacter with octal value ooo\t\t\t\t(3,5)
\\xhh\t\tCharacter with hex value hh\t\t\t\t(4,5)

Notes:

1.Individual code units which form parts of a surrogate pair can be encoded using this escape sequence.
2.Any Unicode character can be encoded this way, but characters outside the Basic Multilingual Plane (BMP) will be encoded using a surrogate pair if Python is compiled to use 16-bit code units (the default).
3.As in Standard C, up to three octal digits are accepted.
4.Unlike in Standard C, exactly two hex digits are required.
5.In a string literal, hexadecimal and octal escapes denote the byte with the given value; it is not necessary that the byte encodes a character in the source character set. In a Unicode literal, these escapes denote a Unicode character with the given value.
"""

print """
\\\\ Hey a back slash
\\\' Hey a single quotation marks
\\\" Hey a double quotation marks

Following line are formatted like 'PREDECESSOR\\$SUCCESSOR'

\\a What for ???
PREDECESSOR\aSUCCESSOR
\\b Backspace, get it
PREDECESSOR\bSUCCESSOR
\\f Formfeed? next line start from next char
PREDECESSOR\fSUCCESSOR
\\n return
PREDECESSOR\nSUCCESSOR
\\r back to the first pos in current line
PREDECESSOR\rSUCCESSOR
\\t horizontal tab
PREDECESSOR\tSUCCESSOR
\\v Vertical tab? can't understand
PREDECESSOR\vSUCCESSOR
"""