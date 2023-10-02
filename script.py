from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import argparse

def encrypt_file(input_file, output_file, public_key):
    with open(public_key, 'r') as f:
        key = RSA.import_key(f.read())
    cipher = PKCS1_OAEP.new(key)
    with open(input_file, 'rb') as f:
        plaintext = f.read()
    ciphertext = cipher.encrypt(plaintext)
    with open(output_file, 'wb') as f:
        f.write(ciphertext)

    print(f"文件 {input_file} 已加密并保存到 {output_file}")

def decrypt_file(input_file, output_file, private_key):
    with open(private_key, 'r') as f:
        key = RSA.import_key(f.read())
    cipher = PKCS1_OAEP.new(key)
    with open(input_file, 'rb') as f:
        ciphertext = f.read()
    plaintext = cipher.decrypt(ciphertext)
    with open(output_file, 'wb') as f:
        f.write(plaintext)

    print(f"文件 {input_file} 已解密并保存到 {output_file}")

def generate_key_pair(public_key_file, private_key_file):
    key = RSA.generate(2048)
    with open(public_key_file, 'w') as f:
        f.write(key.publickey().export_key().decode())
    with open(private_key_file, 'w') as f:
        f.write(key.export_key().decode())
    print(f"公钥已保存到 {public_key_file}")
    print(f"私钥已保存到 {private_key_file}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='RSA加密/解密脚本')
    parser.add_argument('mode', choices=['encrypt', 'decrypt', 'generate'], help='加密、解密或生成密钥对模式')
    parser.add_argument('input_file', nargs='?', help='输入文件路径')
    parser.add_argument('output_file', nargs='?', help='输出文件路径')
    parser.add_argument('key_file', nargs='?', help='公钥或私钥文件路径')

    args = parser.parse_args()

    if args.mode == 'encrypt':
        encrypt_file(args.input_file, args.output_file, args.key_file)
    elif args.mode == 'decrypt':
        decrypt_file(args.input_file, args.output_file, args.key_file)
    elif args.mode == 'generate':
        generate_key_pair(args.input_file, args.output_file)