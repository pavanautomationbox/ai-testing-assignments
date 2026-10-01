print("--2-Multiple Inheritance----")
class Developer:
    def write_code(self):
        print("Developer code complete.")

class Tester:
    def test_application(self):
        print("Tested application.")

class Sdet(Developer,Tester):
    def automate_tests(self):
        print("test automation completed.")

sdet=Sdet()
sdet.write_code()
sdet.test_application()
sdet.automate_tests()