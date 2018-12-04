decode_binary_to_string(text):
	return ''.join(chr(int(text[i*8:i*8+8],2)) for i in range(len(text)//8))

decode_string_to_binary(binary):
	return ' '.join(format(ord(x), 'b') for x in binary)