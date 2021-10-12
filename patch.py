import json

def xor(data):
    return bytearray((data[i] ^ ord("Q") for i in range(0, len(data))))

config = {}
config['Hostname'] = "kunnoh"
config['Migrate'] = "sec"

config = json.dumps(config).encode()
padding = b"\x00" * (2000 - len(config) - 1)
config = xor(config) + b"\xff"+ padding

# Find {"Hostname"
with open('c2', 'rb') as binFile:
    byte_data = bytearray(binFile.read())
binFile.close()
offset = byte_data.find(b'{"Hostname"')
print(offset)

# write data
with open('c2', 'r+b') as binFile:
     binFile.seek(offset)
     binFile.write(config)
binFile.close()