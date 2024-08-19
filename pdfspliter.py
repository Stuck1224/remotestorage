from PyPDF2 import PdfReader, PdfWriter


def split_pdf(input_pdf, start_page, end_page, output_pdf):
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    # 添加指定页面范围到新的PDF文件中
    for i in range(start_page - 1, end_page):
        writer.add_page(reader.pages[i])

    # 保存新的PDF文件
    with open(output_pdf, "wb") as output_file:
        writer.write(output_file)


# 使用示例
split_pdf("D:\\ebooks\\Computervision.pdf", 490, 539, "splited.pdf")
