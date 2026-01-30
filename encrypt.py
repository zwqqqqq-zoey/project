# encrypt.py
import os
from dotenv import load_dotenv

# 1. 加载 .env 文件中的配置
load_dotenv()

# 2. 从环境变量安全读取密钥（而不是硬编码）
SHIFT = int(os.getenv("CAESAR_SHIFT", 3))  # 默认值3，但优先从.env读取
SECRET_KEY = os.getenv("SECRET_KEY", "default_key")  # 添加另一个密钥示例


def caesar_encrypt(text, shift=None):
    """凯撒加密函数"""
    if shift is None:
        shift = SHIFT  # 使用从.env读取的shift值

    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result += encrypted_char
        else:
            result += char
    return result


def caesar_decrypt(text, shift=None):
    """凯撒解密函数"""
    if shift is None:
        shift = SHIFT

    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            result += decrypted_char
        else:
            result += char
    return result


# 3. 演示程序
if __name__ == "__main__":
    print(f"使用的移位值（从.env读取）: {SHIFT}")
    print(f"使用的密钥（从.env读取）: {SECRET_KEY}")
    print("-" * 40)

    # 示例
    first_password = "hello world"
    encrypted = caesar_encrypt(first_password)
    decrypted = caesar_decrypt(encrypted)

    print(f"原文: {first_password}")
    print(f"加密后: {encrypted}")
    print(f"解密后: {decrypted}")

    # 验证
    assert first_password == decrypted, "解密失败！"
    print("\n✅ 加密/解密成功！")