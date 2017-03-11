import hex_base64_converter

def task1():
    hex_string = "faea8766efd8b295a633908a3c0828b22640e1e9122c3c9cfb7b59b7cf3c9d448bf04d72cde3aaa0"
    base64_string = "+uqHZu/YspWmM5CKPAgosiZA4ekSLDyc+3tZt888nUSL8E1yzeOqoA=="

    print("Source string in hex:")
    print(hex_string)
    print("HEX -> BASE64:")
    print(hex_base64_converter.toBase64(hex_string))

    print("Source string in base64:")
    print(base64_string)
    print("BASE64 -> HEX:")
    print(hex_base64_converter.toHex(base64_string))
