def preprocess_text_file(input_file, output_file):
    # Đọc nội dung từ tệp
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # Chuyển nội dung về dạng chữ thường
    processed_content = content.lower()
    # Ghi nội dung đã xử lý vào tệp mới
    with open(output_file, 'w') as file:
        file.write(processed_content)

# Ví dụ sử dụng

input_file = 'SOL.txt'
output_file = 'AliceInTheDreamWorld.txt'
preprocess_text_file(input_file, output_file)

print(f"Nội dung đã được chuyển đổi và lưu vào {output_file}")
