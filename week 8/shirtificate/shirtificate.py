from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 55)
        self.image("shirtificate.png", 20, 80, 170)
        self.cell(80)
        self.cell(30, 70, "CS50 Shirtificate", align="C")
        self.ln(90)

def get_name():
    return f"{input("Name: ")} took CS50"

def make_shirtificate(name):
    shirtificate = PDF()
    shirtificate.add_page()
    shirtificate.set_font("helvetica", "", 25)
    shirtificate.set_text_color(255,255,255)
    shirtificate.cell(80)
    shirtificate.cell(30, 70, name, align="C")
    shirtificate.output("shirtificate.pdf")

def main ():
    name = get_name()
    make_shirtificate(name)



if __name__ == "__main__":
    main()
