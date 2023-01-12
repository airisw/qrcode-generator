import qrcode

def main():
    link = input("Social media link: ")
    generate(link)

def generate(link):
    img = qrcode.make(link)
    file = input("Save file as: ")
    img.save(f"{file}.png")

if __name__ == "__main__":
    main()
