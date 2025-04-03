import base64
def main():
    input_string = input("Nhập thông tin cần mã hóa: ")
    encoded_bytes = base64.b64encode(input_string.encode("utf-8"))
    encoded_string = str(encoded_bytes, "utf-8")
    with open("data.txt", "w") as file:
        file.write(encoded_string)
    print(f"Đã mã hóa  và lưu vào tệp data.txt")
if __name__ == "__main__":
    main()