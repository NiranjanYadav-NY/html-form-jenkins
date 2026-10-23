from html.parser import HTMLParser

class FormTest(HTMLParser):
    def __init__(self):
        super().__init__()
        self.form_found = False
        self.fields = {}
        self.submit_found = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)

        if tag == "form":
            self.form_found = True

        if tag == "input":
            self.fields[attrs.get("name")] = attrs.get("type")

        if tag == "button" and attrs.get("type") == "submit":
            self.submit_found = True

parser = FormTest()

with open("index.html", encoding="utf-8") as file:
    parser.feed(file.read())

assert parser.form_found, "Form not found"
assert parser.fields.get("name") == "text", "Name field missing"
assert parser.fields.get("email") == "email", "Email field missing"
assert parser.fields.get("contact") == "tel", "Contact field missing"
assert parser.submit_found, "Submit button missing"

print("All HTML form tests passed!")
